from __future__ import annotations
import numpy as np

_EPS = 1e-12
def value_at_risk(losses, alpha=0.05):
    L = np.asarray(losses, dtype=float).ravel()
    return np.percentile(L, 100*(1-alpha))
def conditional_value_at_risk(losses, alpha=0.05):
    L = np.asarray(losses, dtype=float).ravel()
    v = value_at_risk(L, alpha)
    tail = L[L>=v]
    return float(tail.mean()) if tail.size else float(v)
def projected_simplex(v, s=1.0):
    v = np.asarray(v, dtype=float)
    u = np.sort(v)[::-1]; cssv = np.cumsum(u)
    rho = np.nonzero(u*np.arange(1, v.size+1) > (cssv - s))[0][-1]
    theta = (cssv[rho]-s)/(rho+1.0)
    w = np.maximum(v-theta, 0.0); sw = w.sum(); return w/sw
def cvar_per_asset(returns_matrix, alpha=0.05):
    R = np.asarray(returns_matrix, dtype=float); L = -R
    return np.array([conditional_value_at_risk(L[:,i], alpha) for i in range(R.shape[1])])
def cvar_adjusted_update(weights, returns_matrix=None, per_asset_cvar=None, alpha=0.05, lam=25.0, clip_min=1e-12):
    w = np.asarray(weights, dtype=float); w = w/w.sum()
    cvars = per_asset_cvar if per_asset_cvar is not None else cvar_per_asset(returns_matrix, alpha)
    adj = np.exp(-lam*np.asarray(cvars, dtype=float))
    new_w = np.maximum(w*adj, clip_min)
    return projected_simplex(new_w, 1.0)
