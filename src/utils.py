import os
import glob
import numpy as np
import pandas as pd

from tqdm import tqdm_notebook as tqdm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from constants import DATA_DIR


def csv_concatenate(folder_path, nested=False):
    # Concatenate all csv files under a directory
    if nested == True:
        files = glob.glob(folder_path + "/*/*.csv")
    else:
        files = glob.glob(folder_path + "/*.csv")

    df_list = []

    for file in files:
        df_list.append(pd.read_csv(file, parse_dates=True,
                                   infer_datetime_format=True))

    # Fill nan with 0s as some values are empty for percentage points
    df = pd.concat(df_list).fillna(0).reset_index(drop=True)

    return df


def calculate_FPTS(df):
    # Scoring rules based on https://www.draftkings.co.uk/help/rules/4
    multipliers = {'PTS': 1, '3P': 0.5, 'TRB': 1.25,
                   'AST': 1.5, 'STL': 2, 'BLK': 2, 'TOV': -0.5}

    indices = len(df)
    fpts_list = []

    for i in tqdm(range(indices)):
        fpts = 0
        doubles = 0
        for stat, multiplier in multipliers.items():
            if stat in ['PTS', 'TRB', 'AST', 'STL', 'BLK']:
                if df.loc[i, stat] >= 10:
                    doubles += 1
            fpts += df.loc[i, stat]*multiplier
        if doubles >= 2:
            fpts += 1.5
        if doubles >= 3:
            fpts += 3
        fpts_list.append(fpts)

    return fpts_list


def calculate_MAE(pred, true):
    n = len(pred)
    abs_error = 0
    for i in range(n):
        abs_error += abs(pred[i] - true[i])
    mae = abs_error/n
    return mae


def calculate_RMSE(pred, true):
    return np.sqrt(mean_squared_error(pred, true))


def load_full_dataset(weighting='quad'):
    df_features = csv_concatenate(os.path.join(
        DATA_DIR, 'Dataframes', 'Modelling', 'Features', weighting))

    X = df_features.loc[:, df_features.columns[5:]]
    X = MinMaxScaler().fit_transform(X)
    y = df_features['FPTS'].values.reshape(-1, 1).flatten()
    return X, y


def cross_val(reg_base, X, y, nfolds=5, verbose=1):
    mae_results_train, rmse_results_train = [], []
    mae_results_valid, rmse_results_valid = [], []

    for i in tqdm(range(nfolds)):
        X_train, X_valid, y_train, y_valid = train_test_split(
            X, y, test_size=1/nfolds, stratify=None, random_state=i)

        reg = reg_base
        reg.fit(X_train, y_train)

        y_pred_train = reg.predict(X_train)
        mae_results_train.append(calculate_MAE(y_pred_train, y_train))
        rmse_results_train.append(calculate_RMSE(y_pred_train, y_train))

        y_pred_valid = reg.predict(X_valid)
        mae_results_valid.append(calculate_MAE(y_pred_valid, y_valid))
        rmse_results_valid.append(calculate_RMSE(y_pred_valid, y_valid))

    if verbose == 1:
        print('[Training Eror]')
        print(' MAE | Mean: {}, SD: {}'.format(round(np.mean(mae_results_train), 5),
                                               round(np.std(mae_results_train), 5)))
        print('RMSE | Mean: {}, SD: {}\n'.format(round(np.mean(rmse_results_train), 5),
                                                 round(np.std(rmse_results_train), 5)))

    print('[Validation Error]')
    print(' MAE | Mean: {}, SD: {}'.format(round(np.mean(mae_results_valid), 5),
                                           round(np.std(mae_results_valid), 5)))
    print('RMSE | Mean: {}, SD: {}'.format(round(np.mean(rmse_results_valid), 5),
                                           round(np.std(rmse_results_valid), 5)))

    return None
