#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
14.Use hotel.csv file and Show how to cluster hotel location data with K-means Clustering. That is performK-means clustering on hotel location data to identify whether the hotels are located in the same district. 
Using k-means cluster location data for 3 clusters. 

'''
import pandas  as pd 
import scipy  as sp
from sklearn.cluster import KMeans
import numpy as np
import xlrd
from sklearn.model_selection import train_test_split

Hotel_df = pd.read_excel("F:/DataSets/Hotel.xlsm")
print(Hotel_df.columns)
#Checking for nulls 
print(Hotel_df.isna())


# In[2]:


print(Hotel_df.head())


# In[3]:


#As we have categorical Data in district column,so standardizing  it to 0,1,2
Hotel_df['district'].replace('Beitou',0,inplace =True)
Hotel_df['district'].replace('Zhongshan',1,inplace =True)
Hotel_df['district'].replace('Xinyi',2,inplace =True)
Hotel_df['district']


# In[8]:


# Data Preparation
X=np.array(Hotel_df[['lat','lon']])

#R = np.reshape(X,-1,1)
#print(R.shape)
y = np.array(Hotel_df['district'].values)
#Splitting iwth 70:30 ratio for Training and Test Data
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size = 0.3,random_state = 0)
#Building the Model

#Number of Clusters =3
n_clusters=3
kmeans =KMeans(n_clusters =n_clusters)
kmeans.fit(X)

KMeans(algorithm='auto', copy_x=True, init=3, max_iter=300,
  n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',
    random_state=None, tol=0.0001, verbose=0)

#Testing the Agorithm   
prediction = kmeans.predict(xTest)
    
print(yTest)
print(prediction)


# In[5]:


#Testing the accurcay of the Model by Confusion Matrix
from sklearn.metrics import confusion_matrix
confusion_mat = confusion_matrix(yTest, prediction)
print(confusion_mat)


# In[6]:


#Calculating the accuracy through completeness_score
from sklearn.metrics import completeness_score
print(completeness_score(yTest,prediction))


# In[ ]:




