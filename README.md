# OPTICHILL - Predicting the efficiency of a chiller plant.

[![Build Status](https://travis-ci.org/optichill/optichill.svg?branch=master)](https://travis-ci.org/optichill/optichill)
[![Coverage Status](https://coveralls.io/repos/github/optichill/optichill/badge.svg?branch=master)](https://coveralls.io/github/optichill/optichill?branch=master)

Optichill is a tool that can be used to predict the efficiency of a given chiller plant based on the recorded data from the plant. The module sorts out the chiller plant data to filter redundant features. The features are then sorted based on "importance" with plant efficiency (measured as kW/ton) with Gradient Boosted Machines. 	

## SOFTWARE DEPENDENCIES
* Python Version 3.5 and 3.6
* Packages used in the tool "os, glob, numpy, scipy, pandas, sklearn, pickle"

## ORGANIZATION OF THE PROJECT
```
data/
doc/
	images/
	posters/
	Design.md
	README.md
	bas_filter_doc.md
examples/
optichill/
	test/
		_init_.py
		test_GBM_model.py
		test_bas_filter.py
	GBM_model.py
	_init_.py
	bas_filter.py
	version.py
.coveragerc
.gitignore
.travis.yml
LICENSE
README.md
requirements.txt
setup.py
```
## SETUP

1.	Clone this repo onto your local machine
2.  Pip install the module with the following command:
```
pip install optichill
```
3.  Start work using the tutorials notebook under examples
4.  Expaind your work to any of the notebooks in examples