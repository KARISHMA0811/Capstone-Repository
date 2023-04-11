#!/usr/bin/env python
# coding: utf-8

# ## Notebook 1
# 
# 
# 

# In[6]:


get_ipython().run_cell_magic('pyspark', '', "df = spark.read.load('abfss://capstonecontainer@capstonestoreacccount123.dfs.core.windows.net/projectdata.csv/3baf781b-271f-4501-8e3e-8eba21eddf7f.txt', \r\nformat='csv',header=True)\r\ndisplay(df.limit(10))\n")


# In[9]:


COUNT = df.groupBy('Category')
PRODUCT_COUNT=COUNT.count()
display(PRODUCT_COUNT)

