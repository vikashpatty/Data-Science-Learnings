#!/usr/bin/env python
# coding: utf-8

# In[3]:


#11. Calculate Pearson correlation coefficient between Girth and Volume in trees dataset( trees csv file) Please  mention what you draw from correlation coefficient

import pandas as pd
import xlrd
from scipy import stats
import numpy as np
from scipy.stats import t
tree_df =pd.read_excel("F:/DataSets/Trees.xlsm")
corr =stats.pearsonr(tree_df['Girth'],tree_df['Volume'])[0]
print(corr)
#Conclusion 
print("As we can see the value of Pearson Correlation coefficent is 0.967(rounded off). It depicts a strong positive relationship..ie as Girth increase ,Volume also increases and vice versa.")


# In[ ]:




