
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[3]:


for roll in range(10):
    print(random.randrange(1, 7), end=' ')


# In[4]:


# fig04_01.py


# In[5]:


"""Roll a six-sided die 6,000,000 times."""
import random


# In[6]:


# face frequency counters
frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0


# In[9]:


#6,000,000 die rolls
for roll in range(6_000_000): # note underscore seperators
    face = random.randrange(1, 7)


# In[10]:


# increment appropriate face counter
if face == 1:
    frequency1 += 1
elif face == 2:
    frequency2 += 1
elif face == 3:
    frequency3 += 1
elif face == 4:
    frequency4 += 1
elif face == 5:
    frequency5 += 1
elif face == 6:
    frequency6 += 1


# In[13]:


print(f'Face{"Frequency":>13}')
print(f'{1:>4}{frequency1:>13}')
print(f'{2:>4}{frequency2:>13}')
print(f'{3:>4}{frequency3:>13}')
print(f'{4:>4}{frequency4:>13}')
print(f'{5:>4}{frequency5:>13}')
print(f'{6:>4}{frequency6:>13}')


# In[15]:


random.seed(32)


# In[16]:


for roll in range(10):
    print(random.randrange(1, 7), end=' ')


# In[18]:


for roll in range(10):
    print(random.randrange(1, 7), end=' ')


# In[19]:


random.seed(32)


# In[20]:


for roll in range(10):
    print(random.randrange(1, 7), end=' ')


# In[21]:


import random


# In[23]:


for i in range(20):
    print('H' if random.randrange(2) == 0 else 'T', end=' ')


# In[24]:


# fig04_01.py
"""Roll a six-sided die 600,000 times."""
import random


# In[25]:


# face frequency counters
frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0


# In[27]:


# 600,000 die rolls
for roll in range(600_000): # note underscore seperators
    face = random.randrange(1, 7)


# In[28]:


# increment appropriate face counter
if face == 1:
    frequency1 += 1
elif face == 2:
    frequency2 += 1
elif face == 3:
    frequency3 += 1
elif face == 4:
    frequency4 += 1
elif face == 5:
    frequency5 += 1
elif face == 6:
    frequency6 += 1


# In[36]:


print(f'Face{"Frequency":>13}')
print(f'{1:>4}{frequency1:>13}')
print(f'{2:>4}{frequency2:>13}')
print(f'{3:>4}{frequency3:>13}')
print(f'{4:>4}{frequency4:>13}')
print(f'{5:>4}{frequency5:>13}')
print(f'{6:>4}{frequency6:>13}')


# In[ ]:




