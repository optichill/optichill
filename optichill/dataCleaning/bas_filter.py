import pandas as pd
import numpy as np
import glob
import os

#<<<<<<< HEAD
#############  Overall Function  ##################

def train_single_plt(folder, train_filenames, test_filenames, keys, include_alarms=True):
	"""imports test and train plant data and creates data frames with filtered data
	
	Input:
	folder = path to location of raw data files
    train_filenames = list of filenames to be used as the training set.
    test_filenames = list of filenames to be used as the testing set.
    keys = file name from current directory containing the keys spreadsheet
    include_alarms = include or remove alarms from dataset (default = True)

    Output:
    df_bas1_train = dataframe containing filtered training data
    df_ce bas1_test = dataframe containing filtered testS data"""
	print('Filtering Training Set')

	df = pd.DataFrame()

	for train_string in train_filenames:

		dfloop, key = data_import(folder, train_string, keys)
		df = pd.concat([df, dfloop], ignore_index=True)

	bas = data_BAS(df, key)
	if include_alarms == False:
		bas1_train = alarm_filter(bas, key)
	else:
		bas1_train = bas

	print('Filtering Test Set')
	df = pd.DataFrame()

	for test_string in test_filenames:

		dfloop, key = data_import(folder, test_string, keys)
		df = pd.concat([df, dfloop], ignore_index=True)

	bas = data_BAS(df, key)
	if include_alarms == False:
		bas1 = alarm_filter(bas, key)
	else:
		bas1 = bas

	vals_test = [x for x in bas1.columns if x in bas1_train.columns]
	df_bas1_test = bas1[vals_test]
	df_bas1_train = bas1_train[vals_test]

	return df_bas1_train, df_bas1_test

def train_plt_ref(train_folder, train_string, train_keys, test_folder, test_string, test_keys, include_alarms=True):
	"""imports test and train plant data and creates data frames with filtered data
	
	Input:
    train_folder = folder containing raw data.
    train_string = prefix of the csv files to be imported.
    train_keys = file name from current directory containing the keys spreadsheet
    test_folder = folder containing raw data.
    test_string = prefix of the csv files to be imported.
    test_keys = file name from current directory containing the keys spreadsheet
    include_alarms = include or remove alarms from dataset (default = True)

    Output:
    df_bas1_train = dataframe containing filtered training plant data
    df_ce bas1_test = dataframe containing filtered test plant data"""
	print('Filtering Training Set')
	df, key = data_import(train_folder, train_string, train_keys)
	bas = data_BAS(df, key)
	if include_alarm == False:
		bas1_train = alarm_filter(bas, key)
	else:
		bas1_train = bas

	print('Filtering Test Set')
	df, key = data_import(test_folder, test_string, test_keys)
	bas = data_BAS(df, key)
	if include_alarm == False:
		bas1 = alarm_filter(bas, key)
	else:
		bas1 = bas

	vals_test = [x for x in bas1.columns if x in bas1_train.columns]
	df_bas1_test = bas1[vals_test]
	df_bas1_train = bas1_train[vals_test]

	return df_bas1_train, df_bas1_test

############  Sub Components  #####################

def import_and_filter(dat_folder, string, keys):
	"""imports plant data and creates data frames with filtered data and keys
	
	Input:
    dat_folder = folder containing raw data.
    string = prefix of the csv files to be imported.
    keys = file name from current directory containing the keys spreadsheet

    Output:
    bas1 = dataframe containing filtered plant data
    key = dataframe containing descriptor key"""

	df, key = data_import(dat_folder, string, keys)
	bas = data_BAS(df, key)
	bas1 = alarm_filter(bas, key)
	return bas1, key
#=======
#>>>>>>> 94153ebb45dbed36823b404b6571e0385755acc3

def data_import(dat_folder, string, keys):
    """imports plant data and creates data frames with raw data and keys

    dat_folder = folder containing raw data.
    string = prefix of the csv files to be imported.
    keys = file name from current directory containing the keys spreadsheet

    Output:
    df = dataframe containing plant data
    key = dataframe containing descriptor key"""

    # Assert that dat_folder is .csv

    # Assert that string is string type

    #extracts file names
    dat_list = [f for f in glob.glob(os.path.join(dat_folder, string + '*'))]
    print(dat_list)
    
    #reads and appends content from file to a data frame
    df = pd.DataFrame()

    for lst in dat_list:
        df_add = pd.read_csv(lst)
        df = pd.concat([df, df_add], ignore_index=True)
    
    key = pd.read_excel(keys)
    
    return df, key


def import_and_filter(dat_folder, string, keys):
	"""imports plant data and creates data frames with filtered data and keys
	
	Input:
    dat_folder = folder containing raw data.
    string = prefix of the csv files to be imported.
    keys = file name from current directory containing the keys spreadsheet

    Output:
    bas1 = dataframe containing filtered plant data
    key = dataframe containing descriptor key"""

	df, key = data_import(dat_folder, string, keys)
	bas = data_BAS(df, key)
	bas1 = alarm_filter(bas, key)
	return bas1, key



def data_BAS(df, key):
	'''Filters out non-BAS descriptors and data containing NaN values

	df = dataframe containing plant data
	key = dataframe containing descriptor key'''
	key_bas = key.loc[key['PointType'].str.contains("BAS")==True,'DataPointName']
	key_chiller = key.loc[key['PointType'].str.contains("Chiller")==True,'DataPointName']
	key_condenser = key.loc[key['PointType'].str.contains("Condenser Water Pump")==True,'DataPointName']
	key_cool = key.loc[key['PointType'].str.contains("Cooling Tower Cell")==True,'DataPointName']
	
	key = pd.concat([key_bas, key_condenser, key_cool, key_chiller], ignore_index = True)
	#print(key.head())
	#converts pandas series to a list for future use
	val = key.values.T.tolist()

    #removes DataPointNames that containt the prefix CHWV
	kw = [x for x in val if not 'kW' in x]
	vals = [x for x in kw if not x.startswith('CHWV')]

    #tests whether all values from the point list spreadsheet are column headings of the dataset
	print('Descriptors in the points list that are not in the datasets.')
	for x in vals:
		if x not in df.columns:
            #prints and removes any string not found in the data
			print(x)
			vals.remove(x)
        #tests whether all values from the point list spreadsheet are column headings of the dataset

	vals_new = [x for x in vals if x in df.columns]
	#vals_kw = [x for x in vals_new if not x]
	#print(vals_new)
	
	#for x in df.columns:
		#if x not in vals:
            #prints and removes any string not found in the data
			#print(x)
    #expresses data using columns specified by the vals list
	bas = df[vals_new+['OptimumControl', 'kW/Ton']]
    
	print('Original data contains '+str(df.shape[0])+' points and '+str(df.shape[1])+ ' dimensions.')
	
	return bas.dropna()


def alarm_filter(bas, key):
	"""removes any datapoints with alarms going off or without optimum control

	bas = dataframe containing plant data
    key = dataframe containing descriptor key"""

    #filters kes to select those with alarm units that are also BAS	
	key_alarm = key.loc[key['Units'].str.contains("Normal/Alarm")==True, 'DataPointName']

	vals = [x for x in key_alarm if x in bas.columns]
	#print(vals)
	for alm in vals:
		bas_start = bas.shape[0]
		bas = bas[bas[alm] == 0]

		bas_end = bas.shape[0]
		if bas_end != bas_start:
			print('A '+alm+' was noted and '+str(bas_start-bas_end)+' datapoints were removed from the dataset.')

	bas = bas[bas['OptimumControl'] == 1]

	vals_rm = [x for x in bas.columns if not x in vals]
	bas_new = bas[vals_rm].copy()

	print('Filtered data contains '+str(bas_new.dropna().shape[0])+' points and '+str(bas_new.dropna().shape[1])+ ' dimensions.')

	return bas_new

