#!/usr/bin/env python
# coding: utf-8

# In[14]:


print(months[1])
print(months[2])


# In[18]:


#lists []
months = ['ccc','xcjcjc','cccjhh','xcjcjchkl','cnmbb','jj']
print(type(months))


# In[19]:


print(months[-1])


# In[1]:


# tuples ()
x = (2,5,6)
print(type(x))


# In[5]:


print(x[1])


# In[6]:


# sets {}
set_1 = {1,5,10,11}
print(type(set_1))


# In[18]:


# dictionary key and value {key:value}
dic_1 = {"a1":50,
       "a2":100,
       1:True}
print(type(dic_1))
#print(type(dic_10)
#print(dic_1["a1"])
#print(dic_1{1})


# In[19]:


print(dic_1['a1'])


# In[20]:


print(dic_1[1])


# In[21]:


dic_1["a3"] = 555
print(dic_1)


# In[22]:


print(True in dic_1)


# In[23]:


print(55 in dic_1)


# In[32]:


####### Lesson 4 Control flow 
# if condition 

q1 = input("Enter Q 1 : ") 
q2 = input("Enter Q2 : ")
#print(q1,q2)

if q2 > q1 :
    print("q1 is > q2")
elif q2 < q1 :
    print("q1 is < q2  ")
else :
    print("not found")


# In[47]:


q3 = input("Enter number : ")
if int(q3) % 2 == 0 :
    print(f"Q3 is even number = {q3}.")
else : 
    print(f'Q3 is odd number {q3} .')


# In[39]:


type(input("enter nym "))


# In[59]:


##Practice: Which Prize vid 4,5,6
points = int(input("Enter your points from 1 to 200 :  "))

if points>=1 and points<=50 :
    print("Congratulations! You won a woddon rapit !")
elif points>50 and points<=150 :
    print("Oh dear, no prize this time!")
elif points>150 and points<=180 :
    print("Congratulations! You won a wafer-thin mint!")
elif points>180 and points<=200 :
    print("Congratulations! You won a penguin !")
else :
    print(f"number {points} is not in range .")


# In[17]:


####### Lesson 4 Control flow 
#for loop
#for loop in data structure set , dictionary , list , string , tuples 
#for loop in list 
cities = ["cairo","mansoura","alex","monofia","hurgada"]
for city1 in cities:
    print(city1)

print("========================================")
for index in range(len(cities)):
    print(cities[index])


# In[14]:


## range functin  >> range(start 0,stop,step 1) all parameters ar integers 
print(list(range(4)))
print(list(range(2,6)))
print(list(range(1,10,2)))


# In[15]:


for num in range(4) :
    print(num)


# In[19]:


for x in "banana":
  print(x)


# In[23]:



#for i=0 and i<= 5:
 #   print(i++)
for i in range(0,5,1) :
    print(i)


# In[27]:


for i in range(5,0,-1) :
    print(i)


# In[30]:


#Practice: Multiples of 5
for i in range(5,35,5):
    print(i)
  


# In[32]:


sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for word in range(len(sentence)):
    print(sentence[word].title())


# In[33]:


print(list(range(0,-5)))


# In[34]:


######## Lesson 4 Control flow 
# for else
for x in range(6):
  print(x)
else:
  print("Finally finished!")


# In[35]:


card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  < 17:
    hand.append(card_deck.pop())
print(hand)    


# In[37]:


#while loops 
i1 = 1
while i1 < 6:
  print(i1)
  i1 += 1    


# In[38]:


#Zip and Enumerate lesson4
letters = ['a', 'b', 'c']
nums = [1, 2, 3]
print(list(zip(letters,nums)))


# In[39]:


for ope in zip(letters,nums):
    print(ope[0],ope[1])


# In[40]:


for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))


# In[46]:


letters1 = ['a', 'b', 'c', 'd', 'e']
for i,item in enumerate(letters1):
    print(i,item)


# In[49]:


# important note #####################################################################
dog1 = 12
print(f"dog is {dog1}")


# In[55]:


###### Lesson5 functions
def cyinder_volum(height,radious):
    pi = 3.14
    return height * pi * radious**2


print(cyinder_volum(10,3))
cyinder_volum(10,20)


# In[57]:


def printing_data() :
    print("hello world")
printing_data()    


# In[61]:


#Default Arguments
def square_area(h1,w1=50):
    return h1*w1
print(square_area(10,20))
print(square_area(10))
print(square_area(h1=20,w1=40))


# In[7]:


#variable scope 
#lesson5 functions 
egg_count = 0

# def buy_eggs():
#     egg_count += 12 # purchase a dozen eggs

# buy_eggs()
egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)
print(egg_count)


# In[8]:


str1 = 'Functions are important programming concepts.'

def print_fn():
    #str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()


# In[9]:


#lampda expression (small function)
#lesson5 functions 
x = lambda a : a + 10
print(x(5))


# In[11]:


double_num = lambda x : x*2
double_num(5)


# In[12]:


#multiple arguments
mul = lambda x,y : x*y
mul(10,50)


# In[1]:


how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)


# In[2]:


#lesson5 scripting 
#input from user
username = input("Enter username:")
print("Username is: " + username)


# In[3]:


idd = int(input("Enter id "))
print(idd*2)


# In[5]:


num = 30
x = eval('num+42')
print(x)


# In[8]:


#Handling Errors
#try except
try:
    c=int(input("Enter num :"))
except:
    print("invalid type")


# In[10]:


def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")

    return(num_each, leftovers)

party_planner(5,10)


# In[19]:


# read and write files 
#f = open('E:\Data Structure Course with Dr Walid Youssef\hello.txt','r')
#print(f.read())


# In[1]:


#lesson 6 scripting 
#importing standard libraries modules
import math
print(math.factorial(4))


# In[7]:


import statistics as st
l1 = [1,5,6,3,4,8,5]
print(st.mean(l1))
print(st.mode(l1))
print(st.median(l1))
print(st.median_low(l1))
print(st.median_high(l1))


# In[8]:


#lesson 7 final lesson in introduction to python programming language 
#generators and iterators 
#[Optional] Iterators and Generators
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1
for x in my_range(5):
    print(x)        

