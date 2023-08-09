import pandas as pd

# CSVファイルの読み込み
filename = "result.csv"
df = pd.read_csv(filename)

# cpu_infoとmemory_infoの列を8に変更
df['cpu_info'] = 8
df['memory_info'] = 8

# 変更をCSVファイルに書き戻す
df.to_csv(filename, index=False)
