# ベースとなる Docker イメージを選択
FROM python:3.9

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# ワークディレクトリを設定
WORKDIR /app

# requirements.txtをコンテナにコピー
COPY requirements.txt ./

# Pythonライブラリのインストール
RUN pip install --no-cache-dir -r requirements.txt

# Python スクリプトをコンテナにコピー
COPY ramdom_dot.py /app/

