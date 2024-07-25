import random
from memory_profiler import profile

@profile
def generate_large_list(num_elements):
    large_list = []
    for i in range(num_elements):
        large_list.append(random.randint(1, 100))
    
    return large_list

if __name__ == "__main__":
    
    num_elements = 10000
    result = generate_large_list(num_elements)


