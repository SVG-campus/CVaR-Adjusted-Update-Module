# CVaR Adjusted Update Module (Paper 3)

*A per-asset tail-risk aware reweighting for portfolios.*

<!-- Replace after your first Zenodo release -->

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

This repository provides a production-ready, **reproducible** implementation of the **CVaR-Adjusted Update** described in the paper. The method explicitly **penalizes tail risk** by down-weighting assets with larger Conditional Value-at-Risk (CVaR) at level $\alpha$.

**Per-asset adjustment**

$$
\text{Adj}_i = \exp\!\big(-\lambda\,\text{CVaR}_i(\alpha)\big), \qquad
w' = \Pi_\Delta\!\left(w \odot \text{Adj}\right),
$$

where $\Pi_\Delta$ projects back to the probability simplex (non-negative, sums to 1).

---

## Quick start

```bash
# (optional) create venv
python -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate

pip install -r requirements.txt
pytest -q
python examples.py
```

---

## Usage

```python
import numpy as np
from cvar_module import (
    value_at_risk, conditional_value_at_risk,
    cvar_per_asset, cvar_adjusted_update
)

# toy returns (T x N) where columns are assets
rng = np.random.default_rng(0)
T, N = 2000, 3
R = np.column_stack([
    rng.normal(0.001, 0.01, T),                                   # milder tails
    rng.normal(0.001, 0.01, T) + rng.standard_t(3, T) * 0.01,     # heavier tails
    rng.normal(0.001, 0.012, T)
])

w0 = np.array([1/3, 1/3, 1/3])
w1 = cvar_adjusted_update(w0, returns_matrix=R, alpha=0.05, lam=25.0)
print("w1:", w1, "sum:", w1.sum())
```

**Key properties**

* **Per-asset CVaR** drives re-allocation — heavier downside tails → lower weight.
* Maintains a valid allocation (non-negative, **sums to 1**).
* Flexible API: pass a returns matrix, per-asset losses, or pre-computed CVaR values.

---

## Files included

* `cvar_module.py` — VaR/CVaR routines, per-asset CVaR, simplex projection, and update.
* `tests/test_cvar_module.py` — invariants + demonstrates down-weighting of tail-risky assets.
* `tests/test_artifacts_exist.py` — checks for `CVaR_Adjusted_Update_Module.pdf` and `Tests.zip` (skips gracefully if missing).
* `.github/workflows/ci.yml` — pytest on push/PR.
* `.github/workflows/release.yml` — GitHub Release on tags (works with Zenodo’s GitHub integration).
* `CITATION.cff` — citation metadata (includes your ORCID).
* `.zenodo.json` — deposition metadata for Zenodo.
* `requirements.txt`, `examples.py`, `CHANGELOG.md`, `LICENSE-CODE` (MIT), `LICENSE-DOCS` (CC BY 4.0), `.gitignore`.

**Research artifacts expected at repo root (already in your repo)**

* `CVaR_Adjusted_Update_Module.pdf`
* `Tests.zip` (or the unpacked test pages under a `Tests/` folder)

---

## ORCID & Zenodo integration

Your ORCID iD: **[https://orcid.org/0009-0004-9601-5617](https://orcid.org/0009-0004-9601-5617)**.

With GitHub ↔ Zenodo connected, **pushing a tag** triggers Zenodo to mint a DOI.

**Publish checklist**

1. Commit code + paper + tests.
2. Update versions in `CHANGELOG.md` and `CITATION.cff`.
3. Tag a release:

   ```bash
   git tag v0.1.0 && git push --tags
   ```
4. When the DOI appears on Zenodo, update the badge at the top of this README and add to:

   * `CITATION.cff` → `identifiers:`
   * (Optional) repo description/badges.
5. Check your **ORCID Works**; add the DOI manually if it didn’t auto-sync.

---

## Citing

See `CITATION.cff`. After your first Zenodo release, replace the placeholder DOI above.

```bibtex
@misc{cvaradj2025,
  title        = {CVaR Adjusted Update Module},
  author       = {Villalobos-Gonzalez, Santiago de Jesus},
  year         = {2025},
  note         = {Code and preprint. DOI to be added after first Zenodo release.},
  howpublished = {GitHub + Zenodo}
}
```

---

## License

* **Code**: MIT (see `LICENSE-CODE`)
* **Text/figures/PDFs**: CC BY 4.0 (see `LICENSE-DOCS`)

---

## Acknowledgements

Implements per-asset CVaR reweighting with numerically stable simplex projection and exponential damping $\exp(-\lambda\,\text{CVaR})$ to attenuate tail-risk-heavy assets.
