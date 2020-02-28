#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Descriptive and Inferential Statistics:
#7.Suppose the height of men in the United Kingdom is known to be normally distributed with a mean of 177 centimeters and a standard deviation of 10 centimeters. If you were to select a man from the United Kingdom population at random, what is the probability that he would be more than 200 centimeters tall?
#Soln
#To solve this problem, you will first need to calculate the Z value of the variable of interest and then use a Z distribution table to look up the probability. To calculate the Z score, use the following formula.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mean =177
Standard_Deviation = 10
variable_of_interest =200
Z_Score = ((variable_of_interest-mean)/Standard_Deviation)
print("Z_Score =",Z_Score)
#Now by Z Distribution table Probability is
Probability =.9893
print("Probability =",Probability)


# In[ ]:




