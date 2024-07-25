import psutil
import time

def monitor_memory(interval_seconds=1, duration_seconds=10):
    print(f"Monitoring memory usage every {interval_seconds} seconds for {duration_seconds} seconds...")
    start_time = time.time()
    end_time = start_time + duration_seconds
    
    while time.time() < end_time:
        # Get current memory usage
        memory_usage = psutil.virtual_memory().used
        
        # Convert memory usage to MB for readability
        memory_usage_mb = memory_usage / (1024 * 1024)
        
        # Print memory usage to console
        print(f"Memory Usage: {memory_usage_mb:.2f} MB")
        
        # Wait for the specified interval before checking again
        time.sleep(interval_seconds)

# Example usage: Monitor memory for 30 seconds with an interval of 2 seconds
monitor_memory(interval_seconds=2, duration_seconds=30)

