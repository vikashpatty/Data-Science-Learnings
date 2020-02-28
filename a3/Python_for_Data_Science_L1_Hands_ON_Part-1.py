#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Date Preparation and Exploration: 
#1. Reading a Titanic dataset from a CSV file 
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np  
Df1 = pd.read_csv("F://DataSets//Titanic.csv")
#2. Detecting missing values
'''
Missing values reduce the representativeness of the sample, and furthermore, might distort inferences about the population.  

How many missing values are there in  age  Attribute of Titanic dataset 
'''


print(Df1.Age.isnull().count())


# In[23]:


'''
3.Imputing missing values 

After detecting the number of missing values within each attribute, we have to impute the missing values since they might have a significant effect on the conclusions that can be drawn from the data. 

 Assign the missing value to the most likely port, which is Southampton 
'''
Df1.fillna('Southampton',inplace=True)
print(Df1)


# In[ ]:


'''
4. Exploring and visualizing data 

After imputing the missing values, one should perform an exploratory analysis, which involves using a visualization plot and an aggregation method to summarize the data characteristics. The result helps the user gain a better understanding of the data in use. 

 

a) Bar Plot which shows how many passengers survived and how many perished 

b) Bar Plot which shows how many passesngers travelled by first class, second class and thrid class 

c) Barplot which shows how many are male passengers and how many are female passengers 

d) plot histogram of different ages 

e) Stacked barplot's  to find out  

3 -which gender is more likely to perish during shipwrecks 

 -Passenger survival by class 

f) Box Plot which shows passenger survival by age 

'''


# In[25]:


#a) Bar Plot which shows how many passengers survived and how many perished 

x1 = Df1[Df1['Survived']==0].Survived.count()
x2 = Df1[Df1['Survived']==1].Survived.count()

n =2
k=0
index =np.arange(n)


plt.bar(1,x1,alpha =0.8,color ='b',label='Survived')
plt.bar(0,x2,alpha =0.8,color='g',label ='Perished')
plt.xlabel("Survived or Perished")
plt.ylabel("Total Passengers")
plt.xticks(index+k,('Survived','Perished'))

plt.title('Survived or Perished')
plt.legend()
plt.show()


# In[26]:



#b) Bar Plot which shows how many passesngers travelled by first class, second class and thrid class

x1 =Df1[Df1['Pclass']==1].Pclass.count()
x2=Df1[Df1['Pclass']==2].Pclass.count()
x3 =Df1[Df1['Pclass']==3].Pclass.count()
plt.bar(1,x1,alpha =0.8,color ='b',label='First Class')
plt.bar(2,x2,alpha =0.8,color ='g',label='Second Class')
plt.bar(3,x3,alpha =0.8,color ='c',label='Third Class')
plt.xlabel("Classes")
plt.ylabel("Total Passengers")
n =3
k=1
index =np.arange(n)

plt.xticks(index+k,('First Class','Second Class','Third Class'))

plt.title('Classes Comparison')
plt.legend()
plt.show()


# In[27]:




#c) Barplot which shows how many are male passengers and how many are female passengers
x1 =Df1[Df1['Sex']=='male'].Sex.count()
x2 =Df1[Df1['Sex']=='female'].Sex.count()
plt.bar(1,x1,alpha = 0.8,color = 'r',label='male')
plt.bar(2,x2,alpha = 0.8,color = 'g',label='female')
plt.xlabel("Sex")
plt.ylabel("Total Passengers")
n =2
k=1
index =np.arange(n)
plt.xticks(index+k,('male','female'))
plt.title('Sex By Passengers')
plt.legend()
plt.show()


# In[29]:


#d) plot histogram of different ages

Df1.Age.replace('Southampton',np.nan,inplace =True)
x1 = Df1.groupby(['Age']).Age.agg(['count'])
bins =[0,10,20,30,40,50,60,70,80]
x1 =x1.sort_values(by='count')
x = x1.index
plt.hist(x,bins)
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()


# In[31]:


'''
e) Stacked barplot's  to find out  
a) -which gender is more likely to perish during shipwrecks 
b)-Passenger survival by class 
''' 
#a) -which gender is more likely to perish during shipwrecks 
m1 =Df1[(Df1.Survived==0) &(Df1.Sex =='male')]
m2 =Df1[(Df1.Survived==0) &(Df1.Sex =='female')]
y1 =m1.Sex.count()
y2 =m2.Sex.count()
x_1 =y1+y2
plt.bar(x_1,y1,alpha =0.8,color='b',label='male')
plt.bar(x_1,y2,alpha =0.8,color='g',label='female')
plt.xlabel('Perished')
plt.ylabel('Gender')
plt.title('Gender comparison on Basis of ShipWrecks')
plt.legend()
plt.show()


# In[32]:


#e) b)Passenger survival by class 
n1 =Df1[(Df1.Survived==1) &(Df1.Pclass ==1)]
n2 =Df1[(Df1.Survived==1) &(Df1.Pclass ==2)]
n3 =Df1[(Df1.Survived==1) &(Df1.Pclass ==3)]

r_1 =n1.Pclass.count()
r_2 =n2.Pclass.count()
r_3 =n3.Pclass.count()
x__1 = Df1[Df1['Survived']==1].Survived.count()

plt.bar(x__1,r_1,alpha =0.8,color = 'r',label='First Class')
plt.bar(x__1,r_2,alpha =0.8,color = 'g',label='Second Class')
plt.bar(x__1,r_3,alpha =0.8,color = 'y',label='Third Class')

plt.xlabel('Total Survivors')
plt.ylabel('Passenger Class')
plt.title('Passenger Survival by Class')
plt.legend()
plt.show()


# In[33]:



#f) Box Plot which shows passenger survival by age 
Df1.Age.replace('Southampton',np.nan,inplace =True)
z_1 = Df1[['Survived','Age']]
z_2 =z_1[z_1.Survived==1]

z_2.boxplot(column='Age', by ='Survived')
plt.show()


# In[21]:












# In[ ]:





# In[ ]:




