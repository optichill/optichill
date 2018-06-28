import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score
import pickle


def train_model(
    xtrain_df, ytrain_df, xtest_df, ytest_df, num_params=500, max_dp=6,
    min_samp_splt=2, lrn_rt=0.01, losss='ls', feat_filename=None
):
    """
    This function takes dataframes of the x and y values for training and testing
    and uses the scikit learn toolbox to train a Gradient Boosting Regressor model
    with preset parameters that can be specified. It returns a trained model and
    the r2 value of the trained model. There is an option to create a normalized
    list of the features to a user-named Excel file.
    """
    # Reshaping the inputs into numpy arrays for the scikit learn module.
    xtrain = xtrain_df.values
    ytrain = ytrain_df.values
    xtest = xtest_df.values
    ytest = ytest_df.values
    # Defining the parameters of GBM
    params = {
        'n_estimators': num_params, 'max_depth': max_dp, 'min_samples_split':
        min_samp_splt, 'learning_rate': lrn_rt, 'loss': losss
        }
    model = GradientBoostingRegressor(**params)
    model.fit(xtrain, ytrain)
    ypred = model.predict(xtest)
    test_score = r2_score(ytest, ypred)
    filename = 'trained_model.sav'
    pickle.dump(model, open(filename, 'wb'))
    # Feature importance list function call
    if feat_filename:
        assert isinstance(feat_filename, str)
        feature_importance_list(feat_filename, xtest_df)
        return test_score
    else:
        return test_score


def predict_model():
    """
    This function unpickles the saved model and returns it as an object.
    """
    filename = 'trained_model.sav'
    new_model = pickle.load(open(filename, 'rb'))
    return new_model


def feature_importance_list(file_name_string, xtest_df):
    """
    This function takes the trained model and returns an ordered list of the
    relative importance of the features. This will be written to an Excel
    file that the user will specify.
    """
    filename = 'trained_model.sav'
    new_model = pickle.load(open(filename, 'rb'))
    feature_importance = new_model.feature_importances_
    feature_importance = 100.0 * (feature_importance / feature_importance.max())
    sorted_idx = np.argsort(feature_importance)
    pos = np.arange(sorted_idx.shape[0]) + 0.5
    x = xtest_df.columns[sorted_idx]
    imp = feature_importance[sorted_idx]
    df_feats = pd.DataFrame({'Feature Name': x, 'Feature Importance': imp})
    df_feats.to_csv(file_name_string)
    return print("The feature importance list was created as", file_name_string)
