#!/usr/bin/env python
# coding: utf-8

# In[1]:


1.
counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")


# In[3]:


2.
print("the first 5 even no are:")
start, end = 4, 13
  
# iterating each number in list 
for num in range(start, end + 1): 
      
    # checking condition 
    if num % 2 == 0: 
        print(num, end = " ") 


# In[6]:


3.
print("the first 4 even no are:")
start, end = 4, 11
  
# iterating each number in list 
for num in range(start, end + 1): 
      
    # checking condition 
    if num % 2 == 0: 
        print(num, end = " ") 


# In[4]:


4.
str = input("Enter a string: ")

counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)


# In[5]:


5.
str = input("Enter the string : ")
total = 0
 
for i in str:
    total = total + 1
 
print("Total Number of Characters in this String = ", total)


# In[8]:


6.
var=input("Enter the string:")
ans=var[0:2]+var[-2:]
if(len(var)<2):
    print(ans)
else:
    print(ans)


# In[2]:


7.
n=input("Enter the string:")
firstchar=n[0]
newN=n.replace(firstchar,"$")
print(firstchar+newN[1: ])


# In[1]:


8.
x=input("Enter the string:")
y=input("Enter the string:")
print(y[0:1]+x[1: ], x[0:1]+y[1: ])


# In[ ]:





# In[ ]:




