import os
import glob
import numpy as np
import pandas as pd
import lightgbm as lgb

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


def cross_val(reg_base, X, y, n_folds=5, isLightGBM=False, params=None, verbose=0):
    errors = {'MAE': {'train': [], 'valid': []},
              'RMSE': {'train': [], 'valid': []}}

    for i in tqdm(range(n_folds)):
        X_train, X_valid, y_train, y_valid = train_test_split(
            X, y, test_size=1/n_folds, stratify=None, random_state=i)

        if isLightGBM == True:
            if params == None:
                return ('Error: Specify parameters for LightGBM')
            else:
                d_train = lgb.Dataset(X_train, label=y_train)
                d_valid = lgb.Dataset(X_valid, label=y_valid)
                watchlist = [d_valid]
                reg = lgb.train(params, d_train, watchlist, verbose_eval=1)

        else:
            reg = reg_base
            reg.fit(X_train, y_train)
        y_pred_train = reg.predict(X_train)
        errors['MAE']['train'].append(calculate_MAE(y_pred_train, y_train))
        errors['RMSE']['train'].append(calculate_RMSE(y_pred_train, y_train))

        y_pred_valid = reg.predict(X_valid)
        errors['MAE']['valid'].append(calculate_MAE(y_pred_valid, y_valid))
        errors['RMSE']['valid'].append(calculate_RMSE(y_pred_valid, y_valid))

        if verbose == 1:
            print('<--- Training Error ({}/{})--->'.format(i+1, n_folds))
            print(' MAE: {}'.format(round(errors['MAE']['train'][i], 5)))
            print('RMSE: {}\n'.format(round(errors['RMSE']['train'][i], 5)))

            print('<--- Validation Error ({}/{}) --->'.format(i+1, n_folds))
            print(' MAE: {}'.format(round(errors['MAE']['valid'][i], 5)))
            print('RMSE: {}\n\n'.format(round(errors['RMSE']['valid'][i], 5)))

    return errors


def summarize_errors(errors, verbose=0):
    df_mae = pd.DataFrame(errors['MAE']).T
    df_rmse = pd.DataFrame(errors['RMSE']).T

    df_mae.columns = ['' for i in df_mae.columns]
    df_rmse.columns = ['' for i in df_rmse.columns]

    df_mae.index.name = "MAE"
    df_rmse.index.name = "RMSE"

    if verbose == 1:
        display(df_mae, df_rmse)

    print('\n   <--- Validation Errors --->')
    print('MAE  | Mean: {}, SD: {}'.format(str(round(np.mean(errors['MAE']['valid']), 5)),
                                           str(round(np.std(errors['MAE']['valid']), 5))))
    print('RMSE | Mean: {}, SD: {}\n'.format(str(round(np.mean(errors['RMSE']['valid']), 5)),
                                             str(round(np.std(errors['RMSE']['valid']), 5))))
    return None
