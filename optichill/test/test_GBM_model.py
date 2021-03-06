from optichill import bas_filter
from optichill import GBM_model
import os


def test_train_model():
    """
    This functions tests the train_model function.
    """
    dirname = os.path.dirname(__file__)
    dat_folder = os.path.join(dirname, '../../data')
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
            xtrain, ytrain, xtest, ytest, feat_filename=2
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
    This function tests the feature_importance_list function.
    """
    # Assertion that the string is a csv file
    dirname = os.path.dirname(__file__)
    dat_folder = os.path.join(dirname, '../../data')
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
    GBM_model.train_model(xtrain, ytrain, xtest, ytest)
    try:
        GBM_model.feature_importance_list(
            'files.txt', xtest
        )
    except(Exception):
        pass
    else:
        raise Exception('.csv Exception not raised. Fix it.')
    return
