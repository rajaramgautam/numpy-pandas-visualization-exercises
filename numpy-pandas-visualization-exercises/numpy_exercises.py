#!/usr/bin/env python
# coding: utf-8

# # Exercises
# 
# # In your numpy-pandas-visualization-exercises repo, create a file named numpy_exercises.py for this exercise.
# 
# # Use the following code for the questions below:
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
# 
# 

# # 1. How many negative numbers are there?

# In[1]:


import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[2]:


a<0


# In[3]:


b = a[a<0]
b


# In[4]:


len(b)


# # 2. How many positive numbers are there?

# In[5]:


a>0


# In[6]:


c = a[a>0]
c


# In[7]:


len(c)


# # 3. How many even positive numbers are there?

# In[8]:


c%2 == 0


# In[9]:


d = c[c%2 == 0]
d


# In[10]:


len(d)


# # 4. If you were to add 3 to each data point, how many positive numbers would there be?

# In[11]:


a


# In[12]:


e=a+3
e


# In[13]:


f = e[e>0]
f


# In[14]:


len(f)


# # 5. If you squared each number, what would the new mean and standard deviation be?

# In[15]:


a


# In[16]:


a.mean()


# In[17]:


a.std()


# In[18]:


g=a**2
g


# In[19]:


g.mean()


# In[20]:


g.std()


# # 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

# In[21]:


a


# In[22]:


a.mean()


# In[23]:


b = a-3
b


# In[24]:


b.mean()


# # 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# 
# Z =(x−μ)/σ

# In[25]:


a


# In[26]:


m = a.mean() 
s = a.std()
m
s


# In[27]:


z_score = (a-m)/s
z_score


# # 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

# In[28]:


import numpy as np


# # Setup 1
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# # Use python's built in functionality/operators to determine the following:
# # Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
# 
# 

# In[29]:


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# In[30]:


sum_of_a = a.sum()
sum_of_a


# # Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# In[31]:


min_of_a = a.min()
min_of_a


# # Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

# In[32]:


max_of_a = a.max()
max_of_a


# # Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
# 
# 

# In[33]:


mean_of_a = a.mean()
mean_of_a


# # Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# In[34]:


product_of_a = np.product(a)
product_of_a


# # Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# In[35]:


squares_of_a = a**2
squares_of_a


# # Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# In[36]:


odds_in_a = a%2 != 0
odds_in_a
a[odds_in_a]


# # Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

# In[37]:


evens_in_a = a%2 == 0
evens_in_a
a[evens_in_a]


# # What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
# ## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
# b = [
#     [3, 4, 5],
#     [6, 7, 8]
# ]
# 
# 

# In[38]:


b = [
    [3, 4, 5],
    [6, 7, 8]
]
b= np.array([
    [3, 4, 5],
    [6, 7, 8]
])
b


# In[39]:


b.sum()


# In[40]:


b.min()


# In[41]:


b.max()


# In[42]:


b.mean()


# In[43]:


np.product(b)


# In[44]:


b**2


# In[45]:


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)


# In[46]:


sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
sum_of_b


# In[47]:


b.sum()


# In[48]:


# Exercise 2 - refactor the following to use numpy. 

min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) 


# In[49]:


b.min()


# In[50]:


min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])
min_of_b


# In[51]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.


# In[52]:


max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b


# In[53]:


b.max()


# In[54]:



# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))


# In[55]:


mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b


# In[56]:


b.mean()


# In[57]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number


# In[58]:


product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
product_of_b


# In[59]:


np.product(b)


# In[60]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)


# In[61]:


squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
squares_of_b


# In[62]:


b**2


# In[63]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)


# In[64]:


odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
odds_in_b


# In[65]:


b[b%2 != 0]


# In[66]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)


# In[67]:


evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
evens_in_b


# In[68]:


b[b%2 == 0]


# In[69]:


# Exercise 9 - print out the shape of the array b.


# In[70]:


print(b.shape)


# In[71]:


# Exercise 10 - transpose the array b.
b.transpose()


# In[72]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

np.reshape(b, (1,6))


# # Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

# In[73]:


np.reshape(b, (6,1))


# In[74]:


## Setup 3

c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] ])

c


# # HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# # Exercise 1 - Find the min, max, sum, and product of c.

# In[75]:


c.min(), c.max(), c.sum(), np.product(c)


# # Exercise 2 - Determine the standard deviation of c.

# In[76]:


c.std()


# # Exercise 3 - Determine the variance of c.

# In[77]:


c.var()


# # Exercise 4 - Print out the shape of the array c

# In[78]:


c.shape


# # Exercise 5 - Transpose c and print out transposed result.

# In[79]:


c.transpose()


# # Exercise 6 - Get the dot product of the array c with c.

# In[80]:


np.dot(c,c)


# # Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
# 

# In[81]:


c


# In[82]:


d =c.transpose()
d


# In[83]:


e = c*d
e


# In[84]:


e.sum()


# # Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
# 

# In[85]:


np.product(e)


# In[86]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])

d


# In[87]:


# Exercise 1 - Find the sine of all the numbers in d


# In[88]:


np.sin(d)


# In[89]:



# Exercise 2 - Find the cosine of all the numbers in d


# In[90]:


np.cos(d)


# In[91]:


# Exercise 3 - Find the tangent of all the numbers in d


# In[92]:


np.tan(d)


# In[93]:


# Exercise 4 - Find all the negative numbers in d


# In[94]:


d[d<0]


# In[95]:


# Exercise 5 - Find all the positive numbers in d


# In[96]:


d[d>0]


# In[97]:


# Exercise 6 - Return an array of only the unique numbers in d.


# In[98]:


np.unique(d)


# In[99]:


# Exercise 7 - Determine how many unique numbers there are in d.


# In[100]:


len(np.unique(d))


# In[101]:


# Exercise 8 - Print out the shape of d.


# In[102]:


d.shape


# In[103]:


# Exercise 9 - Transpose and then print out the shape of d.


# In[104]:


e = d.transpose()
e


# In[105]:


e.shape


# In[106]:


# Exercise 10 - Reshape d into an array of 9 x 2


# In[107]:


np.reshape(d, (9, 2))

