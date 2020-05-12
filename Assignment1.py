#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


for i in range(2000,3201):
    if (i%7==0) and not (i%5==0):
        print(i,end=',')


# In[52]:


fname=input("Enter First name")[::-1]
lname=input("Enter last name")[::-1]
print(lname,"",fname)


# In[53]:


import math
diameter=12
radius=diameter/2
volume=(4/3)*math.pi*radius**3
print(volume)


# In[4]:


l1=[]

a=input("Enter comma separated numbers:")
l1.append(a)
print (l1)


# In[103]:


str='*'
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print(" ")
for i in range(5,0,-1):
    for j in range(0, i - 1):
        print("*",end="")
    print(" ")
    


# In[104]:


word=input("Enter a word:")[::-1]
print(word)


# In[14]:


'{:>10}'.format('WE, THE PEOPLE OF INDIA,having solemnly resolved to constitute India into a SOVEREIGN! SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens')


# In[ ]:




