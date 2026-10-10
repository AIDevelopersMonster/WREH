# WR-VII v0.2 — result and dependency map

Carrier: normalized absolutely continuous pure states, integrable finite-dimensional Hermitian Hamiltonians, orthogonal projector Q, Qψ(0)=0. Resource: Hamiltonian spectral diameter in joules, elapsed evolution time in seconds. Only scalar identity shifts are removed as gauge; lab axes are fixed.

| Result | Input | Conclusion | Dependency and boundary |
|---|---|---|---|
| Definition 2.1 | Fixed carrier/protocol, cap E, time τ, response set J | Generator-history completion class C(E,τ,J) | ∃ one compatible history; not all controls or a full world |
| Theorem 3.1 | Integrable operator norm, pure closed unitary dynamics | arcsin√p ≤ ∫D/(2ℏ) | Orthogonal projector split; endpoint-safe regularized chain rule; elementary speed-limit argument |
| Corollary 3.2 | D≤E, prescribed qubit preparation/projector, free transverse controls | Sharp frontier and full reachable probability interval | Thm 3.1 + explicit Pauli witness; sufficiency is qubit-specific |
| Theorem 4.1 | Constant traceless qubit, 0<p<1, fixed lab axes | All phase windows and latitude/azimuth parameters | Pauli exponential, no optimization; revival windows cannot be omitted |
| Corollary 4.2 | Constant family, 0<p≤1, C=arcsin√p | Fixed d=E with a circle of distinct H | Thm 4.1 and direct p=1 endpoint; no generator singleton |
| Theorem 5.1 | Constant frontier family; exact additional calibrated Pauli means | Final means identify H for 0<p<1; at p=1 final density fails, half-duration means identify | New data on fresh preparations; does not identify arbitrary time-dependent H |
| Proposition 6.1 | Nonempty closed response interval, qubit carrier | Feasible iff Eτ≥2ℏ arcsin√p₋ | Monotonicity + qubit witness; ∃ response in interval |
| Proposition 7.1 | Fixed N, iid Bernoulli means, uniform nonnegative calibration bias δ | Coverage ≥1−α; false exclusion ≤α within true capped model | Self-contained Bernoulli concentration; no adaptive stopping, drift or optimal sample law |

Seven proof blocks, thirteen numbered equations, thirty-one labels and twelve bibliography entries, with identical assignments in EN/RU. Numerical witnesses are regression checks, not general proof premises.

## Upstream and downstream

WR-I: response equivalence and projected identification; diameter is constant on the constrained frontier fibre, not asserted identifiable on every response fibre. WR-II: global realization needs its own carrier and existence assumptions; its Example 10.19 and WR-VI v0.2 Corollary 5.3 use nonclosed classes with excluded minimizers, unlike the attained circle here. WR-III: for fixed E,τ and 0<C<π/2, M=(0,1) has reachable image (0,sin²C] with boundary {sin²C}; this is a response-image boundary, not a proved structural wall or failure of local triviality. WR-IV: projected uniqueness does not identify a full history/world. WR-V: responses and transitions are different objects; its nonexclusive scenario labels remain intact. WR-VI: records distinguish observations, structure and independently supplied bounds; dimensionless activity is not promoted to energy.

This paper supplies a declared unit-bearing quantum response calculation. It does not determine manifesto energy suprema, object/vacuum lifetimes, effective-theory cutoffs, gravitational collapse or cosmological realizability. WR-VIII and WR-IX remain planned. WREH is a programme and community, separate from Boundary Compensation.

## v0.2 revision boundary

All seven proofs, all numbered result statements and all thirteen numbered equations are byte-identical to v0.1. Added prose positions the certificate against static orthogonalization bounds using state spread and mean energy above ground. Those state resources are not supplied assumptions of Theorem 3.1; the static mean-energy formula is not transferred to arbitrary H(t). Original references 1–10 retain their text and numbers; primary references 11–12 are appended.
