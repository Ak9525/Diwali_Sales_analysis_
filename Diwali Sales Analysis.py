#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv("Diwalisales.csv", encoding ="unicode_escape")
#to avoid encoding error, use "unicode_escape"


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.drop(['Status','unnamed1',] ,axis=1 ,inplace= True)


# In[7]:


df.info()


# In[8]:


pd.isnull(df)


# In[9]:


pd.isnull(df).sum()


# In[10]:


df.shape


# In[11]:


#drop null values
df.dropna(inplace=True)


# In[12]:


df.shape


# In[13]:


#initialize list of lists
data_test =[['madhav',11],['Gopi',15],['Keshav',],['Lalita',16]]

#create the pandas dataframe using list
df_test =pd.DataFrame(data_test, columns=['Name','Age'])

df_test


# In[14]:


df_test.dropna(inplace=True)


# In[15]:


df_test


# In[16]:


#change data type
df['Amount'] = df['Amount'].astype(int)


# In[17]:


df['Amount'].dtype


# In[18]:


df.columns


# In[19]:


#rename column
df.rename(columns={'Marital_Status':'Shaadi'})


# In[20]:


#describe() method returns description of the data in the dataframe (i.e. count,mean, etc)
df.describe()


# In[21]:


#use describe for specific column
df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis
# 
# 
# Gender

# In[22]:


df.columns


# In[24]:


ax =sns.countplot(x ='Gender', data= df)


# In[25]:


ax =sns.countplot(x ='Gender', data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[26]:


df.groupby(['Gender'], as_index=False,)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[27]:


sales_gen =df.groupby(['Gender'], as_index=False,)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Gender', y='Amount', data= sales_gen)


# from above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than man

# # Age

# In[28]:


ax =sns.countplot(x ='Age Group', hue= 'Gender', data= df)


# In[29]:


ax =sns.countplot(x ='Age Group', hue= 'Gender', data= df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


#total amount vs age group

sales_age =df.groupby(['Age Group'], as_index=False,)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Age Group', y='Amount', data= sales_age)


# From the above graphs we can see that most of the buyers are of age group between 26-35 years females

# # State

# In[42]:


sales_state =df.groupby(['State'], as_index=False,)['Orders'].sum().sort_values(by='Orders', ascending=False).head(5)

sns.barplot(x='State', y='Orders', data= sales_state)
sns.set(rc={'figure.figsize':(10,6)})


# In[54]:


sales_state =df.groupby(['State'], as_index=False,)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.barplot(x='State', y='Amount', data= sales_state)
sns.set(rc={'figure.figsize':(13,15)})


# From above graphs we can see that most of the orders and total sales/amount are from top 3 state respectively

# # Marital Status

# In[60]:


ax =sns.countplot(x ='Marital_Status',data= df)

sns.set(rc={'figure.figsize':(5,3)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[63]:


sales_state =df.groupby(['Marital_Status','Gender'], as_index=False,)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Marital_Status', y='Amount', hue='Gender',data= sales_state)
sns.set(rc={'figure.figsize':(5,5)})


# From above graphs we can see that most of the buyers are married (women)and they have high purchasing power

# # Occupation

# In[67]:


ax =sns.countplot(x ='Occupation',data= df)

sns.set(rc={'figure.figsize':(20,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[68]:


sales_state =df.groupby(['Occupation'], as_index=False,)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Occupation', y='Amount',data= sales_state)
sns.set(rc={'figure.figsize':(20,5)})


# From above graphs we can see that most of the buyers are working in IT Sector, Healthcare, and Aviation

# # Product Category

# In[77]:


ax =sns.countplot(x ='Product_Category',data= df)

sns.set(rc={'figure.figsize':(22,20)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[88]:


sales_state =df.groupby(['Product_Category'], as_index=False,)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.barplot(x='Product_Category', y='Amount',data= sales_state)
sns.set(rc={'figure.figsize':(18,18)})


# 
# From above graphs we can see that most of the sold products are from Food, Clothing, and Electronics devices.
# 

# In[89]:


sales_state =df.groupby(['Product_ID'], as_index=False,)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.barplot(x='Product_ID', y='Orders',data= sales_state)
sns.set(rc={'figure.figsize':(20,15)})


# In[91]:


#Top 10 most sold products (same thing as above)

fig1, ax1= plt.subplots(figsize=(15,8))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion
# 

# Married women age group 26-35 yrs from UP, MAHARASTRA, and KARNATAKA working in IT Sector, Healthcare and Aviation are more likely buy products from Food, Clothing and Electronics category.
# 
# 
# 
# 
# 
# Thank You.
