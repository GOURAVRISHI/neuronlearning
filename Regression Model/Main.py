# Necessary import 
import pandas as pd 
import pickle 
import matplotlib.pyplot as plt

import sklearn.linear_model

# Data is about amount spent on advertising throught different channels like TV, Radio & Newspaper. 
# Goal is to predict how expenses on each channel affects the Sales and find ways to optimise the Sales exps.
data=pd.read_csv('C:\Users\GAURAV\.spyder-py3\Regression Model\Advertising.csv')
data

