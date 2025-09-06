import numpy as np
from cvar_module import cvar_adjusted_update
if __name__ == "__main__":
    rng = np.random.default_rng(1); T=3000
    R = np.column_stack([rng.normal(0.001,0.01,T), rng.normal(0.001,0.01,T)+rng.standard_t(3,T)*0.02])
    w = np.array([0.5,0.5]); print("w_next:", cvar_adjusted_update(w, returns_matrix=R))
