import datetime
import numpy as np
np.random.seed(0)
import pandas as pd
from PandasIntro import series_info, df_info

ds = pd.date_range("21/4/2021", periods=3, freq="H")
series_info(ds)

friday = pd.Timestamp("2018-01-05 12:00:00").tz_localize("Europe/Berlin")
print(friday)
saturday = friday + pd.Timedelta("1 Day")
print(saturday)
