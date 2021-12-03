#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
import datetime as dt
import os
import glob


# Nov_4_Comm = pd.read_csv('../netmenu_files/Netmenu11.4.csv', encoding='latin-1')
# 

# In[6]:


os.chdir(r'C:\Users\ferralme\OneDrive - Vanderbilt\ODCapstone\OD_netmenu_trigger_files')


# In[7]:


file_extension = '.csv'


# In[8]:


all_filenames = [i for i in glob.glob(f"*{file_extension}")]


# In[9]:


print(all_filenames)


# In[11]:


netmenu = pd.concat([pd.read_csv(file, encoding='latin-1') for file in all_filenames],ignore_index=True)


# In[13]:


netmenu= netmenu.drop_duplicates()


# In[23]:


netmenu = netmenu[['AscTimePeriodName','ScheduleDate','Day','mealperiod','Name','AscServiceCourseName','SSServiceName','AscForecastUofMName','AscPreparedUofMName','AscServedUofMName','SSForecastAmount','SSForecastCost','SSPreparedAmount','SSPreparedCost','SSServedAmount','SSServedCost']]


# In[24]:


netmenu['ScheduleDate'] = netmenu['ScheduleDate'].map(lambda x: str(x)[:-4])


# In[25]:


netmenu['ScheduleDate']=pd.to_datetime(netmenu.ScheduleDate)


# In[26]:


netmenu[['Day','mealperiod']] = netmenu['Name'].str.split('-', n=1,expand=True)


# In[22]:


netmenu.to_excel(r'C:\Users\ferralme\nss-data-analytics\Capstone\netmenu_pbi_files\netmenu.xlsx', index = False)


# In[ ]:




