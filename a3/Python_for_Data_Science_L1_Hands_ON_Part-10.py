#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''

12. Use Automobile price data Raw csv file : 
•	Split data 80% to train 20% for test
•	predict price for 20% test data
•	Determine R-Squared value
'''
#Importing the required packages

import pandas as pd
import numpy as np
import xlrd
import matplotlib.pyplot as  plt 
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
#Reading the DataSet
Auto_df =pd.read_excel("F:\DataSets\AutoMobile Price Data.xlsm")
#print(Auto_df)

#Exploratory Data Analysis
#Dropping tyhe NAn'S
Auto_df.replace('?',np.NAN,inplace =True)
Auto_df.dropna(inplace=True)
#We will use only numeric columns for our MODEL

cols_for_model =['symboling','normalized-losses','wheel-base','length','width','height','curb-weight','engine-size','bore','stroke','compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg']
Auto_df1 =Auto_df[cols_for_model].astype(float)

Target_Variable = Auto_df['price']
#Building the model
X= np.array(Auto_df1)
Y = Target_Variable
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=101)
regr=linear_model.LinearRegression()
regr.fit(X_train,Y_train)
y_pred=regr.predict(X_test)
print("Y_Predicted",y_pred)

print('RSquared Value(Coefficient of Determinations) : %.2f' % r2_score(Y_test, y_pred))



# In[ ]:




