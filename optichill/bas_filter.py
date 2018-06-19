import pandas as pd
import numpy as np
import glob
import os

#  Overall Function  #


def train_single_plt(
    folder, train_filenames, test_filenames,
    keys, include_alarms=True, dim_remove=[], time_list=[]
):
    """imports test and train plant data and creates data frames
    with filtered data
    Input:
    folder = path to location of raw data files
    train_filenames = list of filenames to be used as the training set.
    test_filenames = list of filenames to be used as the testing set.
    keys = file name from current directory containing the keys spreadsheet
    include_alarms = include or remove alarms from dataset (default = True)
    dim_remove = list of descriptors to remove from dataset (default = NULL)

    Output:
    df_bas1_train = dataframe containing filtered training data
    df_bas1_test = dataframe containing filtered testS data"""

    print('Filtering Training Set')

    bas1_train = import_and_filter(
        folder, train_filenames, keys, include_alarms=include_alarms,
        dim_remove=dim_remove, time_list=time_list
    )

    print('Filtering Test Set')

    bas1_test = import_and_filter(
        folder, test_filenames, keys, include_alarms=include_alarms,
        dim_remove=dim_remove, time_list=time_list
    )

    # matches training and testing columns
    vals_test = [x for x in bas1_test.columns if x in bas1_train.columns]
    df_bas1_test = bas1_test[vals_test]
    df_bas1_train = bas1_train[vals_test]

    return df_bas1_train, df_bas1_test

#  Sub Components  #


def import_and_filter(
    folder, train_filenames, keys, include_alarms=True, dim_remove=[],
    time_list=[]
):
    """imports plant data and creates data frames with filtered data and keys

    Input:
    folder = folder containing raw data.
    train_filenames = list of filenames to be used as dataset.
    keys = file name from current directory containing the keys spreadsheet
    include_alarms = include or remove alarms from dataset (default = True)
    dim_remove = list of descriptors to remove from dataset (default = NULL)

    Output:
    bas1 = dataframe containing filtered plant data"""

    # creates blank dataframe for appending
    df = pd.DataFrame()

    # imports and concats all datasets
    for train_string in train_filenames:

        dfloop, key = data_import(
            folder, train_string, keys
        )
        df = pd.concat([df, dfloop], ignore_index=True)

    # removes optional timeframes

    # df_time = time_filter(df, time_list)

    # removes categories of descrdiptors from the dataset
    bas = data_BAS(df, key, dim_remove=dim_remove)

    # filters out alarms
    if include_alarms is False:
        bas1 = alarm_filter(bas, key)
    else:
        bas1 = bas

    # verification statement
    print(
        'Filtered data contains ' + str(bas1.shape[0]) + ' points and '
        + str(bas1.shape[1]) + ' dimensions.'
    )

    return bas1


def data_import(dat_folder, string, keys):
    """imports plant data and creates data frames with raw data and keys

    dat_folder = folder containing raw data.
    string = prefix of the csv files to be imported.
    keys = file name from current directory containing the keys spreadsheet

    Output:
    df = dataframe containing plant data
    key = dataframe containing descriptor key"""

    # Assert that string is .csv
    
    assert string.endswith('.csv'), (
        "file name " + string + " is not a csv"
    )

    # extracts file names
    dat_list = glob.glob(os.path.join(dat_folder, string))
    print(dat_list)
    

    # reads and appends content from file to a data frame
    df = pd.read_csv(dat_list[0])

    key = pd.read_excel(keys)

    return df, key


def data_BAS(df, key, dim_remove=[]):
    '''Filters out descriptors containing NaN values, calculated descriptors,
     and miscelaneous descriptors specified by the user.

    Input:
    df = dataframe containing plant data
    key = dataframe containing descriptor key
    dim_remove = list of descriptors to remove from dataset (default = NULL)

    Output:
    bas = dataframe filtered for descriptors and NaN values'''

    # finds keys from categories BAS, Chiller, Condenser Water Pump
    # and Cooling Tower Cell
    keys = []

    key_list = ["BAS", "Chiller", "Condenser Water Pump", "Cooling Tower Cell"]

    for k in range(0, len(key_list)):
        key_loop = key.loc[
            key['PointType'].str.contains(key_list[k])==True, 
            'DataPointName'
        ].T.tolist()
        keys += key_loop

    # removes DataPointNames that containt the prefix CHWV
    kw = [x for x in keys if 'kW' not in x]
    vals = [x for x in kw if not x.startswith('CHWV')]

    # optional dimension remover
    for dim in dim_remove:
        vals.remove(dim)

    # tests whether all values from the point list spreadsheet are column
    # headings of the dataset
    print('Descriptors in the points list that are not in the datasets.')
    for x in vals:
        if x not in df.columns:
            # prints and removes any string not found in the data
            print(x)
            vals.remove(x)
    # tests whether all values from the point list spreadsheet are column
    # headings of the dataset

    vals_new = [x for x in vals if x in df.columns]

    # expresses data using columns specified by the vals list
    bas = df[vals_new+['OptimumControl', 'kW/Ton']]

    print(
        'Original data contains ' + str(df.shape[0]) + ' points and '
        + str(df.shape[1]) + ' dimensions.'
    )

    return bas.dropna()


def time_filter(df, time_list):
    ''' Filters out a specified timestamp from the dataset 
    
    df = dataframe containing the plant data
    time_list = timestamps to be removed'''
    
    #df = df[~df['timestamp'].str.contains('|'.join(time_list))]
    return #df


def alarm_filter(bas, key):
    """removes any datapoints with alarms going off or without optimum control

    bas = dataframe containing plant data
    key = dataframe containing descriptor key"""

    # filters kes to select those with alarm units that are also BAS
    key_alarm = key.loc[
        key['Units'].str.contains("Normal/Alarm") == True, 'DataPointName'
    ]

    vals = [x for x in key_alarm if x in bas.columns]

    # tests whether an alarm is going off
    bas_start = bas.shape[0]
    for alm in vals:

        # returns dataframe that have no alarms going off
        bas = bas[bas[alm] == 0]

        bas_end = bas.shape[0]

        # compares shape before and after alarm filtering
        if bas_end != bas_start:
            print(
                'A ' + alm + ' was noted and ' + str(bas_start-bas_end)
                + ' datapoints were removed from the dataset.'
            )

    bas = bas[bas['OptimumControl'] == 1]

    return bas

# two plant test train function
# THIS FUNCTION DOES NOT NEED UNIT TESTS!!!!
# IT IS NOT BEING USED RIGHT NOW!!!


def train_plt_ref(
    train_folder, train_string, train_keys, test_folder,
    test_string, test_keys, include_alarms=True
):
    """imports test and train plant data and creates data frames with
     filtered data

    Input:
    train_folder = folder containing raw data.
    train_string = prefix of the csv files to be imported.
    train_keys = file name from current directory containing the keys
     spreadsheet
    test_folder = folder containing raw data.
    test_string = prefix of the csv files to be imported.
    test_keys = file name from current directory containing keys spreadsheet
    include_alarms = include or remove alarms from dataset (default = True)

    Output:
    df_bas1_train = dataframe containing filtered training plant data
    df_ce bas1_test = dataframe containing filtered test plant data"""
    print('Filtering Training Set')
    df, key = data_import(train_folder, train_string, train_keys)
    bas = data_BAS(df, key)
    if include_alarm is False:
        bas1_train = alarm_filter(bas, key)
    else:
        bas1_train = bas

    print('Filtering Test Set')
    df, key = data_import(test_folder, test_string, test_keys)
    bas = data_BAS(df, key)
    if include_alarm is False:
        bas1 = alarm_filter(bas, key)
    else:
        bas1 = bas

    vals_test = [x for x in bas1.columns if x in bas1_train.columns]
    df_bas1_test = bas1[vals_test]
    df_bas1_train = bas1_train[vals_test]

    return df_bas1_train, df_bas1_test
