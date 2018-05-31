## Functional Use Cases: 
![DESIGN](https://github.com/optichill/optichill/blob/master/doc/Design.jpg)
### Data Cleaning:
* **Name**: bas_filter
* **What it does**: Filtering out the features of the dataset to get only the BAS and measured values of the plant equipment. 
* **Input**: Raw Spreadsheets. 
* **Output**: Data with the desired features. 

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
