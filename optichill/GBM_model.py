import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import seaborn as sns
import glob
import os
from optichill import bas_filter


def train_GBM_model(
    xtrain, ytrain, xtest, ytest, num_params=450, min_samp_splt=2,
    lrn_rt=0.01, losss='ls', max_dp=6
):
    """
    This functions takes a cleaned dataset and uses the scikit learn toolbox to train
    a Gradient Boosting Regressor model with preset parameters that can	be specified.
    It returns a trained model and the r2 value of the trained model.
    Defaults: 
    """
    params = {
        'n_estimators': num_params, 'max_depth': max_dp, 'min_samples_split':
        min_samp_splt, 'learning_rate': lrn_rt, 'loss': losss
        }
    model = GradientBoostingRegressor(**params)
    model.fit(xtrain, ytrain)
    ypred = model.predict(xtest)
    test_score = r2_score(ytest, ypred)
    if feat == yes:
        feature_importance_list
    return r2_score


def feature_importance_list(file_name_string):
    """
    This function takes the trained model and returns an ordered list of the
    relative importance of the features. This will be written to an Excel
    file that the user will specify.
    """
    # feauture_importance = trained_model.feature_importances_
    # feautre_importance = 100.0 * (feature_importance / feature_importance.max())
    # sorted_idx = np.argsort(feature_importance)
    # pos = np.arange(sorted_idx.shape[0]) + 0.5
    # x = test_dataframe.drop(['target'], axis=1).columns[sorted_idx]
    # imp = feature_importance[sorted_idx]
    # df_feats = pd.DataFrame({'Feature Name': x, 'Feature Importance': imp})
    # df_feats.to_csv(file_name_string)
    return
