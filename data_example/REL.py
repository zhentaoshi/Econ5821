# relaxed empirical likelihood

import numpy as np
import cvxpy as cp
from scipy.sparse import csc_matrix, hstack, vstack

def innerloop(b, y, X, Z, tau):
    n, p = X.shape
    m, k = Z.shape

    # Generate moment condition
    H = MomentMatrix(y, X, Z, b)

    # Initialize the CVXPY problem
    beta = cp.Variable(p)
    u = cp.Variable(n)
    v = cp.Variable(n)
    obj = cp.Maximize(cp.sum(u) - tau * cp.sum(v))
    constr = [H @ beta + Z @ u - v == np.ones(m),
              u >= 0,
              v >= 0,
              beta >= 0]
    prob = cp.Problem(obj, constr)

    # Solve the problem
    prob.solve(solver=cp.MOSEK, verbose=False)

    if prob.status == 'optimal':
        # Return the optimal value
        return -prob.value
    else:
        # Return infinity if the problem is infeasible
        print('WARNING: Inner loop not optimized')
        return np.inf

