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

# In[4]:


import pandas as pd
fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
fruits = pd.Series(fruits)
fruits


# In[5]:


fruits.size


# # 2. Output only the index from fruits.

# In[6]:


fruits.index


# # 3. Output only the values from fruits.

# In[7]:


fruits.values


# # 4. Confirm the data type of the values in fruits.

# In[17]:


fruits.values.dtype


# # 5. Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
# 

# In[18]:


fruits.head(n=5)


# In[19]:


fruits.head(n=3)


# In[20]:


fruits.sample(2)


# # 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.
# 

# In[21]:


fruits.describe()


# # 7. Run the code necessary to produce only the unique string values from fruits.

# In[22]:


fruits.unique()


# # 8. Determine how many times each unique string value occurs in fruits.

# In[23]:


fruits.value_counts()


# # 9. Determine the string value that occurs most frequently in fruits.

# In[24]:


fruits.value_counts().nlargest(n=1, keep = 'all')


# # 10. Determine the string value that occurs least frequently in fruits.

# In[25]:


fruits.value_counts().nsmallest(n=1, keep = 'all')


# # Exercises Part II
# 
# # Explore more attributes and methods while you continue to work with the fruits Series.
# 

# # 1. Capitalize all the string values in fruits.

# In[26]:


fruits.str.capitalize()


# # 2. Count the letter "a" in all the string values (use string vectorization).

# In[27]:


fruits.apply(lambda row: row.count('a'))


# In[28]:


fruits.str.count('a')


# # 3. Output the number of vowels in each and every string value.

# In[29]:


def count_vowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

fruits.apply(count_vowels)


# # 4. Write the code to get the longest string value from fruits.

# In[34]:


fruits[fruits.str.len().idxmax()]


# In[35]:


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

# In[36]:


def string_length(string):
    result = len(string)
    for item in string:
        if result >= 5:
            return result
fruits.apply(string_length) 


# In[38]:


fruits[fruits.str.len() > 5]


# # 6. Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
# 

# In[39]:


fruits[fruits.apply(lambda row: row.count('o')>=2)]


# # 7. Write the code to get only the string values containing the substring "berry".

# In[40]:


fruits[fruits.str.contains('berry')]


# # 8. Write the code to get only the string values containing the substring "apple".

# In[41]:


fruits[fruits.str.contains('apple')]


# # 9. Which string value contains the most vowels?

# In[42]:


fruits[fruits.apply(count_vowels).idxmax()]


# # Exercises Part III
# 
# 

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

# In[43]:


import pandas as pd
letters = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
letters = pd.Series(list(letters))
letters


# # 1. Which letter occurs the most frequently in the letters Series?

# In[45]:


letters.value_counts().idxmax()


# # 2. Which letter occurs the Least frequently?

# In[46]:


letters.value_counts().idxmin()


# # 3. How many vowels are in the Series?

# In[47]:


def count_vowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels


# In[48]:


letters.apply(count_vowels).sum()


# In[50]:


letters.str.lower().str.count('[aeiou]')


# In[51]:


letters.str.lower().str.count('[aeiou]').sum()


# # 4. How many consonants are in the Series?

# In[52]:


letters.value_counts().sum() - letters.apply(count_vowels).sum()


# # 5. Create a Series that has all of the same letters but uppercased.

# In[55]:


letters.str.upper()


# # 6 Create a bar plot of the frequencies of the 6 most commonly occuring letters.

# In[57]:


import matplotlib.pyplot as plt
letters.value_counts().head(6)


# In[63]:


letters.value_counts().head(6).plot(kind='barh', 
                                    color='green',                       
                                    width=.7)

plt.title('Most Repeated 6 Letters')



plt.show()


# # Use pandas to create a Series named numbers from the following list:
# 
# # ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
# 

# In[64]:


numbers =  ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

numbers = pd.Series(numbers)
numbers


# # 1. What is the data type of the numbers Series?

# In[66]:


numbers.dtype


# # 2.  How many elements are in the number Series?

# In[67]:


numbers.size


# # 3. Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.

# In[68]:


numbers = numbers.str.replace('$', '')
numbers = numbers.str.replace(',', '')
numbers


# # 4.Run the code to discover the maximum value from the Series.

# In[69]:


numbers = numbers.astype('float')
numbers


# In[70]:


numbers.max()


# # 5. Run the code to discover the minimum value from the Series.

# In[71]:


numbers.min()


# In[72]:


numbers


# # 6. What is the range of the values in the Series?

# In[73]:


range_values = max(numbers) - min(numbers)
range_values


# # 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
# 

# In[76]:


bin_data = pd.cut(numbers, bins = 4).value_counts()
bin_data


# # 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.

# In[80]:


plt.title('No. of distributions')
plt.hist(numbers, bins = 4)
plt.xlabel('Amount in 1000 dollars ')
plt.ylabel('Frequency or Repetition')
plt.show()


# # # Use pandas to create a Series named exam_scores from the following list:
# 
#     - [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]

# In[81]:


exam_scores = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
exam_scores = pd.Series(exam_scores)
exam_scores


# # 1. How many elements are in the exam_scores Series?

# In[82]:


exam_scores.size


# # 2. Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
# 

# In[83]:


exam_scores.min(), exam_scores.max(), exam_scores.mean(), exam_scores.median()


# # 3. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
# 

# In[85]:


plt.title('Exam Scores')
plt.hist(exam_scores)
plt.xlabel('Scores')
plt.ylabel('No of Students or Frequency')
plt.show()


# # 4. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
# 

# In[89]:


curved_grades = 100 - exam_scores.max()
curved_grades


# In[91]:


curved_scores = exam_scores + curved_grades
curved_scores


# # 5. Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
# 

# In[93]:


letter_grades = pd.cut(exam_scores, bins = 6, labels= ['A', 'B', 'C', 'D', 'E', 'F'])
letter_grades


# # 6 . Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
# 

# In[102]:



letter_grades.value_counts().sort_index().plot.bar(color='Green', width=0.7)
plt.title('Exam Grades')
plt.xlabel('Grades')
plt.ylabel('No of Students or Frequency')
plt.show()

