import numpy as np
import pandas as pd
from dataCleaning import bas_filter
from sklearn.preprocessing import MinMaxScaler

def scale_avg(dfs):
	""" imports the data, scales all the features on a scale 
	from 0 to 1 and takes the mean of each row across different 
	plant datasets 

	Input:
	dfs: A list of the dataframes
	
	Output:
	df_avg_scale: A dataframe with the average values of all the plants 
	for each row."""

	common_cols = list(set.intersection(*(set(df.columns) for df in dfs)))
	df_concat = pd.concat([df[common_cols] for df in dfs], ignore_index=True)
	by_row_index = df_concat.groupby(df_concat.index)
	df_avg = by_row_index.mean()
	#Moving the kW/ton column to be the last column:
	df_avg = df_avg[[c for c in df_avg if c not in ['kW/Ton']] + ['kW/Ton']]
	scale = MinMaxScaler()
	scale.fit(df_avg)
	df_avg_scale = scale.transform(df_avg)
	df_avg_scale = pd.DataFrame(df_avg_scale)
	df_avg_scale.columns = df_avg.columns

	return df_avg_scale