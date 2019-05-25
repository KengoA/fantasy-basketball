import glob
import pandas as pd
from tqdm import tqdm_notebook as tqdm

# Concatenate all csv files under a directory


def csv_concatenate(folder_path, nested=False):
    if nested == True:
        files = glob.glob(folder_path + "/*/*.csv")
    else:
        files = glob.glob(folder_path + "/*.csv")

    df_list = []

    for file in tqdm(files):
        df_list.append(pd.read_csv(file, parse_dates=True,
                                   infer_datetime_format=True))

    # Fill nan with 0s as some values are empty for percentage points
    df = pd.concat(df_list).fillna(0).reset_index(drop=True)

    return df
