# OPTICHILL - Predicting the efficiency of a chiller plant.

[![Build Status](https://travis-ci.org/optichill/optichill.svg?branch=master)](https://travis-ci.org/optichill/optichill)
[![Coverage Status](https://coveralls.io/repos/github/optichill/optichill/badge.svg?branch=master)](https://coveralls.io/github/optichill/optichill?branch=master)

Optichill is a tool that can be used to predict the efficiency of a given chiller plant based on the recorded data from the plant. The module sorts out the chiller plant data to filter redundent features. The features are then sorted based on "importance" with plant efficiency (measured as kW/ton) with Gradient Boosted Machines. 	

## SOFTWARE DEPENDENCIES
* Python Version 3.6

## PACKAGES INCLUDED IN THE TOOL
* Numpy
* Pandas
* Scipy
* Scikit Learn

## FOLDERS IN THE REPOSITORY
* **doc** - Contains the design of the project, figures and the project poster. 
* **examples** - Houses all the jupyter notebooks that were used to develop the modules, and the .csv files of the features and their importance. 
* **optichill** - Contains the modules for data filtering (`bas_filter.py`) and for prediction and feature importance (`gbm.py`) 

## SETUP

## ACKNOWLEDGEMENTS