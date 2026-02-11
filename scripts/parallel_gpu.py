# %%

import time

import numpy as np

try:
    import cupy as cp
except ImportError:
    cp = None

mu = 2


def ci_bounds(x):
    # x is a 1D numpy array of random variables
    n = len(x)
    xbar = np.mean(x)
    sig = np.std(x)
    upper = xbar + 1.96 / np.sqrt(n) * sig
    lower = xbar - 1.96 / np.sqrt(n) * sig
    return {"lower": lower, "upper": upper}


def capture_cpu(_):
    x = np.random.poisson(mu, sample_size)
    bounds = ci_bounds(x)
    return (bounds["lower"] <= mu) & (mu <= bounds["upper"])


def coverage_gpu(rep, n, lam):
    # All replications are generated and processed on GPU in parallel.
    x = cp.random.poisson(lam=lam, size=(rep, n))
    xbar = cp.mean(x, axis=1)
    sig = cp.std(x, axis=1)
    margin = (1.96 / np.sqrt(n)) * sig
    covered = (xbar - margin <= lam) & (lam <= xbar + margin)
    return cp.mean(covered)


Rep = 200; sample_size = 200000
# Rep = 2000; sample_size = 20

# Rep = 100000
# sample_size = 5
print(f"Sample size = {sample_size}, replications = {Rep}:")

pts0 = time.time()
out_cpu = [capture_cpu(i) for i in range(Rep)]
pts1 = time.time() - pts0
print(f"* single-core CPU loop takes {pts1:.4f} seconds")
print(f"* CPU coverage = {np.mean(out_cpu):.4f}")

if __name__ == "__main__":
    if cp is None:
        print("* GPU run skipped: cupy is not installed.")
    else:
        try:
            n_gpu = cp.cuda.runtime.getDeviceCount()
            if n_gpu < 1:
                print("* GPU run skipped: no CUDA device detected.")
            else:
                props = cp.cuda.runtime.getDeviceProperties(0)
                gpu_name = props["name"].decode("utf-8")
                print(f"* GPU device: {gpu_name}")

                pts2 = time.time()
                out_gpu = coverage_gpu(Rep, sample_size, mu)
                cp.cuda.Stream.null.synchronize()
                pts3 = time.time() - pts2

                print(f"* GPU parallel run takes {pts3:.4f} seconds")
                print(f"* GPU coverage = {float(out_gpu.get()):.4f}")
        except cp.cuda.runtime.CUDARuntimeError as err:
            print(f"* GPU run skipped: {err}")

# %%

