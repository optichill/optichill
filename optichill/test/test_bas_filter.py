import pandas as pd
from optichill import bas_filter


def test_train_single_plt():
    dat_folder = 'data'
    train_filenames = ['Plt1 h 2017-05.csv']
    test_filenames = ['Plt1 h 2017-11.csv']
    keys = 'data/Plt1 Points List.xlsx'

    df_train, df_test = bas_filter.train_single_plt(
        dat_folder, train_filenames, test_filenames,
        keys, include_alarms=False
    )

    assert len(df_train.columns.tolist()) == len(df_test.columns.tolist()), (
        "the training and testing sets have different numbers of descriptors!"
    )

    return


def test_import_and_filter():

    dat_folder = 'data'
    string = ['Plt1 h 2017-05.csv', 'Plt1 h 2017-11.csv']
    keys = 'data/Plt1 Points List.xlsx'

    df = bas_filter.import_and_filter(
        dat_folder, string, keys, include_alarms=False
    )

    assert df.shape[0] != 0, (
        "you've filtered out all of your data!"
    )
    assert df.shape[1] != 0, (
        "you have no descriptors, check your filtering!"
    )

    return


def test_data_import():
    dat_folder = 'data'
    string = 'Plt1 h 2017-05.csv'
    keys = 'data/Plt1 Points List.xlsx'

    df, key = bas_filter.data_import(dat_folder, string, keys)

    assert isinstance(df, pd.DataFrame), (
        "variable containing data is not a pandas dataframe!"
    )
    assert isinstance(key, pd.DataFrame), (
        "variable containing data is not a pandas dataframe!"
    )

    assert 'DataPointName' in key.columns.tolist(), (
        "The datapoint names are not in the points list!"
    )
    assert 'PointType' in key.columns.tolist(), (
        "the point types are not in the points list!"
    )
    assert 'Units' in key.columns.tolist(), (
        "the units are not in the points list!"
    )

    return


def test_data_BAS():

    dat_folder = 'data'
    string = 'Plt1 h 2017-05.csv'
    keys = 'data/Plt1 Points List.xlsx'
    dim_remove = ['HX1CDWRT', 'HX1CHWST']

    df, key = bas_filter.data_import(dat_folder, string, keys)
    bas = bas_filter.data_BAS(df, key, dim_remove=dim_remove)

    assert isinstance(bas, pd.DataFrame), (
        "variable containing filtered data is not a pandas dataframe!"
    )

    cat_test = bas.columns.tolist()
    # cat_test.remove('timestamp')

    for cat in cat_test:
        assert cat in key['DataPointName'].T.tolist(), (
            cat + " is not in the points list!"
        )

    return


def test_alarm_filter():
    dat_folder = 'data'
    string = 'Plt1 h 2017-05.csv'
    keys = 'data/Plt1 Points List.xlsx'
    dim_remove = []

    df, key = bas_filter.data_import(dat_folder, string, keys)
    bas = bas_filter.data_BAS(df, key, dim_remove=dim_remove)
    bas_alm = bas_filter.alarm_filter(bas, key)

    assert "Normal/Alarm" not in bas_alm.columns.tolist(), (
        "there are still alarms in the dataset!"
    )

    return
