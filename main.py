import pandas as pd

from get_historical_klines import klineData


bybit_api_key = "API_KEY_HERE"
bybit_api_secret = "API_SECRET_HERE"


symbol_list=["BTCUSDT","ETHUSDT","BANANAUSDT"]


kl = klineData(
    symbol_list=symbol_list,
    interval="1",
    extract_dates=["2024-08-14"],
    category="linear",
    num_threads=12,
    bybit_api_key = bybit_api_key,
    bybit_api_secret = bybit_api_secret
)
data = kl.run_threads()

volume_list = []
for symbol in symbol_list:
    close_col = f"Volume_{symbol}"
   

    volume_list.append({"symbol":symbol,"volume":data[close_col].astype(float).sum()})


pd.DataFrame(volume_list).sort_values(by="volume")



