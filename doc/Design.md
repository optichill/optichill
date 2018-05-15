## Functional Use Cases: 
![DESIGN]()
### Data Cleaning:
* **Name**: bas_filter
* **What it does**: Filtering out the features of the dataset to get only the BAS and measured values of the plant equipment. 
* **Input**: Raw Spreadsheets. 
* **Output**: Data with the desired features. 

### Determining Feature importance: Decision Trees
* **Name**: feature_importance
* **What it does**: Scales the different features from the Plant 1 dataset with their relation to the plant efficiency i.e. kW/ton. The deeper the decision tree for that partucilar feature, the higher the importance. 
* **Input**: Dataset.
* **Output**: Features with their corresponding importance. 

### Regression analysis between the different features
* **Name**: linear_regr
* **What it does**: Fits different types of regression models on the different features of the data from the Plant 1 dataset to determine the coefficient and intercept between kW/ton and different features. 
* **Input**: Dataset.
* **Output**: Regression coefficients. 

### Predict the efficiency with the different features 
* **Name**: 
* **What it does**:
* **Input**: 
* **Output**: 

### Fitting data from other plants with the features determined:
* **Name**: 
* **What it does**:
* **Input**: 
* **Output**: 


