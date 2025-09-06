# CVaR Adjusted Update Module (Paper 3)

This repository provides a production-ready implementation of a per-asset CVaR-adjusted reweighting. Assets with heavier downside tails get down-weighted:

Adj_i = exp(-λ * CVaR_i(α)),    w' = ΠΔ( w ⊙ Adj )

See README for usage and publishing with ORCID + Zenodo.
