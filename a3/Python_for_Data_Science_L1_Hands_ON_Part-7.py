#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
10. The mean score of the mathematics exam at a national level is 60 marks and the standard deviation is 3 marks. The mean marks of a class are 53. The null hypothesis is that the mean marks of the class are similar to the national average.  Test this Hypothesis using Z – Test. 
'''
from scipy import stats
#  Null Hypothesis -mean =60
#Alternate Hypothesis -mean!=60
#SIgnificance Level alpha =0.05
alpha =0.05
#We will perform a Two Tailed  Z-Test
#Step1)
X= 60  
mean =53
sd =3
#Step2)
#cALCULATE The Z_score
Z_Score = (X-mean)/sd
print(Z_Score)
#Step3) Calculate the p_value
p_value=stats.norm.pdf(X,mean,sd)
print(p_value)
if p_value<alpha:
  print("Reject the Null Hypothesis")
  print("The mean marks of the class are signficantly different to the national average")
else:
  print("Accept the Null Hypothesis")
  print("mean marks of the class are similar to the national average")  


# In[ ]:




