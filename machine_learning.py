import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ダミーデータの生成（実際のデータに置き換える）
# CPUの性能、メモリ容量、コードの行数を特徴量として、処理時間をターゲットとする
cpu_performance = np.random.rand(100, 1)  # 100個のCPU性能のランダムなデータ
memory_capacity = np.random.rand(100, 1)   # 100個のメモリ容量のランダムなデータ
code_lines = np.random.rand(100, 1)       # 100個のコード行数のランダムなデータ
processing_time = 5 * cpu_performance + 3 * memory_capacity + 2 * code_lines + np.random.randn(100, 1)

# 特徴量を結合
X = np.hstack((cpu_performance, memory_capacity, code_lines))

# 学習データと検証データに分割
X_train, X_val, y_train, y_val = train_test_split(X, processing_time, test_size=0.2, random_state=42)

# モデルの構築と学習
model = LinearRegression()
model.fit(X_train, y_train)

# モデルの評価
y_pred = model.predict(X_val)
mse = mean_squared_error(y_val, y_pred)
r2 = r2_score(y_val, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# 新しいデータに対して処理時間を推定
new_data = np.array([[0.8, 0.6, 200]])  # 例として新しいデータを用意
predicted_time = model.predict(new_data)
print(f"Predicted Processing Time: {predicted_time[0][0]}")
