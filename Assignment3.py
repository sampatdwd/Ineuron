#!/usr/bin/env python
# coding: utf-8

# In[11]:


try:
    def check_error(n):
        a=0
        div=n/a
        return div
 
    check_error(5)
except Exception as e:
    print(e)
    


# In[18]:


subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
for i in subjects:
    for j in verbs:
        for k in objects:
            print(i,j,k)


# In[4]:


import numpy as np
x = np.array([1, 2, 3, 5])
N=3
np.column_stack([x**(N-1-i) for i in range(N)])


# In[ ]:





# In[ ]:




