import pandas as pd
import numpy as np
import glob
import os

#<<<<<<< HEAD
#############  Overall Function  ##################

def train_plt_ref(train_folder, train_string, train_keys, test_folder, test_string, test_keys):
	"""imports test and train plant data and creates data frames with filtered data
	
	Input:
    train_folder = folder containing raw data.
    train_string = prefix of the csv files to be imported.
    train_keys = file name from current directory containing the keys spreadsheet
    test_folder = folder containing raw data.
    test_string = prefix of the csv files to be imported.
    test_keys = file name from current directory containing the keys spreadsheet

    Output:
    bas1_train = dataframe containing filtered training plant data
    bas1_test = dataframe containing filtered test plant data"""
	print('Filtering Training Set')
	df, key = data_import(train_folder, train_string, train_keys)
	bas = data_BAS(df, key)
	bas1_train = alarm_filter(bas, key)

	print('Filtering Test Set')
	df, key = data_import(test_folder, test_string, test_keys)
	bas = data_BAS(df, key)
	bas1 = alarm_filter(bas, key)

	vals_test = [x for x in bas1.columns if x in bas1_train.columns]
	bas1_test = bas1[vals_test]

	return bas1_train, bas1_test

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
	print('Filtered data contains '+str(bas.dropna().shape[0])+' points and '+str(bas.dropna().shape[1])+ ' dimensions.')
	return bas.dropna()


def alarm_filter(bas, key):
	"""removes any datapoints with alarms going off or without optimum control

	bas = dataframe containing plant data
    key = dataframe containing descriptor key"""

    #filters kes to select those with alarm units that are also BAS	
	key_alarm = key[key['Units'].str.contains("Normal/Alarm")==True]
	vals = [x for x in key_alarm if x in bas.columns]

	for alm in vals:
		bas = bas[bas[alm] == 0]

	bas = bas[bas['OptimumControl'] == 1]

	return bas

