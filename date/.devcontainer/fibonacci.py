import time
import csv

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def measure_time_and_compute_fibonacci(n):
    elapsed_time = 0
    result = 0

    # Fibonacci number calculation is done three times
    for _ in range(3):
        start_time = time.time()
        result = fibonacci(n)
        end_time = time.time()
        elapsed_time = end_time - start_time

    print(f"Fibonacci number for n = {n} is {result}")
    print(f"Time taken to compute: {elapsed_time} seconds")

    return n, result, elapsed_time

with open('fibonacci_output.csv', 'a', newline='') as file:
    writer = csv.writer(file)

    if file.tell() == 0:
        writer.writerow(["CPU Info", "Memory Info", "N", "Elapsed Time", "Fibonacci"])

    cpu_info = 1
    memory_info = 0.1

    for n in range(20, 37):
        n, fib, elapsed = measure_time_and_compute_fibonacci(n)
        writer.writerow([cpu_info, memory_info, n, elapsed, fib])
