import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# ダミーデータの生成（実際のデータに置き換える）
cpu_performance = np.random.rand(100, 1)  # 100個のCPU性能のランダムなデータ
memory_capacity = np.random.rand(100, 1)   # 100個のメモリ容量のランダムなデータ
code_lines = np.random.rand(100, 1)       # 100個のコード行数のランダムなデータ
processing_time = 5 * cpu_performance + 3 * memory_capacity + 2 * code_lines + np.random.randn(100, 1)

# 特徴量を結合
X = np.hstack((cpu_performance, memory_capacity, code_lines))

# PyTorchテンソルに変換
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(processing_time, dtype=torch.float32)

# 学習データと検証データに分割
X_train, X_val, y_train, y_val = train_test_split(X_tensor, y_tensor, test_size=0.2, random_state=42)

# ニューラルネットワークモデルの定義
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(3, 10)  # 入力層から隠れ層への結合
        self.fc2 = nn.Linear(10, 1)  # 隠れ層から出力層への結合

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # 隠れ層の活性化関数としてReLUを使用
        x = self.fc2(x)             # 出力層の線形結合
        return x

# モデルの初期化
model = Net()

# 損失関数と最適化アルゴリズムの設定
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# モデルの学習
epochs = 1000
for epoch in range(epochs):
    # 順伝播
    outputs = model(X_train)
    loss = criterion(outputs, y_train)

    # 逆伝播とパラメータの更新
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item()}")

# モデルの評価
with torch.no_grad():
    y_pred_val = model(X_val)
    mse = mean_squared_error(y_val, y_pred_val.numpy())
    print(f"Mean Squared Error on Validation Set: {mse}")

# 新しいデータに対して処理時間を推定
new_data = torch.tensor([[0.8, 0.6, 200]], dtype=torch.float32)
predicted_time = model(new_data)
print(f"Predicted Processing Time: {predicted_time.item()}")
