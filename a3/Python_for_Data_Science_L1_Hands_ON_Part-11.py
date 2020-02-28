#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
13. The Pima Indians Diabetes Binary Classification dataset csv file contains all of the data of female   patients of the same age belonging to Pima Indian heritage. The data includes medical data, such as glucose and insulin levels, as well as lifestyle factors of the patients. The columns in the dataset are as follows: 
•	Number of times pregnant
•	Plasma glucose concentration of 2 hours in an oral glucose tolerance test
•	Diastolic blood pressure (mm Hg)
•	Triceps skin fold thickness (mm)
•	2-hour serum insulin (mu U/ml)
•	Body mass index (weight in kg/(height in m)^2)
•	Diabetes pedigree function
•	Age (years)
•	Class variable (0 or 1)
•	The last column is the target variable or class variable that takes the value 0 or 1, where 1 is positive or affected by diabetes and 0 means that the patient is not affected.
•	You have to build models that could predict whether a patient has diabetes or tests positive or not using logistic regression
'''
#Solution

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Pima_df =pd.read_excel("F:/DataSets/Pima Indians Diabetes Binary Class.xlsm")
#Looking at columns in the DataSet
Pima_df.columns


# In[3]:


Pima_df.head()


# In[4]:


Pima_df.shape


# In[5]:


#Reanaming the Target Column 
Pima_df.rename(columns={'Class variable (0 or 1)':'OutCome'},inplace =True)
Pima_df


# In[6]:


Pima_df.groupby('OutCome').size()


# In[7]:


# Have to see which of the columns are to use to build the model,by checking the correlation with the OutCome column.
corr =Pima_df.corr()
corr['OutCome'].sort_values(ascending =False)


# In[8]:


# The  The columns with   Plasam glucose concentration and Body mass index have highest correlation with Target Column OutCome.
#So the two columns will be used.
#Renaming Colums
Pima_df.rename(columns={'Plasma glucose concentration a 2 hours in an oral glucose tolerance test':'Plasma Glucose Concentartion','Body mass index (weight in kg/(height in m)^2)':'Body Mass Index'},inplace =True)
Pima_df[['Plasma Glucose Concentartion','Body Mass Index']]


# In[9]:


#Replacing Os with NaN and Dropping NaN's
Pima_df[['Plasma Glucose Concentartion', 'Body Mass Index']]=Pima_df[['Plasma Glucose Concentartion', 'Body Mass Index']].replace(0,np.NaN)
Pima_df.dropna(inplace=True)


# In[10]:


#Build the Model
X =Pima_df[['Plasma Glucose Concentartion', 'Body Mass Index']].values
y_actual = Pima_df['OutCome'].values


# In[11]:


# For normal Distribution should have mean =0 and standard devaiation =1.So scale our selected columns for the model
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

mean = np.mean(X, axis=0)
print('Mean: (%d, %d)' % (mean[0], mean[1]))
standard_deviation = np.std(X, axis=0)
print('Standard deviation: (%d, %d)' % (standard_deviation[0], standard_deviation[1]))


# In[12]:


#Now training the model.Splitting into 80% Training Data and 205 Test Data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y_actual, test_size = 0.2, random_state = 0)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
#Predicting using the model
model.fit(X_train, y_train.ravel())
y_predicted = model.predict(X_test)
#Testing our model
y_actual


# In[13]:


y_predicted


# In[14]:


#Testing the acuuracy through Confusion Matrix.
from sklearn.metrics import confusion_matrix
confusion_mat = confusion_matrix(y_test, y_predicted)
print("Confusion Matrx",confusion_mat)


# In[15]:


#29 True Positives and and 93 True Negatives .So total 119 correct prediction  out of 151 .
print("Accuracy of model",119/151*100)


# In[ ]:




