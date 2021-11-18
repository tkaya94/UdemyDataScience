import numpy as np
np.random.seed(0)
import pandas as pd


def highlight_nan(data: pd.DataFrame, color: str) -> pd.DataFrame:
    attr = f'background-color: {color}'
    is_nan = pd.isna(data)
    return pd.DataFrame(
        np.where(is_nan, attr, ''),
        index=data.index,
        columns=data.columns
    )


def df_info(df: pd.DataFrame) -> None:
    return df.style.apply(
        highlight_nan,
        color='darkorange',
        axis=None
    )


if __name__ == '__main__':
    data = np.array([1, np.nan, 3, 4])
    print("Sum of data is", np.nansum(data))

    df = pd.DataFrame(np.random.randn(5, 3), index=["a", "b", "c", "f", "h"], columns=["one", "two", "three"])
    df["one"]["a"] = None
    df["two"]["f"] = None
    print(pd.isna(df))
    print("\nCleared df:\n", df.dropna(axis="rows"))
    print("Sum of column two in df is", df["two"].sum())


    num_samples = 100
    index = pd.date_range("21/4/2021", periods=num_samples)
    values = 2 * np.sort(np.random.randn(num_samples)) + 1
    df = pd.DataFrame(values, index)
    df.iloc[2] = None
    df.iloc[6] = None
    df.plot