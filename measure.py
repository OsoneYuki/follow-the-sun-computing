import psutil
import subprocess
import time

def measure_cpu_usage(pid, duration):
    process = psutil.Process(pid)
    cpu_percent_list = []
    start_time = time.time()

    while time.time() - start_time < duration:
        cpu_percent = process.cpu_percent(interval=0.1)
        cpu_percent_list.append(cpu_percent)

    return cpu_percent_list

def measure_memory_usage(pid, duration):
    process = psutil.Process(pid)
    memory_usage_list = []
    start_time = time.time()

    while time.time() - start_time < duration:
        memory_info = process.memory_info()
        memory_usage = memory_info.rss / (1024 * 1024)  # バイトをメガバイトに変換
        memory_usage_list.append(memory_usage)

    return memory_usage_list

# 実行するプログラムのパスと引数を指定
program_path = 'primenumbers.py'
program_args = ['arg1', 'arg2']

# プログラムを非同期で実行
process = subprocess.Popen(['python', program_path] + program_args)

# プログラムのPIDを取得
pid = process.pid

# CPU使用率とメモリ使用量を測定する時間（秒）
measurement_duration = 10

# CPU使用率を測定
cpu_usage_list = measure_cpu_usage(pid, measurement_duration)

# メモリ使用量を測定
memory_usage_list = measure_memory_usage(pid, measurement_duration)

# 測定結果を表示
print(f'CPU使用率: {cpu_usage_list}')
print(f'メモリ使用量: {memory_usage_list} MB')

# プログラムの終了を待機
process.wait()
