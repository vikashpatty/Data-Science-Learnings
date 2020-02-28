#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
12.Suppose that you want to perform a hypothesis test to help determine whether the correlation between tree girth and tree volume is statistically significant. 

Perform a two-sided test of the Pearson's product moment correlation between tree girth and volume at the 5% significance level, 
'''

import pandas as pd
import xlrd
from scipy import stats
import numpy as np
from scipy.stats import t
tree_df =pd.read_excel("F:/DataSets/Trees.xlsm")
print(tree_df.columns)
Class1 =np.array(tree_df['Girth'])

Class2 =np.array(tree_df['Volume'])
alpha =0.5
#Sample size of each class is 30
df=(30+30)-2
mean1 =np.sum(Class1)/30
mean2=np.sum(Class2)/30
std1,std2 =np.std(Class1),np.std(Class2)
denom=(std1**2)/30+(std2**2)/30
print()
t_statistic =(mean1-mean2)/(np.sqrt(denom))
print()

#Calculating the critical t-value
cv = t.ppf(1.0 - alpha, df)
cv

#Checking if the t_statistic value is greater than t-crictical value or not
if abs(t_statistic) <= cv:
    print('Accept null hypothesis that the correlation between tree girth and tree volume is statistically not significant')
else:
    print('Reject the null hypothesis that the correlation between tree girth and tree volume is statistically significant')
# Cross checking the  results with scipy's internal function to calculate t_statistic .The implementation is correct 
tst = stats.ttest_ind(Class1,Class2)[0]

print(t_statistic)
print(tst)


# In[ ]:




