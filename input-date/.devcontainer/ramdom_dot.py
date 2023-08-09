import numpy as np
import time
import pandas as pd
import os

# CPUとメモリ情報
cpu_info = 4
memory_info = 2.5

# データフレームの初期化
df = pd.DataFrame(columns=["cpu_info", "memory_info", "size", "elapsed_time"])

# size=1000～10000まで1000間隔で行列の計算を行う
for size in range(100, 10000, 100):  # 0ではなく100から開始

    # 大規模な行列の生成
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    # 処理時間の計測開始
    start_time = time.time()

    # 行列の掛け算
    C = np.dot(A, B)

    # 処理時間の計測終了
    elapsed_time = time.time() - start_time

    # 結果の表示
    print(f"Size: {size}, The first element of the result matrix is: {C[0, 0]}")
    print("Elapsed time: ", elapsed_time)

    # 結果をデータフレームに保存
    result_df = pd.DataFrame({
        "cpu_info": [cpu_info], 
        "memory_info": [memory_info], 
        "size": [size], 
        "elapsed_time": [elapsed_time]
    })

    df = pd.concat([df, result_df])

# データフレームをCSVファイルに書き込む
filename = "result.csv"
write_header = not os.path.exists(filename)
df.to_csv(filename, mode='a', index=False, header=write_header)
