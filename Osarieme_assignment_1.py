#!/usr/bin/env python
# coding: utf-8

# # Assignment 1 (Week 1)
# 
# >**Note**: Late submissions are ***`penalized`***.
# 
# ## Name: Osarieme Ehimwenma

# In[49]:


# Black code formatter (Optional)
# $ pip install nb_black

# auto reload imports
import pandas as pd
import numpy as np
import random
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# ## Qs 1: 
# 
# Create a class **`Die`** with one attribute called sides, which has a default value of 6. Write a method called `roll_die()` that prints a random number between **1** and the **number of sides** the die has. Make a **6-sided** die and roll it **4** times.

# In[50]:


class Die:
    """creating a class and method that prints random number of a die between 1 and num"""
    
    def __init__(self, sides: int) -> None:
        """Initializing a 6-sided die"""
        self.sides = sides
        
#     def die_roll():
#         diceRoll = random.randint(1, 6)
#         return diceRoll
        
    def roll_die(self) -> int:
        """Rolling the die randomly"""
        dieRoll = random.randint(1, 6)
        return dieRoll, {self.sides}


# In[51]:


# Write your solution here
die = Die(6)
die.roll_die()


# In[52]:


# Write your solution here
die = Die(6)
die.roll_die()


# In[56]:


# Write your solution here
die = Die(6)
die.roll_die()


# In[54]:


# Write your solution here
die = Die(6)
die.roll_die()


# In[ ]:





# ## Qs 2: 
# 
# Write a function called `checker()` that accepts a number between 1 and N. Your function should print **Yes** if the number is divisible by 3, **Okay** if the number is divisible by 4 and **Perfect** if the number is divisible by 12. Test your function with **2** examples as shown below:
# 
# ```python
# 
# def checker(number: int) -> None:
#     pass
# 
# checker(number=13)
# 
# # 3: Yes
# # 4: Okay
# # 6: Yes
# # 8: Okay
# # 9: Yes
# # 12: Perfect
# 
# checker(number=30)
# ```

# In[24]:


# Write your solution here
def checker(number: int) -> None:
     """A function that accepts a number divisible by 3, 4, 12"""

num = 13
for num in range(1, num):
    if num % 12 == 0:
        print(f"{num}: Perfect")
    elif num % 4 == 0:
        print(f"{num}: Okay")
    elif num % 3 == 0:
        print(f"{num}: Yes")
        

# number in desc order to prevent error occurring while dividing


# In[25]:


# Write your solution here
def checker(number: int) -> None:
     """A function that accepts a number divisible by 3, 4, 12"""

checker = 30
for checker in range(1, checker):
    if checker % 12 == 0:
        print(f"{checker}: Perfect")
    elif checker % 4 == 0:
        print(f"{checker}: Okay")
    elif checker % 3 == 0:
        print(f"{checker}: Yes")
 


# #### Qs 3: 
# 
# Create a class called `MeanOrMedian`. Implement two methods in your class `calculate_mean()` and `calculate_median()` that calculates the **`mean`** and the **`median`** respectively given a list. Instantiate the class `MeanOrMedian` and test the **2** `mean` and `median` methods.

# In[26]:


# Write your solution here
class Students():
    """creating a class that calculate the man and median of a given list"""
    def __init__(self, *score: int) -> None:
        """Initializing the attribute"""
        self.score = score
        
    def calculate_mean(self) -> list:
        """calculate for Mean"""
        my_list = list()
        my_list.extend(self.score)
        mean = sum(my_list) / len(my_list)
        return mean
   
    def calculate_median(self) -> list:
        """calculate for Median"""
        my_list = list()
        my_list.extend(self.score)
        my_list = sorted(my_list)
        middle_num = (len(my_list) // 2)
        
        if len(my_list) % 2 != 0:
            return my_list[middle_num]
        
        else:
            median = (my_list[middle_num]+ my_list[middle_num -1])/2
            median / 2
            
        return median  


# In[27]:


# Write your solution here
score = Students(82,88,91,75,91,99)
mean = score.calculate_mean()
print(f"mean: {mean}")


# In[28]:


# Write your solution here
score = Students(82,88,91,75,91,99)
median = score.calculate_median()
print(f"median: {median}")


# In[ ]:





# ## Qs 4:
# 
# Write a program to create the function called `solver()`, which can accept two variables and perform **multiplication** and **division**. It must also return both **multiplication** and **division** in the same return call. Call the function using **two** different examples.

# In[47]:


# Write your solution here
def solver(a,b):
    """A function that accepts two(2) variables to perform multiplication and division."""
    multiplication = (a*b)
    division = (a/b)
    print(f"multiplication: {multiplication}, division: {division}")
    #return multiplication, division

solver(12,4)


# In[48]:


# Write your solution here
solver(36,3)


# In[ ]:





# ## Qs 5:
# 
# Given the dictionary below, extract the following:
# 
# a.`name`
# 
# b. `height,width`
# 
# c. `size`
# 
# 
# 
# ```python
# 
# my_dict = {
#    "id": "001",
#    "name": "dog",
#    "image":
#       {
#          "url": "images/001.jpg",
# 
#             "thumbnail":
#                {
#                   "url": "images/thumbnails/001.jpg",
#                   "height,width": "3x6"
#                },
#           "size": "30 kB"
#       }
# }
# 
# ```

# In[6]:


my_dict = {"id": "001", "name": "dog", "size": "30 kB", "height,width": "3x6"}
my_dict


# In[7]:


# Write your solution here
my_dict["name"]


# In[8]:


# Write your solution here
my_dict.get("height,width")


# In[9]:


# Write your solution here
my_dict.get("size")


# In[ ]:





# In[ ]:





# In[ ]:




