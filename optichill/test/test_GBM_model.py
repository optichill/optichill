import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score
import pickle
from optichill import bas_filter
from optichill import GBM_model


def test_train_model():
    """
    This functions tests the train_model function.
    """
    dat_folder = '../../data'
    list_train = ['Plt1 h 2017-05.csv']
    list_test = ['Plt1 h 2017-11.csv']
    keys = 'data/Plt1 Points List.xlsx'
    df_train, df_test = bas_filter.train_single_plt(
        dat_folder, list_train, list_test,
        keys, include_alarms=False
    )
    ytrain = df_train['kW/Ton']
    ytest = df_test['kW/Ton']
    xtrain = df_train.drop(['kW/Ton'], axis=1)
    xtest = df_test.drop(['kW/Ton'], axis=1)
    test_score = GBM_model.train_model(xtrain, ytrain, xtest, ytest)
    # Assertion to ensure the test score is being returned as a number
    assert isinstance(test_score, float), (
        'Calculation of the test score is incorrect.'
    )
    try:
        GBM_model.train_model(
            xtrain, ytrain, xtest, ytest, feat_filename=csv_file
        )
    except(AssertionError):
        pass
    else:
        raise Exception('Assertion Error not raised. Fix it.')
    return


def test_predict_model():
    """
    This function tests the predict_model function.
    """
    return


def test_feature_importance_list():
    """
    This function tests the feature_imortantce_list function.
    """
    return
