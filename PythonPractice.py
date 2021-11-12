#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[30]:


import numpy as np


# In[19]:


import os


# In[34]:


import matplotlib


# In[21]:


os.getcwd()


# In[27]:


df = pd.read_csv('C:/users/cbull/anaconda3/video_games.csv')


# In[29]:


df


# In[33]:


print (df.describe)


# In[35]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


# In[51]:


plt.scatter("Metrics.ReviewScore", "Length.MainStory.Median", marker = 'o')

