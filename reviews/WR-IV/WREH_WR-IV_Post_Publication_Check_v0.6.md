# WR-IV v0.6 — publication identity check

Checked: 8 October 2026, after the author reported publication. This is a publication/provenance check, not a new independent scientific audit.

The public Zenodo API for [record 23248138](https://zenodo.org/records/23248138) returned the assigned version DOI **10.5281/zenodo.23248138**, publication date **2026-10-08**, open access, resource type **Preprint**, author **Malachevsky, A. A.**, ORCID **0009-0008-6009-3196** and record licence **CC BY 4.0**. Its parent/concept DOI is **10.5281/zenodo.23248137**; the version DOI is used for WR-IV citations. Version v0.6 is established from the filenames and repository checksums, not from a record-level version field.

[PR #5](https://github.com/AIDevelopersMonster/WREH/pull/5) is merged. Source head: `a2dd6f60400ef429c5da2b8e914415a57a715a3f`; merge into main: `a82ca16675a6b3f358d800963fa7ff0c4e5385bb`, 2026-10-08T21:27:45Z.

## File comparison

The published size/MD5 pairs exactly match the corresponding files at the merged repository snapshot. The local SHA-256 hashes below were also calculated. This comparison uses the public record's published checksums; it is not represented as a second full download of all published bytes.

| File | Bytes | Published/repository MD5 | Repository SHA-256 |
|---|---:|---|---|
| WREH_WR-IV_Preprint_v0.6_EN.pdf | 162297 | `7a8b6395bfec11ddc8d1475b48a38e8a` | `c51f9ec383ba370cb3263c2bcca51ade81c8e61c7d52e0ab084fb183e1d1792a` |
| WREH_WR-IV_Preprint_v0.6_RU.pdf | 177360 | `59f17dada07ed509213d9902d626a0ed` | `a03989d39a24dcd4a9838fb362338d16b1dc544465ed356a787c2e08d36cfaaf` |
| WREH_WR-IV_Demo_v0.6_EN-RU.html | 38887 | `5cbadca08dabe5c147f525e1c975fbe0` | `2353c7130fb3ecbd64c669074974dea631c2cf9e83bdfa30a30aab65cb75ae61` |

## Metadata follow-up

- The record has the two PDFs and HTML, but not the prepared full source/reproduction ZIP. The complete source remains in the repository; an archive upload would improve the deposit.
- The keywords field is one long string containing several semicolon-separated keywords plus pre-deposit prose, including the obsolete assertion that no WR-IV DOI has been assigned. It should be split into individual keywords and that obsolete prose removed.
- The record's description is the English abstract. The prepared bilingual description and explicit split CC BY/MIT supplement notice were not fully transferred into the visible metadata. The HTML's code licence remains established by the repository notices; a record-level CC BY label alone should not be used to infer a different licence for that code.
- The two published PDFs retain historical pre-deposit wording. Frozen PDFs and checksums are not rewritten in the WR-V transition; the assigned DOI is recorded in current project documentation.

No Zenodo metadata mutation or new upload was made in this transition. These metadata/archive follow-ups do not change the WR-IV mathematical interfaces or prevent a review draft of WR-V. They are not silently marked corrected.
