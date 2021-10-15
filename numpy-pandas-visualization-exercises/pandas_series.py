#!/usr/bin/env python
# coding: utf-8

# # Exercises Part I
# 
# # Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.
# 

# # Use pandas to create a Series named fruits from the following list:
# 
# 
# #    ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
# # Use Series attributes and methods to explore your fruits Series.

# In[6]:


import pandas as pd
fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
fruits = pd.Series(fruits)
fruits


# # 1. Determine the number of elements in fruits.

# In[7]:


fruits.size


# # 2. Output only the index from fruits.

# In[11]:


fruits.index


# # 3. Output only the values from fruits.

# In[12]:


fruits.values


# # 4. Confirm the data type of the values in fruits.

# In[23]:


fruits.dtype


# # 5. Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
# 

# In[20]:


fruits.head(n=5)


# In[21]:


fruits.head(n=3)


# In[24]:


fruits.sample(2)


# # 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.
# 

# In[22]:


fruits.describe()


# # 7. Run the code necessary to produce only the unique string values from fruits.

# In[25]:


fruits.unique()


# # 8. Determine how many times each unique string value occurs in fruits.

# In[26]:


fruits.value_counts()


# # 9. Determine the string value that occurs most frequently in fruits.

# In[28]:


fruits.value_counts().nlargest(n=1, keep = 'all')


# # 10. Determine the string value that occurs least frequently in fruits.

# In[27]:


fruits.value_counts().nsmallest(n=1, keep = 'all')


# # Exercises Part II
# 
# # Explore more attributes and methods while you continue to work with the fruits Series.
# 

# # 1. Capitalize all the string values in fruits.

# In[36]:


fruits.str.capitalize()


# # 2. Count the letter "a" in all the string values (use string vectorization).

# In[39]:


fruits.apply(lambda row: row.count('a'))


# In[45]:


fruits.str.count('a')


# # 3. Output the number of vowels in each and every string value.

# In[71]:


def count_vowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

fruits.apply(count_vowels)


# # 4. Write the code to get the longest string value from fruits.

# In[108]:


fruits[fruits.str.len().idxmax()]


# In[82]:


def string_long(string):
    result = len(string)
    for item in string:
        if result == max(string):
            return result

def string_len(string):
    result = len(string)
    return result

b = fruits.apply(string_len)
max(b)


# # 5. Write the code to get the string values with 5 or more letters in the name.

# In[76]:


def string_length(string):
    result = len(string)
    for item in string:
        if result >= 5:
            return result
fruits.apply(string_length) 


# In[98]:


fruits[fruits.str.len() > 5]


# # 6. Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
# 

# In[85]:


fruits[fruits.apply(lambda row: row.count('o')>=2)]


# # 7. Write the code to get only the string values containing the substring "berry".

# In[100]:


fruits[fruits.str.contains('berry')]


# # 8. Write the code to get only the string values containing the substring "apple".

# In[101]:


fruits[fruits.str.contains('apple')]


# # 9. Which string value contains the most vowels?

# In[105]:


fruits[fruits.apply(count_vowels).idxmax()]


# In[ ]:


Exercises Part III


Use pandas to create a Series named numbers from the following list:

    ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
get_ipython().set_next_input('What is the data type of the numbers Series');get_ipython().run_line_magic('pinfo', 'Series')

get_ipython().set_next_input('How many elements are in the number Series');get_ipython().run_line_magic('pinfo', 'Series')

Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.

Run the code to discover the maximum value from the Series.

Run the code to discover the minimum value from the Series.

get_ipython().set_next_input('What is the range of the values in the Series');get_ipython().run_line_magic('pinfo', 'Series')

Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.

Plot the binned data in a meaningful way. Be sure to include a title and axis labels.

Use pandas to create a Series named exam_scores from the following list:


    [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
get_ipython().set_next_input('How many elements are in the exam_scores Series');get_ipython().run_line_magic('pinfo', 'Series')

Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.

Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.

Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.

Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.

More Practice

Revisit the exercises from https://gist.github.com/ryanorsinger/f7d7c1dd6a328730c04f3dc5c5c69f3a.

After you complete each set of Series exercises, use any extra time you have to pursue the challenge below. You can work on these in the same notebook or file as the Series exercises or create a new practice notebook you can work in a little every day to keep your python and pandas skills sharp by trying to solve problems in multiple ways. These are not a part of the Series exercises grade, so don't worry if it takes you days or weeks to meet the challenge.

Challenge yourself to be able to...

solve each using vanilla python.

solve each using list comprehensions.

solve each by using a pandas Series for the data structure instead of lists and using vectorized operations instead of loops and list comprehensions.


# # Use pandas to create a Series named letters from the following string:
# 
# 
#     'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
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
# 

# # 1. Which letter occurs the most frequently in the letters Series?

# In[ ]:


pd.cut(x, bins, labels=[])


# # 2. Which letter occurs the Least frequently?

# # 3. How many vowels are in the Series?

# # 4. How many consonants are in the Series?

# # 5. Create a Series that has all of the same letters but uppercased.

# # 6 Create a bar plot of the frequencies of the 6 most commonly occuring letters.

# In[ ]:




