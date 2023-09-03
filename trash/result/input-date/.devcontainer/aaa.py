import pandas as pd

# CSVファイルの読み込み
df = pd.read_csv('input_data2022.csv')

# ヘッダーの取得
header = df.columns

# 最初の100行のデータ部分の取得
subset_data = df.iloc[:10000]

# 新しいDataFrameの作成
new_df = pd.DataFrame(subset_data, columns=header)

# CSVファイルとして保存
new_df.to_csv('input_data2022_10000.csv', index=False)
