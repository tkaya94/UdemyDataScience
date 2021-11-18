import numpy as np
np.random.seed(0)
import pandas as pd


def series_info(series: pd.Series) -> None:
    print(f"ndim: {series.ndim}")
    print(f"shape: {series.shape}")
    print(f"size: {series.size}")
    print(f"dtype: {series.dtype}")
    print(f"values:\n{series}\n")


def df_info(df: pd.DataFrame) -> None:
    print(f"ndim: {df.ndim}")
    print(f"shape: {df.shape}")
    print(f"size: {df.size}")
    print(f"dtype: {df.dtypes}")
    print(f"values:\n{df}\n")

if __name__ == '__main__':
    data = pd.Series(data=[.25, .5, .75, 1.0], dtype=np.float32)
    series_info(data)

    print(data.values)
    print(data.index)

    slice_data = data[1:3]
    print(slice_data[1])

    colors_dict = {"Red": 12, "Green": 8, "Blue": 33}
    colors_s = pd.Series(colors_dict, dtype=np.int8)
    series_info(colors_s)

    print("======")

    codes_dict = {"Red": "#FF0000", "Green": "#00FF00", "Blue": "#0000FF"}
    codes_c = pd.Series(codes_dict, dtype="string")

    combined_df = pd.DataFrame({"count": colors_s, "code": codes_c})
    df_info(combined_df)
    print(combined_df.index)
    print(combined_df.columns)

    