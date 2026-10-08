#!/usr/bin/env python3
"""Regenerate WR-IV v0.6 analytic figures and verify Gaussian benchmarks.

MIT License; Copyright (c) 2026 A. A. Malachevsky.
Figures are research content under CC BY 4.0. No experimental data are used.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / 'figures'


def marginal(x0, kappa, horizon, time, datum, noise_variance=0.0):
    if not (kappa > 0 and horizon > 0 and 0 <= time <= horizon and noise_variance >= 0):
        raise ValueError('Invalid diffusion parameters')
    denominator = 2 * kappa * horizon + noise_variance
    mean = x0 + 2 * kappa * time / denominator * (datum - x0)
    variance = 2 * kappa * time - (2 * kappa * time) ** 2 / denominator
    return mean, max(0.0, variance)


def filter_and_smooth(q, r, y, x0=0.0):
    q, r, y = map(lambda a: np.asarray(a, dtype=float), (q, r, y))
    if not (len(q) == len(r) == len(y) and np.all(q > 0) and np.all(r > 0)):
        raise ValueError('Positive variances and matching lengths required')
    means, variances = [float(x0)], [0.0]
    for qi, ri, yi in zip(q, r, y):
        predicted_variance = variances[-1] + qi
        gain = predicted_variance / (predicted_variance + ri)
        means.append(means[-1] + gain * (yi - means[-1]))
        variances.append((1 - gain) * predicted_variance)
    smooth_means, smooth_variances = np.array(means), np.array(variances)
    for k in range(len(q) - 1, -1, -1):
        gain = variances[k] / (variances[k] + q[k])
        smooth_means[k] = means[k] + gain * (smooth_means[k + 1] - means[k])
        smooth_variances[k] = variances[k] + gain**2 * (
            smooth_variances[k + 1] - variances[k] - q[k])
    return np.array(means), np.array(variances), smooth_means, smooth_variances


def batch_condition(q, r, y, x0=0.0):
    # Independently construct the full prior state covariance, then Schur complement.
    times = np.cumsum(q)
    prior_covariance = np.minimum.outer(times, times)
    observation_covariance = prior_covariance + np.diag(r)
    mean = x0 + prior_covariance @ np.linalg.solve(observation_covariance, np.array(y) - x0)
    covariance = prior_covariance - prior_covariance @ np.linalg.solve(
        observation_covariance, prior_covariance)
    return mean, covariance


def verify():
    rng = np.random.default_rng(20261008)
    count = 0
    for length in (1, 2, 4, 9):
        for _ in range(20):
            q = np.exp(rng.normal(size=length))
            r = np.exp(rng.normal(size=length))
            y = rng.normal(size=length)
            x0 = float(rng.normal())
            mf, pf, ms, ps = filter_and_smooth(q, r, y, x0)
            mb, pb = batch_condition(q, r, y, x0)
            np.testing.assert_allclose(ms[1:], mb, rtol=1e-10, atol=1e-10)
            np.testing.assert_allclose(ps[1:], np.diag(pb), rtol=1e-10, atol=1e-10)
            assert np.all(ps >= -1e-12) and np.all(ps <= pf + 1e-12)
            count += 1
    mf, pf, ms, ps = filter_and_smooth([1, 1], [1, 1], [.2, 1.4])
    np.testing.assert_allclose([mf[1], pf[1], mf[2], pf[2], ms[1], ps[1]],
                               [.1, .5, .88, .6, .36, .4], atol=1e-12)
    for kappa, horizon in ((.5, 1), (2.7, 3.1)):
        for fraction in (.001, .2, .6, .999):
            time = fraction * horizon
            _, exact = marginal(0, kappa, horizon, time, 2.5)
            _, noisy = marginal(0, kappa, horizon, time, 2.5, .5)
            prior = 2 * kappa * time
            np.testing.assert_allclose(exact, 2 * kappa * time * (horizon-time) / horizon)
            assert 0 < exact < noisy < prior
        assert marginal(0, kappa, horizon, 0, 2.5)[1] == 0
        assert marginal(0, kappa, horizon, horizon, 2.5)[1] == 0
        np.testing.assert_allclose(marginal(0, kappa, horizon, .6*horizon, 2.5, 1e14)[1],
                                   2*kappa*.6*horizon, rtol=1e-12)
    return {'seed': 20261008, 'independent_RTS_batch_cases': count,
            'two_observation_example': {'filtered_mean_1': .1, 'filtered_variance_1': .5,
                                        'smoothed_mean_1': .36, 'smoothed_variance_1': .4},
            'result': 'passed'}


def figures():
    FIGURES.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'axes.grid': True, 'grid.alpha': .18, 'pdf.fonttype': 42})
    colors = ['#697580', '#096a8b', '#ca7721', '#b04c76', '#5e7399']
    for lang in ('en', 'ru'):
        russian = lang == 'ru'
        fig, ax = plt.subplots(figsize=(7.1, 3.7), layout='constrained')
        q = np.linspace(0, 1, 401)
        ax.plot(q, q, color=colors[0], ls='--', lw=1.8,
                label='Априорная' if russian else 'Prior')
        ax.plot(q, q*(1-q), color=colors[1], lw=2.5,
                label='Точный мост' if russian else 'Exact bridge')
        for j, r in enumerate((.05, .5, 5)):
            ax.plot(q, q-q*q/(1+r), color=colors[j+2], lw=1.7,
                    label=('Шум' if russian else 'Noise') + f' r = {r:g}')
        ax.set(xlim=(0, 1), ylim=(0, 1.025), xlabel='q = t / T',
               ylabel=('Дисперсия / (2κT)' if russian else 'Variance / (2κT)'))
        ax.legend(loc='upper left', frameon=False, fontsize=9)
        fig.savefig(FIGURES / f'variance_{lang}.pdf')
        fig.savefig(FIGURES / f'variance_{lang}.png', dpi=170)
        plt.close(fig)
        fig, (ax, intervals) = plt.subplots(2, 1, figsize=(7.1, 4.1),
                                           height_ratios=(3, 1.25), sharex=True,
                                           layout='constrained')
        laws = [(0, .6), marginal(0, .5, 1, .6, 2.5), marginal(0, .5, 1, .6, 2.5, .5)]
        labels = ['Априорный закон', 'Точный отсчёт', 'Шумный отсчёт'] if russian else [
                  'Prior', 'Exact endpoint', 'Noisy endpoint']
        x = np.linspace(-3, 4.2, 650)
        for j, ((mean, var), label) in enumerate(zip(laws, labels)):
            density = np.exp(-(x-mean)**2/(2*var))/np.sqrt(2*np.pi*var)
            ax.plot(x, density, color=colors[j], lw=2, label=label)
            intervals.plot([mean-2*np.sqrt(var), mean+2*np.sqrt(var)], [2-j, 2-j],
                           color=colors[j], lw=4, solid_capstyle='round')
            intervals.plot(mean, 2-j, 'o', color=colors[j], ms=5)
        ax.set(ylabel='Плотность' if russian else 'Density')
        ax.legend(frameon=False, fontsize=9)
        intervals.set(yticks=range(3), yticklabels=list(reversed(labels)), ylim=(-.6, 2.6),
                      xlabel='x', xlim=(-3, 4.2))
        intervals.grid(axis='y', visible=False)
        fig.savefig(FIGURES / f'densities_{lang}.pdf')
        fig.savefig(FIGURES / f'densities_{lang}.png', dpi=170)
        plt.close(fig)


if __name__ == '__main__':
    result = verify()
    figures()
    (ROOT / 'verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
