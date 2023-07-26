import time

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

if __name__ == "__main__":
    for n in [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]:  # 計算したいフィボナッチ数列の項をリストで指定
        start_time = time.time()

        result = fibonacci_recursive(n)

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"フィボナッチ数列の第{n}項の計算にかかった時間: {elapsed_time}秒")
        print(f"フィボナッチ数列の第{n}項: {result}")
