#!/usr/bin/env python
# coding: utf-8

# In[2]:


''''
Visualization:

5. Read from sample superstore xl file  into pandas dataframe and perform below operations

a) Display Subcategory wise sum of profit
b) Exclude Office Furniture SubCategory
c) Sort SubCategory in Desc order
d) Categorywise sum of profit in pie chart
e) Line Chart yearwise sum of profit
f) Display Top 10 most profitable customers
g) scatter plot between profit and sales
'''
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np  
Sup_Store = pd.read_excel("F:/DataSets/Sample - Superstore.xls")


# In[4]:


Sup_Store.describe()


# In[5]:


Sup_Store.head()


# In[6]:


#a) Display Subcategory wise sum of profit
Sub1 =Sup_Store.groupby('Sub-Category')
Sub_Pro = Sub1.Profit.sum()
plt.barh(Sub_Pro.index,Sub1.Profit.sum())
plt.xlabel('Profit')
plt.ylabel('Sub-Category')


# In[7]:


#b) Exclude Office Furniture SubCategory
Sub2 = Sup_Store[Sup_Store['Category']=='Furniture'].index

Sub3 =Sup_Store.drop(Sub2)
Sub3 =Sub3.groupby('Sub-Category')
Sub_Pro2 = Sub3.Profit.sum()
plt.barh(Sub_Pro2.index,Sub3.Profit.sum())
plt.xlabel('Profit')
plt.ylabel('Sub-Category')


# In[8]:


#c) Sort SubCategory in Desc order

Sub_Pro3 = Sup_Store.groupby('Sub-Category')
Sub_C = pd.DataFrame(Sub_Pro3.Profit.sum())
Sub_C_Desc =Sub_C.sort_values(by='Profit',ascending=False)
plt.barh(Sub_C_Desc.index,Sub_C_Desc.Profit,color ='g',label='Sub-Ctegory in Descnding Order wise of Profit')
plt.xlabel('Profit')
plt.ylabel('Sub-Category')
plt.title('Sub-Category in Descending Order of Profit')


# In[9]:


#d) Categorywise sum of profit in pie chart
Sub_Pro4 = Sup_Store.groupby('Category')
b=list(Sub_Pro4.Profit.sum().values)
t =list(np.unique(Sup_Store['Category']))
explode = (0.1, 0, 0) 
colors = ['gold', 'red', 'blue']
plt.pie(b,explode=explode,labels=t,colors =colors,autopct='%1.1f%%',shadow=True,startangle=90)


# In[10]:


#e) Line Chart yearwise sum of profit

Sup_Store['Order Year'] = pd.DatetimeIndex(Sup_Store['Order Date']).year
Sup_Pro5 =Sup_Store.groupby('Order Year')
Sub_Pr= pd.DataFrame(Sup_Pro5.Profit.sum())
plt.plot(Sub_Pr.index,Sub_Pr['Profit'],label='Yearwise Sum of Profit')
plt.xlabel('Year')
plt.ylabel('Profit')
plt.legend()


# In[12]:


#f) Display Top 10 most profitable customers
Sup_Pro6 = Sup_Store[['Profit','Customer Name']]
Sub_TpCust=Sup_Pro6.groupby('Customer Name').sum().sort_values(by='Profit',ascending=False).head(10)
plt.barh(Sub_TpCust.index,Sub_TpCust.Profit,color ='y',label='Top 10 Profitable Customers')
plt.xlabel("Profit")
plt.ylabel("Customers")
plt.title('Top 10 Profitable Customers')
plt.legend()


# In[13]:


#g) scatter plot between profit and sales
plt.scatter(Sup_Store.Profit,Sup_Store.Sales,label ='Profit vs Sales',color ='r',s=100,marker='*')
plt.xlabel('Profit')
plt.ylabel('Sales')
plt.title(' Profit  vs Sales')
plt.legend()


# In[ ]:




