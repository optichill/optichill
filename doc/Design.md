## Functional Use Cases: 
![DESIGN](https://github.com/optichill/optichill/blob/master/doc/Design.jpg)
### Data Cleaning:
* **Name**: bas_filter.train_single_plt
* **What it does**: Imports test and train plant data and creates data frames with filtered data. 
* **Input**: 
	* folder = path to location of raw data files
	* train_filenames = list of filenames to be used as the training set.
	* test_filenames = list of filenames to be used as the testing set.
	* keys = file name from current directory containing the keys spreadsheet
	* include_alarms = include or remove alarms from dataset (default = True)
	* dim_remove = list of descriptors to remove from the dataset (default = NULL)

* **Output**:
	* df_bas1_train = dataframe containing filtered training data
	* df_bas1_test = dataframe containing filtered testS data

### Training Model with Gradient Boosting Machines
* **Name**: GBM_model
* **What it does**: Uses the scikit-learn toolbox to train a model with gradient boosting machines. 
* **Input**: Dataset output from the data cleaning function.
* **Output**: Trained model (hdf5?). 

### Determining Feature importance: Gradient Boosting Machines
* **Name**: feature_importance
* **What it does**: Uses the trained model to determine the relative importance of features, as determined by how often a split is made based on that feature within the decision trees of the gradient boosting machines. 
* **Input**: Trained model.
* **Output**: List of features with their corresponding relative importance. 

### Predict the efficiency of chiller plants
* **Name**: GBM_predict 
* **What it does**: Uses the trained model to predict the chiller plant efficiency on test data.
* **Input**: Trained model
* **Output**: Prediction values for test data.
