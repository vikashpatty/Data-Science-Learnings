#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''

6.Create dept dataframe and emp dataframe  with suitable data and perform inner , leftouter,RightOuter andFullOuter Joins based on common column Deptno.

Dept Data Frame will have
Deptno
Dname
Loc

Emp DataFrame will have below columns
Deptno
Eno
Sal

'''
#SOLN
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

Dict1 = {'Dept_No' :[101,110,205,890,905],
'Dname' :['Finance','HR','IT','Health','Travel'],
'Loc' :['Hyd','Vizag','Lucknow','Delhi','Mumbai']}

Dict2 ={'Dept_No' :[56,678,101,907,784,110,890],
'Eno' :[2003,4004,6789,8909,3890,9004,8990],
'Sal':[20000,25000,50000,100000,90000,86000,200000]}
Dept = pd.DataFrame(Dict1)
Emp = pd.DataFrame(Dict2)
Dept


# In[3]:


Emp


# In[5]:


#Inner join on Dept and Emp DataFrames
Df_inner_join= pd.merge(Dept,Emp,on='Dept_No',how='inner')
Df_inner_join


# In[6]:


#Left Outer  join on Dept and Emp DataFrames
Df_LeftOuter_join= pd.merge(Dept,Emp,on='Dept_No',how='left')
Df_LeftOuter_join


# In[7]:


#Right Outer  join on Dept and Emp DataFrames
Df_RightOuter_join= pd.merge(Dept,Emp,on='Dept_No',how='right')
Df_RightOuter_join


# In[8]:


#Full Outer join on Dept and Emp DataFrames
Df_FullOuter_join= pd.merge(Dept,Emp,on='Dept_No',how='outer')
Df_FullOuter_join


# In[ ]:




