#!/usr/bin/env python
# coding: utf-8

# # Data Collections 2 (Dictionaries, Sets) and Importing Modules

# ## Tasks Today:
# 
# 1) Dictionary <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring (key, value) <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Accessing Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; ------ Exercise #1 - Print the eye color of each person in a double nested dict <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Adding New Pairs <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Modifying Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Removing Key, Value Pairs <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) Looping a Dictionary <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Looping Only Keys <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Looping Only Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; ------ Exercise #2 - Create a Function that Prints All Key Value Pairs within a print .format()  <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) sorted() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Lists with Dictionaries <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; k) Dictionaries with Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; l) Dictionaries with Dictionaries <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; ------ Exercise #3 - Write a Function that asks someone's name and address, and then stores that into a dictionary, which prints all names and addresses after they're done putting information in...  <br>
# 2) Dictionaries vs. Lists (over time)<br>
# 3) Set <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) .add() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) .remove() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) .union() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) .intersection() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) .difference() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Frozen Set <br>
# 4) Modules <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Importing Entire Modules <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Importing Methods Only <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Using the 'as' Keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Creating a Module <br>
# 5) Exercises <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Build a Shopping Cart <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Create Your Own Module <br>

# ## Dictionary <br>
# <p>A collection of data with 'key:value' pairs. Dictionaries are ordered as of Python 3.6</p>

# ##### Declaring (key, value)

# In[13]:


#keys should be unique
#can use numbers or strings as keys

dict_1 = {}

#OR

dict_2 = dict()

#with data

dict_3 = {
    'dave' : '225 main street',
    'sean' : '222 turtle crossing'
     }
print(dict_3)


# ##### Accessing Values

# In[14]:


#dict{key}
# ^ this returns the value

dict_3['dave']


# ## In-Class Exercise #1 - Print a formatted statement from the dictionary below <br>
# <p>The output should be '2018 Chevrolet Silverado'</p>

# In[68]:


truck = {
    'year': 2018,
    'make': 'Chevrolet',
    'model': 'Silverado',
}

print('{0} {1} {2}'.format(truck['year'], truck['make'], truck['model']))


# ##### Adding New Pairs

# In[16]:


# dict{key}= value
dict_3['bob']= 'from ohio'

dict_3


# ##### Modifying Values

# In[17]:


# dict{key}= value
dict_3['bob']='now from nashville'
dict_3


# ##### Removing Key, Value Pairs

# In[19]:


# del_dict("key")

del dict_3['bob']
dict_3


# ##### Looping a Dictionary

# In[21]:


# .items()
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)

for key, value in dict_3.items():
    print(key,value)


# ##### Looping Only Keys

# In[23]:


# .keys()
for key in dict_3.keys():
    print(key)


# ##### Looping Only Values

# In[25]:


# .values()
for value in dict_3.values():
    print(value)


# ## In-Class Exercise #2 - Create a Function that Prints All Key Value Pairs within a print .format() <br>
# <p><b>Output should be:</b><br>
# Max has blue eyes<br>
# Lilly has brown eyes<br>
# Barney has blue eyes<br>
# etc.
# </p>

# In[71]:


# use the dict below

people = {
    'Max': 'blue',
    'Lilly': 'brown',
    'Barney': 'blue',
    'Larney': 'brown',
    'Ted': 'purple'
}

def eyeFunc(p):
    for key in people:
        print('{0} has {1} eyes'.format(key, p[key]))
        
eyeFunc(people)


# ##### sorted()

# In[29]:


# sorts variables in order
# sorted(dict.values()) or dict.keys() or dict.items()

print(sorted(people.items()))
print(sorted(people.keys()))
print(sorted(people.values()))

new_variable = sorted(people.values())
print(new_variable)


# ##### List with Dictionaries

# In[32]:


names = ['dave', 'randy', 'greg', {"random_guy": 'robert', 'random_girl': 'baraba'}]
print(names[3]['random_girl'])

#get all the keys from a nested dict in a list
for keys in names[3].keys():
    print(keys)


# ##### Dictionaries with Lists

# In[34]:


# be careful when using numbers as keys in dictionaries, don't confuse them with indexes

rando_data = {
    'list1':[54,7,11], 
    '2': ['smith', 'iphone', 'hydro flask'], 
}

for key in rando_data['2']:
    print(key)


# ##### Dictionaries with Dictionaries

# In[35]:


# to get values, must traverse through keys
food_dict ={
    'ice cream':{
        "CHO": 2.99, 
        "VA": 3.99, 
        "OR":5.99,
        "PB": 6.99
    }
}

print(food_dict['ice cream']['PB'])


# ## Dictionaries vs. Lists (over time) Example of RUNTIME
# ### When inputting values in a Dictionary vs List

# In[ ]:


import time


# generate fake dictionary
d = {}

for i in range(10000000):
    d[i] = 'value'
    

# generate fake list
big_list = [x for x in range(10000000)]


# In[ ]:


# tracking time for dictionary
start_time = time.time()

print(d[9999999])

end_time = time.time() - start_time

print('Elapsed time for dictionary: {}'.format(end_time))


# tracking time for list
start_time = time.time()

for i in range(len(big_list)):
    if i == 9999999:
        print(i)

end_time = time.time() - start_time

print('Elapsed time for list: {}'.format(end_time))


# ## Exercise #3 - Write a Function that asks someone's name and address, and then stores that into a dictionary, and continues to do so until they choose to 'quit'. Once they quit, the program should print all names and addresses. <br>
# <p>
# <b>Proper steps:</b><br>
# step 1: write a function that takes in information and stores it in a dictionary<br>
# step 2: define an empty dictionary to work with<br>
# step 3: create our loop, which asks the user for information until they quit<br>
# step 4: ask for the information, and store it into variables<br>
# step 5: check if the user types quit<br>
# step 5a: print out all information<br>
# step 5b: break out of the loop<br>
# step 6: if they didn't quit, add the information to the dictionary<br>
# step 7: invoke the function by calling it
# </p>

# In[ ]:


from IPython.display import clear_output


# ## Set <br>
# <p>A Set is an unordered collection data type that is iterable (loop), mutable, and has no duplicate elements.<br>Major advantage is that it is highly optimized in checking if something is in the set, as opposed to checking if something is in a list.</p>

# ##### Declaring

# In[36]:


# set() or {}
# no order {3, 2, 1} outputs as {1, 2, 3}

nums = {4,1,6,4}

print(nums)


# ##### .add()

# In[37]:


# set.add()
nums.add(56)
print(nums)


# ##### .remove()

# In[38]:


# removes by value
# set.remove()
# nums.remove(56)

nums.remove(56)
print(nums)


# ##### .union() 

# In[40]:


# Returns a union of two sets, can also use '|' or set.union(set)
# joins all numbers, gets rid of duplicates

s1 = {1,2,3,4}
s2 ={3,4,5,6}

s3 = s1.union(s2)
print(s3)

#or 
s4 = s1 | s2
print(s4)


# .intersection()

# In[42]:


# Returns an intersection of two sets, can also use '&'
# only takes similar elements from both sets

s5 = s2 & s1
print(s5)

s6 = s1.intersection(s2)
print(s6)


# ##### .difference()

# In[43]:


# Returns a set containing all the elements of invoking set that are not in the second set, can also use '-'
# only takes values from the first set that are not in the second set
# order matters

s7 = s2 - s1 

s8 = s1.difference(s2)

print(s1)
print(s2)
print(s7)
print(s8)


# ##### .clear()

# In[44]:


# Empties the whole set
# set.clear()

s8.clear()
print(s8)


# ##### Frozenset <br>
# <p>Frozen sets are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied.</p><br><b>Unique & Immutable</b>

# In[47]:


# frozenset([])
my_forzen_set = frozenset(s1)
print(my_forzen_set)


# ## Modules

# ##### Importing Entire Modules

# In[51]:


# import or from 'xxx' import *
# import math
from math import pi, floor
print(pi)
print(floor(pi))


# ##### Importing Methods Only

# In[ ]:


# from 'xxx' import 'xxx'
# from math import floor
#see above


# ##### Using the 'as' Keyword

# In[53]:


# from 'xxx' import 'xxx' as 'xxx' or import 'xxx' as 'xxx'
# from math import floor as f
from math import floor as f, pi as p
print(f(p))


# ##### Creating a Module

# In[55]:


from module import printName


# # Exercises

# ### 1) Build a Shopping Cart <br>
# <p><b>You can use either lists or dictionaries. The program should have the following capabilities:</b><br><br>
# 1) Takes in input <br>
# 2) Stores user input into a dictionary or list <br>
# 3) The User can add or delete items <br>
# 4) The User can see current shopping list <br>
# 5) The program Loops until user 'quits' <br>
# 6) Upon quiting the program, print out all items in the user's list <br>
# </p>

# In[ ]:


ShoppingBag = (2,8,14)

wholeFoods_bag = ShoppingBag
while True:
    response = input('what do you want to do? add/show/quit ')
   
    if response.lower()== 'quit':
        wholeFoods_bag.showShoppingBag()
        print('thanks for shopping!')
        break
    elif response.lower() == 'add':
        wholeFoods_bag.addToShoppingBag()
    elif response.lower()== 'show':
        wholeFoods_bag.showShoppingBag()
    else:
        print('try another command')


# ### 2) Create a Module in VS Code and Import It into jupyter notebook <br>
# <p><b>Module should have the following capabilities:</b><br><br>
# 1) Has a function to calculate the square footage of a house <br>
#     <b>Reminder of Formula: Length X Width == Area<br>
#         <hr>
# 2) Has a function to calculate the circumference of a circle <br><br>
# <b>Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage</b>
# </p>

# In[ ]:


def find_house_area(side):
    area = side*side
    print('the area of the house is ' + str(area))

def cir_of_cirle(radius):
    circumference = 2 * radius * 3.14 
    print('the circumference of this circle is ' + str(circumference))


find_house_area(12)
cir_of_cirle(7)

