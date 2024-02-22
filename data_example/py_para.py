# %%
import numpy as np
import pandas as pd
import time

def CI(x):
    # x is a numpy array of random variables
    n = len(x)
    mu = np.mean(x)
    sig = np.std(x)
    upper = mu + 1.96 / np.sqrt(n) * sig
    lower = mu - 1.96 / np.sqrt(n) * sig
    return {"lower": lower, "upper": upper}

# ## Parallel Computing

# %%
Rep = 100
sample_size = 100
mu = 2

import numpy as np
from scipy.stats import poisson
import time

### efficient loop.
# encapsulate the code in a function

def capture(i):
    x = np.random.poisson(mu, sample_size)
    bounds = CI(x)  # You need to define the CI function in Python
    return (bounds['lower'] <= mu) & (mu <= bounds['upper'])


out = [capture(i) for i in range( Rep)]
# print( np.mean(out) )

# %%
Rep = 20; sample_size = 2000000

# single-core execution
pts0 = time.time()  # check time
out = [capture(i) for i in range(Rep)]  # single-core execution of capture function
pts1 = time.time()# - pts0  # check time elapsed
# print(f"single-core loop takes {pts1 - pts0} seconds")

# multi-core execution
from multiprocessing import Pool
# %%
pts2 = time.time()  # check time elapsed

if __name__ == '__main__':
    with Pool(4) as p:  # open 2 CPUs
        out = p.map(capture, range(Rep))  # parallel execution of capture function
        pts3 = time.time()#  - pts2  # check time elapsed
        print(f"single-core loop takes {pts1 - pts0} seconds")
        print(f"2-core parallel loop takes {pts3 - pts2} seconds")

# pts3 = time.time()#  - pts2  # check time elapsed
# print(f"2-core parallel loop takes {pts3 - pts2} seconds")

# %%
