#!/usr/bin/env python
# coding: utf-8

# In[2]:


1.
def add_num(a,b):
    multiply=a*b;
    return multiply; 

num1=int(input("Enter the first no: "))
num2=int(input("Enter the second no: "))

print("The product is",add_num(num1,num2))


# In[4]:


2.
def sum_num(a,b):
    add=a+b;
    return add;

num1=int(input("Enter the first no: "))
num2=int(input("Enter the second no: "))

print("The solution is",sum_num(num1,num2))


# In[5]:


3.
def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)

num = int(input("Enter a Number: "))

if num < 0:
    print("Factorial cannot be found for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", num, "is: ", factorial(num))


# In[6]:


4.
def gen_seq(length):
    if(length <= 1):
        return length
    else:
        return (gen_seq(length-1) + gen_seq(length-2))

length = int(input("Enter number of terms:"))

print("Fibonacci sequence using Recursion :")
for iter in range(length):
    print(gen_seq(iter))


# In[7]:


6.
def compute_hcf(x, y):
    
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input("enter the value of num1: "))
num2 = int(input("enter the value of num2: "))

print("The H.C.F. is", compute_hcf(num1, num2))


# In[8]:


7.
c = (input(" Please Enter the Alphabet : ")) 
print("The ASCII value of '" + c + "' is", ord(c))


# In[1]:


8.
abs(-7)
any((1,0,0))
bin(7)


# In[2]:


9.
import datetime 
from datetime import date  
print ("Present date is : ",end="") 
print (date.today())


# In[10]:


10.
def printme(str):
   "This prints a passed string into this function"
   print (str)
   return;

printme("I'm first call to user defined function!")
printme("Again second call to the same function")


# In[17]:


11.
def student(firstname, lastname):  
     print(firstname, lastname)  
    
                      
student(firstname ='Pooja', lastname ='Kashyap')     
student(lastname ='Kashyap', firstname ='Pooja')


# In[15]:


12. 
def myFun(x, y=50): 
    print("x: ", x) 
    print("y: ", y) 
   
myFun(10)


# In[18]:


13. 
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
    
myFun('Hello', 'My', 'name', 'is','Pooja')


# In[ ]:




