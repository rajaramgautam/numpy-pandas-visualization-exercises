#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Let's make a function that takes in a database name as a string
# this function also performs our imports from env
def get_db_url(db_name):
    from env import user, host, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


# In[3]:


import pandas as pd
import numpy as py


# In[4]:


sql = """
    SELECT * from employees limit 3000
"""


# In[5]:


# Called the "Connection string" b/c it has all the info to connect
url = get_db_url("employees")

df = pd.read_sql(sql, url)
df


# In[ ]:





# In[ ]:


# Read a CSV from a webpage hosting a CSV
url = "https://gist.githubusercontent.com/ryanorsinger/19bc7eccd6279661bd13307026628ace/raw/e4b5d6787015a4782f96cad6d1d62a8bdbac54c7/lemonade.csv"
lemonade = pd.read_csv(url)
lemonade.head()


# In[ ]:


# JSON is short for JavaScript Object Notation
# Cool part is JSON is automatically valid python syntax for: a dictionary or a list of dictionaries
quotes = pd.read_json("https://aphorisms.glitch.me/api/all")
quotes.head()


# # Exercises I
# 
# # Run python -m pip install pymysql from your terminal to install pymysql.
# 
# # Create a notebook or python script named advanced_dataframes to do your work in for these exercises.
# 
# 
# 
# 
# 

# # 1. Run python -m pip install pymysql from your terminal to install the mysql client (any folder is fine)

# In[58]:


# pymysql package installed


# # 2. cd into your exercises folder for this module and run echo env.py >> .gitignore

# In[ ]:


# task completed


# # 3. Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url connection string formatted like in the example at the start of this lesson.
# 

# In[59]:


# Let's make a function that takes in a database name as a string
# this function also performs our imports from env
def get_db_url(db_name):
    from env import user, host, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


# # 4. Use your function to obtain a connection to the employees database.

# In[60]:


def get_db_url(employees):
    from env import user, host, password
    return f'mysql+pymysql://{user}:{password}@{host}/{employees}'
    
    


# In[61]:


url = get_db_url("employees")

df = pd.read_sql(sql, url)
df


# # 5. Once you have successfully run a query:
# 
# #   a. Intentionally make a typo in the database url. What kind of error message do you see?
# 
# #   b. Intentionally make an error in your SQL query. What does the error message look like?
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[1]:


5
 i. ConnectionRefusedError
ii. OperationalError: (2003, "Can't connect to MySQL server on '157.230.209.170' ([Errno 61] Connection refused)")

The above exception was the direct cause of the following exception:


# In[ ]:


5 b. ProgrammingError: (pymysql.err.ProgrammingError) (1146, "Table 'employees.employee' doesn't exist")
[SQL: 
    SELECT * from employee limit 3000
]
(Background on this error at: https://sqlalche.me/e/14/f405)


# # 6. Read the employees and titles tables into two separate DataFrames.

# In[6]:


sql = """
    SELECT * from employees limit 3000
"""


# In[16]:


sql1 ="""
SELECT * FROM titles
"""


# In[17]:


url = get_db_url("employees")

df = pd.read_sql(sql, url)
df


# In[18]:


url = get_db_url("employees")

new_df = pd.read_sql(sql1, url)
new_df


# # 7. How many rows and columns do you have in each DataFrame? Is that what you expected?

# In[19]:


df.shape


# In[21]:


# Row 
df.shape[0]


# In[22]:


# Columns
df.shape[1]


# In[20]:


new_df.shape


# In[24]:


# Row
new_df.shape[0]


# In[25]:


# Columns
new_df.shape[1]


# # 8. Display the summary statistics for each DataFrame.

# In[57]:


new_df.describe


# In[29]:


df.info


# # 9. How many unique titles are in the titles DataFrame?

# In[37]:


len(new_df.title.unique())


# # 10. What is the oldest date in the to_date column?

# In[51]:


new_df.to_date.sort_values(ascending = False)


# In[52]:


new_df.to_date.sort_values(ascending = False).head(1)


# In[66]:


new_df[new_df.to_date != new_df.to_date.max()].to_date.min()


# # 11. What is the most recent date in the to_date column?

# In[62]:


new_df[new_df.to_date != new_df.to_date.max()].to_date.max()

