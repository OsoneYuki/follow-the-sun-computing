import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

# Reading data from Excel file
df = pd.read_excel("Data_PV and consumptions.xlsx")

# データの日付をインデックスとして設定
df['Data'] = pd.to_datetime(df['Data'])
df.set_index('Data', inplace=True)

# Initializing a variable to store the total future production.
total_forecast_gen = np.zeros(5)  # 5は予測するステップ数

# Forecasting for each producer
for producer in ['Producer 1 (kW)', 'Producer 2 (kW)', 'Producer 3 (kW)']:
    series = df[producer]
    
    # ARIMAモデルを適合
    model = ARIMA(series, order=(5,1,2))
    model_fit = model.fit()
    
    # 未来の5つのポイントを予測
    forecast_gen = model_fit.forecast(steps=5)
    
    # Adding the forecasted values to the total forecast generation.
    total_forecast_gen += forecast_gen  # 各プロデューサーの予測を合計

# Consumer1.xlsxから消費量を読み込み
file_path = 'Consumer1.xlsx'
df = pd.read_excel(file_path)

df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
df.set_index('Data', inplace=True)

# 消費量（Consumption [kWh]）に対してARIMAモデルを適合
series = df['Consumption [kWh]']

# ARIMAモデルを適合
model = ARIMA(series, order=(5,1,2))
model_fit = model.fit()

# 未来の5つのポイントを予測
forecast_load = model_fit.forecast(steps=5)

# 各時点での差を計算し、表示
difference = total_forecast_gen - forecast_load
print("The difference between forecasted generation and load at each point is:")
print(difference)
