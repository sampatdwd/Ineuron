#!/usr/bin/env python
# coding: utf-8

# In[18]:


l=[10,20,30]
def task(x,y):
    return x+y

def myreduce(task, l):
    temp=None
    it = iter(l)
    if temp is None:
        value = next(it)
    else:
        value = intial
    for element in it:
        value = task(value, element)
    return value

    
myreduce(task,l)


# In[61]:


l=[10,20,25,35,45,30,40,50]
def task(x):
    if x%2==0:
        return x
    else:
        pass

def myfilter(task,l):
    it=iter(l)
    l1=[]
    for element in it:
        l1.append(task(element)) 
    return l1

myfilter(task,l)


# In[5]:


l=['A','C','A','D','G','I','L','D']
[i for i in l]


# In[16]:


l = ['x','y','z']
[ i*times for i in l for times in range(1,5)  ]


# In[25]:


l = ['x','y','z']
[ i*no for no in range(1,5) for i in l]


# In[37]:


l = [2,3,4]
[ [i+no] for no in range(0,3) for i in l]


# In[39]:


l = [2,3,4,5]
[ [i+no for no in range(0,4)] for i in l]


# In[5]:


l=[1,2,3]
[ (it,no) for no in l for it in l]


# In[34]:


def longestword(lst):
    lst=sorted(lst, key=len, reverse=True)
    return lst[0]

l=["Hello","Whatsapp","Facebook","LinkedIn","Twitter","ComputerScience"]    
print(longestword(l))
    


# In[15]:


class parent1:
    def __init__(self,s,sa,sb,sc):  #user defined lent and sides in this class
        self.s=s
        self.sa=sa
        self.sb=sb
        self.sc=sc
        
class child1:
    def area(parent1,*args):
        area= p.s*(p.s-p.sa)*(p.s-p.sb)*(p.s-p.sc) ** 0.5
        print(area)

a=int(input("Enter the length"))
b=int(input("Enter Side A"))
c=int(input("Enter Side B"))
d=int(input("Enter Side C"))

c = child1()
c.area()


# In[36]:


l=["Hello","Whatsapp","Facebook","LinkedIn","Twitter","ComputerScience"] 
def filterlongwords(l,n):
    sorted(l)
    for i in l:
               
        print(i)
        
#n=int(input("Enter an interger"))
filterlongwords(l,n)


# In[54]:


def filterlongword(item,number):
    l = []
    for i in range(len(item)):
        if len(item[i]) > number:
            l.append(item[i])
    return l

item = ["Hello","Whatsapp","Facebook","LinkedIn","Twitter","ComputerScience"]
number=int(input("Enter integer:"))
filterlongword(item,number)


# In[93]:


def lengthofwords(item):
    l=[]
    for i in item:
        l.append(len(i))
    print(l) 
        
            
            
item = ["Hello","Whatsapp","Facebook","LinkedIn","Twitter","ComputerScience"]
lengthofwords(item)


# In[100]:


def vowels(c):
    if c == 'a' and 'A':
        return 1
    elif c == 'e' and 'E':
        return 1
    elif c == 'i' and 'I':
        return 1
    elif c == 'o' and 'O': 
        return 1
    elif c == 'u' and 'U':
        return 1
    else:
        return 0
    

c=input("Enter a Character:")
vowels(c)


# In[ ]:




