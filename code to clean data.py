#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Assuming 'data' is your dataset stored in a DataFrame
# Replace 'data.csv' with the actual file name if you're reading from a CSV file
data = pd.read_csv('airline_reviews.csv')

# Removing duplicate rows
data_no_duplicates = data.drop_duplicates()

# If you want to remove duplicates based on specific columns, you can specify them like this:
# data_no_duplicates = data.drop_duplicates(subset=['column1', 'column2'])

# Now 'data_no_duplicates' contains the dataset without duplicates


# In[3]:


data.head()


# In[ ]:




