#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''

9.Perform T-test on two classes that are given a mathematics test and have 10 students in each class. Determine if 2 distributions are identical or not.

class1_score = np.array([45.0, 40.0, 49.0, 52.0, 54.0, 64.0, 36.0, 41.0, 42.0, 34.0])

class2_score = np.array([75.0, 85.0, 53.0, 70.0, 72.0, 93.0, 61.0, 65.0, 65.0, 72.0])

'''
import numpy as np
from scipy.stats import t
from  scipy import stats
#Defining the significance level called aplha
alpha =0.05
class1_score = np.array([45.0, 40.0, 49.0, 52.0, 54.0, 64.0, 36.0, 41.0, 42.0, 34.0])

class2_score = np.array([75.0, 85.0, 53.0, 70.0, 72.0, 93.0, 61.0, 65.0, 65.0, 72.0])
#Calculating the  mean of two Samples
mean1 =np.sum(class1_score)/10
mean2 =np.sum(class2_score)/10
#Calculating Degrees of freedom
degrees_of_freedom =10+10-2

#Calculating Standard Deviations of Two Samples
std1,std2 =np.std(class1_score),np.std(class2_score)

j =np.sqrt((std1**2)/10 +(std2**2)/10)
#Calculating -the t statistic value
t_stat=(mean1-mean2)/j
#Calculating the critical t-value
cv = t.ppf(1.0 - alpha, degrees_of_freedom)
cv
#Checking if the t_statistic value is greater than t-crictical value or not
if abs(t_stat) <= cv:
    print('Accept null hypothesis that the 2 Distributions  are identical.')
else:
    print('Reject the null hypothesis that the 2 Distributions are Identical ie.the Two Distributionsclass_score1  and class score_2 are Significantly Different.')
# Cross checking the  results with scipy's internal function to calculate t_statistic .The implementation is correct 
t2 = stats.ttest_ind(class1_score,class2_score)[0]
print(t_stat)
print(t2)


# In[ ]:





# In[ ]:




