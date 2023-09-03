import time

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes_up_to_n(n):
    for i in range(2, n + 1):
        if is_prime(i):
            print(i)

if __name__ == "__main__":
    N = 100000  # Change this value to any number you'd like
    
    start_time = time.time()
    print_primes_up_to_n(N)
    end_time = time.time()

    print(f"\nExecution time: {end_time - start_time} seconds")
