
#!/usr/bin/env python
# coding: utf-8

# In[1]:


maximum(12, 27, 36)


# In[2]:


def maximum(value1, value2, value3):
    """Return the maximum of three values"""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value


# In[3]:


maximum(12, 27, 36)


# In[5]:


maximum(12.3, 45.6, 9.7)


# In[6]:


maximum('yellow', 'red', 'orange')


# In[7]:


maximum(13.5, -3, 7)


# In[8]:


maximum(13.5, hello, 7)


# In[9]:


max('yellow', 'red', 'orange', 'blue', 'green')


# In[10]:


min(15, 9, 27, 15)


# In[11]:


max([14,27,5,3])


# In[12]:


min('orange')


# In[ ]:




