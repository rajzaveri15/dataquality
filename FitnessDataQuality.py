#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install great_expectations')


# In[6]:


import great_expectations as ge
df = ge.read_csv('C:/Users/rajza/Documents/Portfolio Projects/Assessing  Data Quality/activities.csv')


# In[10]:


df.head()


# In[11]:


# Is Activity ID unique 

df.expect_column_values_to_be_unique(column="Activity ID")


# In[12]:


# Is the activity type one of the following?
# Bike Hike Walk Run 
activities = ['Run', 'Hike', 'Walk','Bike']
df.expect_column_values_to_be_in_set('Activity Type',
        value_set = activities)


# In[14]:


df.expect_column_values_to_be_between('Max Speed',0,12)


# In[ ]:




