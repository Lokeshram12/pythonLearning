import multiprocessing
import math
import time

def is_prime(num):
    """Function to check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # other even numbers are not prime
    sqrt_num = int(math.sqrt(num)) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end, result_queue):
    """Function to find all prime numbers in a given range [start, end) and put them into a queue."""
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    result_queue.put(primes)

def parallel_find_primes_in_range(num_range, num_processes):
    """Function to parallelize finding primes in a given range using multiprocessing."""
    start_time = time.time()

    # Calculate chunk size for each process
    chunk_size = math.ceil((num_range[1] - num_range[0]) / num_processes)
    processes = []
    result_queue = multiprocessing.Queue()

    # Create processes
    for i in range(num_processes):
        start = num_range[0] + i * chunk_size
        end = min(num_range[1], start + chunk_size)
        process = multiprocessing.Process(target=find_primes_in_range, args=(start, end, result_queue))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    # Collect results from the queue
    all_primes = []
    while not result_queue.empty():
        all_primes.extend(result_queue.get())

    end_time = time.time()
    print(f"Found {len(all_primes)} prime numbers in range {num_range} in {end_time - start_time} seconds.")
    return all_primes

if __name__ == '__main__':
    num_range = (1, 10000)  # Define the range to find primes
    num_processes = 4  # Number of processes to use

    prime_numbers = parallel_find_primes_in_range(num_range, num_processes)
    print("Prime numbers found:", prime_numbers)
