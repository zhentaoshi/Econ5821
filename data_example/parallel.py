# %%

import numpy as np
import time

mu = 2 

def CI(x):
    # x is a numpy array of random variables
    n = len(x)
    mu = np.mean(x)
    sig = np.std(x)
    upper = mu + 1.96 / np.sqrt(n) * sig
    lower = mu - 1.96 / np.sqrt(n) * sig
    return {"lower": lower, "upper": upper}


def capture(i):
    x = np.random.poisson(mu, sample_size)
    bounds = CI(x)  # You need to define the CI function in Python
    return (bounds['lower'] <= mu) & (mu <= bounds['upper'])


Rep = 200; sample_size = 200000
# Rep = 2000; sample_size = 20

# Rep = 10000; sample_size = 10
print(f"Sample size = {sample_size}, replications = {Rep}:")
    

pts0 = time.time()  # check time
out = [capture(i) for i in range(Rep)]  # single-core execution of capture function
pts1 = time.time() - pts0  # check time elapsed
print(f"* single-core loop takes {pts1} seconds")


# start parallel execution
from multiprocessing import Pool

num_cores = 8  # number of cores
pts2 = time.time()  # check time

if __name__ == '__main__':  # required for Windows
    with Pool(num_cores) as pool:  # open 2 CPUs
        out = pool.map(capture, range(Rep))

    pts3 = time.time() - pts2  # check time elapsed
    print(f"* {num_cores}-core parallel loop takes {pts3} seconds")
    # print(f"* coverage =  {np.mean(out):.4f}")
# %%
