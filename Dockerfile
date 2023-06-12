# ベースイメージを指定
FROM python:3.9

# ワーキングディレクトリを設定
WORKDIR /app

# ソースコードをコンテナ内の/appディレクトリにコピー
COPY primenumbers.py /app/primenumbers.py
COPY measure.py /app/measure.py
COPY block_count.py /app/block_count.py


# 必要なパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# コンテナ起動時に実行するコマンドを指定
CMD ["python", "/app/measure.py"]
