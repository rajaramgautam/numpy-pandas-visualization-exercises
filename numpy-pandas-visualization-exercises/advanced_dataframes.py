#!/usr/bin/env python
# coding: utf-8

# In[195]:


# Let's make a function that takes in a database name as a string
# this function also performs our imports from env
def get_db_url(db_name):
    from env import user, host, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


# In[196]:


import pandas as pd
import numpy as py


# In[197]:


sql = """
    SELECT * from employees limit 3000
"""


# In[198]:


# Called the "Connection string" b/c it has all the info to connect
url = get_db_url("employees")

df = pd.read_sql(sql, url)
df


# In[ ]:





# In[199]:


# Read a CSV from a webpage hosting a CSV
url = "https://gist.githubusercontent.com/ryanorsinger/19bc7eccd6279661bd13307026628ace/raw/e4b5d6787015a4782f96cad6d1d62a8bdbac54c7/lemonade.csv"
lemonade = pd.read_csv(url)
lemonade.head()


# In[200]:


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


# # Exercises II
# 
# # 1. Copy the users and roles DataFrames from the examples above.

# In[94]:


# Create the users DataFrame.
import numpy as np
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users


# In[95]:


# Create the roles DataFrame

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles


# # 2. What is the result of using a right join on the DataFrames?

# In[96]:


users.merge(roles, how='right', on=None, left_on=None, right_on=None, left_index=False, right_index=False, indicator=False)


# # 3. What is the result of using an outer join on the DataFrames?

# In[97]:


users.merge(roles, how='outer', on=None, left_on=None, right_on=None, left_index=False, right_index=False, indicator=False)


# # 4. What happens if you drop the foreign keys from the DataFrames and try to merge them?
# 

# In[98]:


users.drop(columns = ['role_id'])


# In[99]:


users.merge(roles, how='left', on=None, left_on=None, right_on=None, left_index=False, right_index=False, indicator=False)


# In[100]:


users.merge(roles, how='right', on=None, left_on=None, right_on=None, left_index=False, right_index=False, indicator=False)


# In[101]:


users.merge(roles, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, indicator=False)


# In[102]:


users.merge(roles, how='outer', on=None, left_on=None, right_on=None, left_index=False, right_index=False, indicator=False)


# # 5. Load the mpg dataset from PyDataset.

# In[89]:


from pydataset import data
data('mpg', show_doc=True)
mpg = data('mpg')


# # 6. Output and read the documentation for the mpg dataset.

# In[103]:


data('mpg', show_doc=True)


# # 7. How many rows and columns are in the dataset?

# In[105]:


mpg.shape


# In[106]:


mpg.shape[0]


# In[107]:


mpg.shape[1]


# # 8. Check out your column names and perform any cleanup you may want on them.

# In[114]:


mpg.head(30)


# # 9. Display the summary statistics for the dataset.

# In[109]:


mpg.describe()


# # 10. How many different manufacturers are there?

# In[126]:


mpg.groupby('manufacturer').describe()


# In[127]:


mpg.groupby('manufacturer').describe().shape[0]


# # 11. How many different models are there?

# In[128]:


mpg.groupby('model').describe().shape[0]


# # 12. Create a column named mileage_difference like you did in the DataFrames exercises; this column should contain the difference between highway and city mileage for each car.
# 

# In[130]:


mileage_difference = mpg.hwy - mpg.cty
mpg['mileage_difference'] = mpg.hwy - mpg.cty
mpg


# # 13. Create a column named average_mileage like you did in the DataFrames exercises; this is the mean of the city and highway mileage.
# 

# In[131]:


average_mileage = (mpg.cty + mpg.hwy)/2
mpg['average_mileage'] = (mpg.cty + mpg.hwy)/2
mpg['average_mileage']
mpg


# # 14. Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.
# 

# In[182]:


is_automatic = mpg.trans.str.contains('auto')
#is_automatic
# mpg[mpg.trans.str.contains('auto')]

mpg['is_automatic'] = mpg.trans.str.contains('auto')
mpg


# # 15. Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
# 

# In[190]:





# In[169]:


mpg[mpg.average_mileage == mpg.average_mileage.max()]


# In[ ]:





# In[135]:


mpg.max()


# # 16. Do automatic or manual cars have better miles per gallon?

# In[170]:


mpg.groupby('is_automatic')


# In[183]:


mpg.groupby('is_automatic').describe()


# # Exercises III
# 

# # 1. Use your get_db_url function to help you explore the data from the chipotle database.

# In[207]:


import pymysql
sql2 = """
select * from orders

"""
url2 = get_db_url("chipotle")

chip_df = pd.read_sql(sql2, url2)
chip_df


# # 2. What is the total price for each order?

# In[208]:


chip_df.groupby('order_id')


# In[222]:


price = chip_df.item_price.str.replace('$', '').astype(float)
#is_automatic
# mpg[mpg.trans.str.contains('auto')]

chip_df['price'] = chip_df.item_price.str.replace('$', '').astype(float)
chip_df


# In[223]:


chip_df.groupby('order_id')


# In[224]:


chip_df.groupby('order_id').price.sum()


# # 3. What are the most popular 3 items?

# In[237]:


chip_df.groupby('item_name').count().sort_values('quantity', ascending=False).head(3)


# # 4. Which item has produced the most revenue?

# In[239]:


price_total = chip_df.quantity * chip_df.price
#is_automatic
# mpg[mpg.trans.str.contains('auto')]

chip_df['price_total'] = chip_df.quantity * chip_df.price
chip_df


# In[243]:


# chip_df.price_total.idxmax()
chip_df[chip_df.price_total == chip_df.price_total.max()]


# # 5. Join the employees and titles DataFrames together.

# In[275]:


sql3 = """
select * from employees

"""
url3 = get_db_url("employees")

emp_df = pd.read_sql(sql3, url3)
emp_df


# In[276]:


sql4 = """
select * from titles

"""
url4 = get_db_url("employees")

title_df = pd.read_sql(sql4, url4)
title_df


# In[279]:



join_emp = emp_df.merge(title_df, left_on='emp_no', right_on ='emp_no', how='inner', indicator=True)

join_emp


# # 6. For each title, find the hire date of the employee that was hired most recently with that title.

# In[281]:


join_emp.groupby('title').from_date.max()


# In[266]:


sql4 = """
select t.title, max(t.from_date) as recent_h_date from employees as e
join titles as t
on e.emp_no = t.emp_no
group by t.title  

"""
url4 = get_db_url("employees")

title_df = pd.read_sql(sql4, url4)
title_df


# In[253]:


emp_df.merge(title_df, left_on='emp_no', right_on='emp_no', how='inner', indicator=True).groupby(title_df.title)


# # 7. Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas code to perform the manipulations.)

# In[285]:



sql5 = """
select d.dept_name, t.title from departments as d
join dept_emp as de on de.dept_no = d.dept_no
join titles as t on t.emp_no = de.emp_no
where t.to_date > curdate()

"""
url5 = get_db_url("employees")

new_df = pd.read_sql(sql5, url5)
new_df


# In[286]:


pd.crosstab(new_df.dept_name, new_df.title)

