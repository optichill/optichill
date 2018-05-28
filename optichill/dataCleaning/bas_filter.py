import pandas as pd
import numpy as np
import glob
import os


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

	#converts pandas series to a list for future use
	val = key_bas.values.T.tolist()

    #removes DataPointNames that containt the prefix CHWV
	vals = [x for x in val if not x.startswith('CHWV')]

    #tests whether all values from the point list spreadsheet are column headings of the dataset
	for x in vals:
		if x not in df.columns:
            #prints and removes any string not found in the data
			print(x)
			vals.remove(x)
        
    #expresses data using columns specified by the vals list
	bas = df[vals+['OptimumControl', 'kW/Ton']]
    
	print('Original data contains '+str(df.shape[0])+' points and '+str(df.shape[1])+ ' dimensions.')
	print('Filtered data contains '+str(bas.dropna().shape[0])+' points and '+str(bas.dropna().shape[1])+ ' dimensions.')
	return bas.dropna()


def alarm_filter(bas, key):
	"""removes any datapoints with alarms going off or without optimum control

	bas = dataframe containing plant data
    key = dataframe containing descriptor key"""

    #filters kes to select those with alarm units that are also BAS	
	key_alarm = key[key['Units'].str.contains("Normal/Alarm")==True]
	key_alarm_BAS = key_alarm.loc[key['PointType'].str.contains("BAS")==True, 'DataPointName']

	for alm in key_alarm_BAS:
		bas = bas[bas[alm] == 0]

	bas = bas[bas['OptimumControl'] == 1]

	return bas