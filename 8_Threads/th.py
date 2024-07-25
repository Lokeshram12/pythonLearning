import threading

def sum_part(numbers, start, end, result_lock, result):
    partial_sum = sum(numbers[start:end])
    with result_lock:
        result[0] += partial_sum

def calculate_sum_with_threads(numbers, num_threads=4):
    # Initialize variables
    result = [0]
    result_lock = threading.Lock()
    threads = []

    # Calculate chunk size for each thread
    chunk_size = len(numbers) // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else len(numbers)
        thread = threading.Thread(target=sum_part, args=(numbers, start, end, result_lock, result))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return result[0]

if __name__ == "__main__":
    # Example usage:
    numbers = list(range(1, 1000001))  # Example: Large list of numbers from 1 to 1,000,000
    sum_result = calculate_sum_with_threads(numbers, num_threads=4)
    print(f"Sum of the numbers: {sum_result}")


import requests
def fetch_url(url):
    try:
        response = requests.get(url)
        print(f"URL: {url} | Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"URL: {url} | Exception: {e}")

def fetch_urls_with_threads(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
if __name__ == "__main__":
    urls = [
        "https://www.example.com",
        "https://www.google.com",
        "https://www.nonexistenturl.com"  
    ]
    fetch_urls_with_threads(urls)
    
