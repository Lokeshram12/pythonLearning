import multiprocessing
import numpy as np
import time

def matrix_multiply_chunk(A, B_chunk, result_queue):
    """Function to perform matrix multiplication for a chunk of B and put result into queue."""
    C_chunk = np.dot(A, B_chunk)
    result_queue.put(C_chunk)

def parallel_matrix_multiply(A, B, num_processes):
    """Function to parallelize matrix multiplication using multiprocessing."""
    start_time = time.time()

    # Split matrix B into chunks along columns
    chunk_size = B.shape[1] // num_processes
    B_chunks = []
    for i in range(num_processes):
        start_col = i * chunk_size
        end_col = start_col + chunk_size if i < num_processes - 1 else B.shape[1]
        B_chunk = B[:, start_col:end_col]
        B_chunks.append(B_chunk)

    # Create a queue to collect results
    result_queue = multiprocessing.Queue()

    # Create processes for matrix multiplication
    processes = []
    for B_chunk in B_chunks:
        process = multiprocessing.Process(target=matrix_multiply_chunk, args=(A, B_chunk, result_queue))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    # Collect results from the queue and concatenate them to form matrix C
    C_chunks = []
    while not result_queue.empty():
        C_chunks.append(result_queue.get())
    C = np.concatenate(C_chunks, axis=1)

    end_time = time.time()
    print(f"Matrix multiplication completed in {end_time - start_time} seconds.")
    return C

if __name__ == '__main__':
    # Example matrices A and B (replace with your matrices)
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    B = np.array([[7, 8],
                  [9, 10],
                  [11, 12]])

    num_processes = 2  # Number of processes to use

    # Perform matrix multiplication in parallel
    C = parallel_matrix_multiply(A, B, num_processes)
    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)
    print("Resultant Matrix C:")
    print(C)
