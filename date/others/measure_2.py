import psutil
import threading
import time

def measure_cpu_usage(duration):
    cpu_percent_list = []
    start_time = time.time()

    while time.time() - start_time < duration:
        cpu_percent = psutil.cpu_percent(interval=0.1)
        cpu_percent_list.append(cpu_percent)

    return cpu_percent_list

def measure_memory_usage(duration):
    memory_usage_list = []
    start_time = time.time()

    while time.time() - start_time < duration:
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.used / (1024 * 1024)  # バイトをメガバイトに変換
        memory_usage_list.append(memory_usage)
        time.sleep(0.1)

    return memory_usage_list

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
measurement_duration = 10

# マルチスレッドでCPU使用率とメモリ使用量を測定
cpu_result = []
memory_result = []

cpu_thread = threading.Thread(target=lambda: cpu_result.extend(measure_cpu_usage(measurement_duration)))
memory_thread = threading.Thread(target=lambda: memory_result.extend(measure_memory_usage(measurement_duration)))

cpu_thread.start()
memory_thread.start()

# 素数の計算
for num in range(1, 10000):
    if is_prime(num):
        primes.append(num)

cpu_thread.join()
memory_thread.join()

# 結果を表示
print(f'CPU使用率: {cpu_result}')
print(f'メモリ使用量: {memory_result} MB')
print(primes)