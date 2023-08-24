#!/usr/bin/env python
# coding: utf-8

# # Sales Analysis with Pandas

# ## Objective
# After an initial general inspection of the data we can start thinking about some questions we'd want to answer:
# 
# - What is the general sales trend?
# - What are the top 10 products by sales?
# - Which are the most selling products?
# - Which are the most profitable categories and sub-categories?

# ### Importing necessary Libraries

# In[1]:


# Data manipulation
import pandas as pd

# Data visualization
import matplotlib.pyplot as plt

import seaborn as sns


# ### Importing the Dataset

# In[2]:


df = pd.read_excel('superstore_sales.xlsx')


# ### Checking Data

# In[3]:


# checking first 5 rows of the Dataset
df.head(5)


# In[4]:


# checking last 5 rows of the Dataset
df.tail(5)


# In[13]:


# summary of the dataset
df.info()


# In[7]:


# looking for duplicates
duplicate = df[df.duplicated()]
 
print("Duplicate Rows :")
duplicate


# In[8]:


# Getting a descriptive statistic summary
df.describe()


# ## Analysis

# ### What is the general/overall sales trend?

# In[16]:


df['order_date'].min()


# In[17]:


df['order_date'].max()


# In[19]:


# getting only month and year
df['month_year'] = df['order_date'].apply(lambda x: x.strftime('%Y-%m'))


# In[25]:


# Grouping by Month-Year
df_trend = df.groupby('month_year').sum()['sales'].reset_index()


# In[30]:


plt.figure(figsize=(15, 6))
plt.plot(df_trend['month_year'], df_trend['sales'])
plt.xticks(rotation=45, size=8)    
plt.show


# Sales trend is growing, sales are rising. We can also notice that sales gets higher at the end of the year.

# ### What are the top 10 products by sales?

# In[34]:


# Grouping product name
prod_sales =  pd.DataFrame(df.groupby('product_name').sum()['sales'])


# In[36]:


# Sorting descending
prod_sales = prod_sales.sort_values('sales', ascending=False)


# #### Top 10 products

# In[37]:


prod_sales[:10]


# ## Which are the most selling products?

# In[38]:


# Grouping
most_sell_prod = pd.DataFrame(df.groupby('product_name').sum()['quantity'])


# In[40]:


# Sorting descending
most_sell_prod = most_sell_prod.sort_values('quantity', ascending=False)


# #### Most selling products

# In[42]:


most_sell_prod[:15]


# ### Which are the most profitable categories and sub-categories?

# In[46]:


cat_profit = pd.DataFrame(df.groupby(['category', 'sub_category']).sum()['profit'])


# In[48]:


cat_profit.sort_values(['category', 'profit'], ascending=False)

