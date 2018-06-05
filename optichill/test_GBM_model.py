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
from optichill import GBM_model


def test_train_GBM_model():
	"""
	This function is the unit test for the train_GBM_model in the optichill module.
	"""
	GBM_model.train_GBM_model()
	return


def test_feature_importance_list():
	"""
	This function is the unit test for the feature_importance_list function from
	the optichill module.
	"""
	GBM_model.feature_importance_list()
	return
