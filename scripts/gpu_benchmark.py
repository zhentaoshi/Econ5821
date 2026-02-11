"""
GPU Benchmark Script
Tests GPU performance using CuPy with matrix operations and random number generation.
"""

import time
import numpy as np

try:
    import cupy as cp
except ImportError:
    print("CuPy is not installed. Run: pip install cupy-cuda12x")
    exit(1)


def benchmark_matrix_mult(size):
    """Benchmark matrix multiplication."""
    print(f"\n{'='*60}")
    print(f"Matrix Multiplication: {size}x{size}")
    print(f"{'='*60}")

    # CPU
    A_cpu = np.random.rand(size, size)
    B_cpu = np.random.rand(size, size)
    t0 = time.time()
    C_cpu = A_cpu @ B_cpu
    cpu_time = time.time() - t0
    print(f"CPU:  {cpu_time:.4f} seconds")

    # GPU
    A_gpu = cp.array(A_cpu)
    B_gpu = cp.array(B_cpu)
    t0 = time.time()
    C_gpu = A_gpu @ B_gpu
    cp.cuda.Stream.null.synchronize()
    gpu_time = time.time() - t0
    print(f"GPU:  {gpu_time:.4f} seconds")
    print(f"Speedup: {cpu_time/gpu_time:.2f}x")


def benchmark_random_stats(samples, size):
    """Benchmark random number generation and statistics."""
    print(f"\n{'='*60}")
    print(f"Random Generation & Stats: {samples:,} samples of {size:,} elements")
    print(f"{'='*60}")

    # CPU
    t0 = time.time()
    x_cpu = np.random.randn(samples, size)
    mean_cpu = np.mean(x_cpu, axis=1)
    std_cpu = np.std(x_cpu, axis=1)
    cpu_time = time.time() - t0
    print(f"CPU:  {cpu_time:.4f} seconds")

    # GPU
    t0 = time.time()
    x_gpu = cp.random.randn(samples, size)
    mean_gpu = cp.mean(x_gpu, axis=1)
    std_gpu = cp.std(x_gpu, axis=1)
    cp.cuda.Stream.null.synchronize()
    gpu_time = time.time() - t0
    print(f"GPU:  {gpu_time:.4f} seconds")
    print(f"Speedup: {cpu_time/gpu_time:.2f}x")


def benchmark_elementwise(size):
    """Benchmark element-wise operations."""
    print(f"\n{'='*60}")
    print(f"Element-wise Operations: {size:,} elements")
    print(f"{'='*60}")

    # CPU
    x_cpu = np.random.rand(size)
    y_cpu = np.random.rand(size)
    t0 = time.time()
    z_cpu = 2.0 * x_cpu**2 + 3.0 * y_cpu**3 + np.sin(x_cpu) * np.cos(y_cpu)
    cpu_time = time.time() - t0
    print(f"CPU:  {cpu_time:.4f} seconds")

    # GPU
    x_gpu = cp.array(x_cpu)
    y_gpu = cp.array(y_cpu)
    t0 = time.time()
    z_gpu = 2.0 * x_gpu**2 + 3.0 * y_gpu**3 + cp.sin(x_gpu) * cp.cos(y_gpu)
    cp.cuda.Stream.null.synchronize()
    gpu_time = time.time() - t0
    print(f"GPU:  {gpu_time:.4f} seconds")
    print(f"Speedup: {cpu_time/gpu_time:.2f}x")


def main():
    print(f"\n{'#'*60}")
    print("# GPU Benchmark Testing")
    print(f"{'#'*60}")

    # Get GPU info
    n_gpu = cp.cuda.runtime.getDeviceCount()
    if n_gpu < 1:
        print("\nError: No CUDA device detected")
        return

    props = cp.cuda.runtime.getDeviceProperties(0)
    gpu_name = props["name"].decode("utf-8")
    multi_processor_count = props["multiProcessorCount"]
    # maxThreadsPerMultiprocessor may not be available on all GPU architectures
    max_threads_per_multiprocessor = props.get("maxThreadsPerMultiprocessor", 2048)
    
    print(f"\nGPU Device: {gpu_name}")
    print(f"CUDA Version: {cp.cuda.runtime.runtimeGetVersion()}")
    print(f"CuPy Version: {cp.__version__}")
    print(f"Multiprocessors: {multi_processor_count}")
    print(f"Max Threads per MP: {max_threads_per_multiprocessor}")
    print(f"Total CUDA Cores: ~{multi_processor_count * 128}")

    # Run benchmarks
    benchmark_elementwise(10_000_000)
    benchmark_random_stats(100_000, 1000)
    benchmark_matrix_mult(2048)

    print(f"\n{'='*60}")
    print("Benchmark completed!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()