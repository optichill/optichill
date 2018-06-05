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
from dataCleaning import bas_filter


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
    if feat=yes
    	feature_importance_list
	return r2_score


def feature_importance_list():
	"""
	This function takes the trained model and returns an ordered list of the
	relative importance of the features. There is an option to write to an Excel
	file that the user will specify.
	"""
	return
