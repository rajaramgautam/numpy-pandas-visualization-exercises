#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


print(plt)


# In[7]:


x = list(range(150))
plt.plot(x)
plt.show()



# In[8]:


plt.plot(range(len(x)), x)
plt.show()


# In[11]:


plt.plot(x, c = 'green')
plt.xlim(-20, 200)
plt.ylim(-5, 160)
plt.show()


# In[13]:


plt.plot(x, c='blue')
plt.show()


# In[14]:


from random import randint

# Some random data
x1 = [randint(-5, 25) + n for n in range(150)]
x2 = [x + randint(-6, 6) for x in x1]

# we can use the alpha kwarg to define how transparent the color is
plt.plot(x1, c='green', alpha=0.6)
plt.plot(x2, c='red', alpha=0.4)
plt.show()


# In[17]:


plt.scatter(range(len(x1)), x1, s=5, c='red')
plt.scatter(range(len(x2)), x2, s=5, c='green')
plt.show()


# In[19]:


plt.scatter(range(len(x1)), x1, s=30, c='red')
plt.scatter(range(len(x2)), x2, s=10, c='green')
plt.title('A couple of random series')
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.show()


# In[24]:


x = list(range(-49, 50))
y = [n ** 2 for n in x]
plt.scatter(x, y)
plt.title('A Quadratic Distribution, $y = x^2$')
plt.xlabel('$x$')
plt.ylabel('$x^2$')
plt.show()


# In[25]:


x = [1, 2, 3.14, 4]
y = [n ** 2 for n in x]
plt.scatter(x, y)
plt.xticks([1, 2, 3.14, 4], ['one', 'two', '$\pi$', 'four'])
plt.show()


# In[35]:


import math

x = range(-4, 4)
y = [math.sin(n) for n in x]
plt.scatter(x, y, c = 'black', s = 20)
plt.plot(x, y, ls=':', c = 'green')
plt.title('An approximation of the sine function')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()


# In[42]:


x = range(1, 5)
y = x
plt.scatter(x, y , s = 100, c = 'green')
plt.yticks([1, 2, 3, 4], ['one', 'two', 'three', 'four'], rotation=45)
plt.xticks(rotation=45)
plt.show()


# In[52]:


import random

weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] * 2

x = range(14)
y = [random.randint(1, 10) for i in x]
plt.plot(x, y)
plt.xticks(x, weekdays, rotation=60)
plt.show()


# In[55]:


x = list(range(-4, 4))
x.append(3.14159)
y = [math.sin(n) for n in x]

plt.scatter(x, y)
plt.plot(x, y, ls=':')

plt.text(0.25, 0, '(0, 0)', fontsize=10, color='blue')
plt.text(1.2, 0.1, '($\pi$, sin($\pi$))', fontsize=14, color='firebrick')

plt.show()


# In[58]:


x = range(-3, 10)
y = [n * 2 for n in x]
z = [n / 2 for n in x]

plt.plot(x, y, c='orange')
plt.plot(x, z, c='green')

plt.annotate('Intersection', xy=(0, 0), xytext=(-3, 5),
             arrowprops={'facecolor': 'blue'})

plt.show()


# In[60]:


x = range(-4, 5)
sin_x = [math.sin(n) for n in x]
cos_x = [math.cos(n) for n in x]

plt.figure(figsize=(14, 6)) # (width, height)

plt.scatter(x, sin_x, c='blue')
plt.scatter(x, cos_x, c='orange')
plt.plot(x, sin_x, c='blue', label='$\sin(x)$')
plt.plot(x, cos_x, c='orange', label='$\cos(x)$')

plt.legend(loc='upper right')
plt.title('Approximate sin and cosine curves')
plt.xlabel('$x$')

plt.show()


# In[61]:


x = range(1, 10)
y = [3 * n + 5 for n in x]
plt.plot(x, y)
plt.savefig('my-figure')
plt.show()


# In[62]:


n_rows = 1
n_cols = 2

# some data to play with
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
z = [1, 2, 3, 4, 5]

# plot the first subplot
plt.subplot(n_rows, n_cols, 1)
plt.plot(x, y)
plt.title('x ~ y')

# the second subplot
plt.subplot(n_rows, n_cols, 2)
plt.plot(x, z)
plt.title('x ~ z')

plt.show()


# In[63]:


# some data to play with
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
z = [1, 2, 3, 4, 5]

# plot the first subplot
plt.subplot(121)
plt.plot(x, y)
plt.title('x ~ y')

# the second subplot
plt.subplot(122)
plt.plot(x, z)
plt.title('x ~ z')

plt.suptitle('Subplots Demo')

plt.show()


# # Histograms

# In[64]:


x = [1, 1, 2, 3, 3, 3, 4, 4, 5]

plt.hist(x)
plt.show()


# In[65]:


x = [1, 1, 2, 3, 3, 3, 4, 4, 5]

plt.hist(x, bins=[0, 1, 2, 3, 4, 5, 6])
plt.show()


# In[66]:


x = [1, 1, 2, 3, 3, 3, 4, 4, 5]

plt.figure(figsize=(16, 6))
plt.suptitle(f'x = {x}')

plt.subplot(131)
plt.hist(x, bins=[0, 1, 2, 3, 4, 5, 6])
plt.title('align="middle" (default)')

plt.subplot(132)
plt.hist(x, bins=[0, 1, 2, 3, 4, 5, 6], align='left')
plt.title('align="left"')

plt.subplot(133)
plt.hist(x, bins=[0, 1, 2, 3, 4, 5, 6], align='right')
plt.title('align="right"')

plt.show()


# In[67]:


x1 = [randint(1, 5) for _ in range(20)]
x2 = [randint(1, 5) for _ in range(20)]

plt.hist(x1, bins=[0, 1, 2, 3, 4, 5, 6], align='left', edgecolor='black', alpha=0.5, color='blue')
plt.hist(x2, bins=[0, 1, 2, 3, 4, 5, 6], align='left', edgecolor='black', alpha=0.5, color='blue')

plt.show()


# In[68]:


x1 = [randint(1, 5) for _ in range(20)]
x2 = [randint(1, 5) for _ in range(20)]

plt.hist(x1, bins=[1, 2, 3, 4, 5, 6], align='left', edgecolor='black', alpha=0.4, label='$x_1$')
plt.hist(x2, bins=[1, 2, 3, 4, 5, 6], align='left', edgecolor='black', alpha=0.4, label='$x_2$')
plt.legend()

plt.show()


# In[69]:


x1 = [randint(1, 5) for _ in range(20)]
x2 = [randint(1, 5) for _ in range(20)]

plt.hist((x1, x2), bins=[1, 2, 3, 4, 5, 6], align='left', edgecolor='black', alpha=0.6, label=['$x_1$', '$x_2$'])

plt.legend()
plt.show()


# In[70]:


plt.figure(figsize=(12, 8))
for i in range(1, 5):
    n = 10 ** i
    x1 = [randint(1, 6) for _ in range(n)]
    x2 = [randint(1, 6) for _ in range(n)]

    total = [x + y for x, y in zip(x1, x2)]

    plt.subplot(2, 2, i)
    plt.hist(total, bins=range(2, 14), align='left', color='white', edgecolor='black')
    plt.title(f'n = {n}')

plt.suptitle('Sum of 2 dice rolls')
plt.show()


# In[ ]:




