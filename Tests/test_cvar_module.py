import numpy as np
from cvar_module import value_at_risk, conditional_value_at_risk, cvar_adjusted_update
def test_invariants_and_shift():
    rng = np.random.default_rng(0); T=4000
    R = np.column_stack([rng.normal(0,0.01,T), rng.normal(0,0.01,T)+rng.standard_t(3,T)*0.02])
    w0 = np.array([0.5,0.5]); w1 = cvar_adjusted_update(w0, returns_matrix=R, alpha=0.05, lam=25.0)
    assert np.all(w1>=0) and np.isclose(w1.sum(),1.0) and w1[1] < w1[0]
