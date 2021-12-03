#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import re
import datetime as dt
import os
import glob


# In[6]:


os.chdir(r'C:\Users\ferralme\OneDrive - Vanderbilt\ODCapstone\OD_gold_trigger_files')


# In[7]:


file_extension = '.csv'


# In[8]:


all_filenames = [i for i in glob.glob(f"*{file_extension}")]


# In[32]:


print(all_filenames)


# In[33]:


gold = pd.concat([pd.read_csv(file, header = None, usecols =[26,27,28,30,31,37]) for file in all_filenames],ignore_index=True,sort=False,axis=0, join = 'outer')


# In[34]:


gold


# In[35]:


gold.columns=['date','time','mealperiod','microsid','location','mealsused']


# df[["col1", "col2", "col3"]] = df[["col1", "col2", "col3"]].apply(pd.to_datetime)

# In[36]:


gold['date']=pd.to_datetime(gold.date)


# In[37]:


gold.dropna()


# In[38]:


gold = gold[gold.mealperiod >=0]


# gold1.columns.nunique()

# In[39]:


gold_commons = gold[gold['location'].isin(['Commons1','Commons2'])]


# In[40]:


gold_commons


# In[41]:


gold_commons.to_excel(r'C:\Users\ferralme\nss-data-analytics\Capstone\gold_pbi_files\gold.xlsx', index = False)

