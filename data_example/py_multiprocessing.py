import multiprocessing

def compute_square(n):
    return n * n

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    results = pool.map(compute_square, range(10))

    print(results)


######### another example
    
import multiprocessing

# Define a worker function
def worker(num):
    return num ** 2

if __name__ == '__main__':
    # Define the dataset
    data = [2, 3, 4, 5, 6]

    # Create a multiprocessing Pool
    with multiprocessing.Pool() as pool:
        # Map worker function to data
        result = pool.map(worker, data)

    print(result)

###################
