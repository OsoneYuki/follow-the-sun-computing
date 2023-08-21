import pandas as pd
import numpy as np
import math as ma
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import time as time_module
import os


# 例: 5000行から10000行までのデータで100行ごとにループを回す
for num_rows in range(100, 17600, 100):

    #スタート
    print("\n\n---電力価格予測プログラム開始---\n\n")
    
    start_time = time_module.time()

    # データの読み込み
    # 学習データ
    input_data = pd.read_csv("input_data2022.csv").head(num_rows)
    # テストデータ
    pv_predict = pd.read_csv("pv_predict.csv")
    # テストデータ(出力ファイルに値を格納するために値を処理することなく保存するため)
    pv_predict_ = pd.read_csv("pv_predict.csv")

    # 使用するパラメータ
    parameters = ['temperature', 'total precipitation', 'u-component of wind', 'v-component of wind',
                'radiation flux', 'pressure', 'relative humidity', 'hourSin', 'hourCos', 'PVout']        
    predict_parameters = ['price', 'imbalance']

    # データの前処理
    scaler = MinMaxScaler()
    input_data[parameters] = scaler.fit_transform(input_data[parameters])
    pv_predict[parameters] = scaler.transform(pv_predict[parameters])

    # 学習データとターゲットデータの作成
    X = input_data[parameters].values
    y = input_data[predict_parameters].values

    # モデルの定義
    hidden_units = [64, 64, 64]  # 隠れ層のユニット数
    epochs = 100  # エポック数

    model = keras.Sequential()
    model.add(keras.layers.Dense(hidden_units[0], activation='relu', input_shape=(len(parameters),)))
    for units in hidden_units[1:]:
        model.add(keras.layers.Dense(units, activation='relu'))
    model.add(keras.layers.Dense(len(predict_parameters)))

    # モデルのコンパイル
    model.compile(optimizer='adam', loss='mse')

    # モデルの学習
    model.fit(X, y, epochs=epochs, verbose=0)

    # 予測の実行
    predictions = model.predict(pv_predict[parameters].values)

    # 予測結果の保存
    pred_df = pd.DataFrame(columns=["year","month","day","hour","hourSin","hourCos","upper","lower","PVout","price","imbalance"])
    pred_df[["price","imbalance"]] = predictions

    pred_df[["year","month","hour","day","hourSin","hourCos"]] = pv_predict[["year","month","hour","day","hourSin","hourCos"]]
    pred_df[["upper","lower","PVout"]] = pv_predict_[["upper","lower","PVout"]]
    pred_df.to_csv("price_predict.csv", index=False)

    
    # 終了
    end_time = time_module.time()
    real_execution_time = end_time - start_time
    print(f"実行時間: {real_execution_time:.2f} 秒")

    #終了
    print("\n\n---電力価格予測プログラム終了---")

    
    # データフレームの初期化
    df = pd.DataFrame(columns=["number_of_data", "real_execution_time"])

    # 結果をデータフレームに保存
    # 実行が終わったら、そのデータの行数をCSVに記録します
    real_execution_df = pd.DataFrame({
        "number_of_data": len(input_data),
        "real_execution_time": [real_execution_time]
    })

    df = pd.concat([df, real_execution_df])

    # データフレームをCSVファイルに書き込む
    filename = "real_execution_time.csv"
    write_header = not os.path.exists(filename)
    df.to_csv(filename, mode='a', index=False, header=write_header)

    print("CSVファイルに記録されました。") 