#!/usr/bin/env python
# coding: utf-8

# # Examples
# 
# ## Lists

# In[17]:


mylist = ["coffee", 2.5, "breakfast", 3, "butter"] # using square brackets
mylist2 = list(("coffee", 2.5, "breakfast", 3, "butter")) # using function "list()"


# In[2]:


print(mylist)
print(mylist2)


# In[3]:


len(mylist)


# ## Dictionaries

# In[4]:


my_dict = dict()
my_dict = {
        "Name": ["Cécé", "Oxy", "Vivi", "Anna", "Micha"], 
        "Age": [30, 31, 31, 31, 49],
        "Hobby": ["Videogaming", "Wine", "Sleep", "Wine", "Music"]
            }

# It is not possible to have two identic keys in a dictionary


# In[5]:


my_dict


# In[6]:


len(my_dict) # length is the number of keys, each can contain multiple items


# # Accessing and changing elements

# ## Lists

# In[7]:


print(mylist[1]) # positive index - starts from 0 from the beginning
print(mylist[-3]) # negative index - runs starting from -1 at the end towards beginning


# In[8]:


print(mylist[:2]) # selects elements up to 2 not inclusive, i.e. 0 and 1
print(mylist[3:]) # selects elements from 3 not inclusive, i.e. 4 and 5


# In[18]:


print(mylist, "before change")
mylist[1] = False
print(mylist, "after change")


# In[19]:


mylist.insert(2, "new item") # insert the item at the indicated index value
print(mylist)


# In[20]:


mylist.append("apple") # add a new item at the end of the list
print(mylist)


# In[21]:


mylist3 = list(('orange', 'keys', 3))
mylist.extend(mylist3)
print(mylist)


# In[22]:


mylist.remove(False) # remove specific item
mylist.pop() # remove the last item from the list
mylist.pop(3) # remove the item under a specific index

print(mylist)


# In[23]:


mylist.sort(reverse = False) # if reverse is set to True, sorting is descending
print(mylist)

# it is important that all elements are of the same type to compare them one to another


# In[25]:


new_list = mylist.copy()


# In[26]:


del mylist[1]
print(mylist)


# In[27]:


mylist.clear()
print(mylist)


# In[28]:


del mylist  # if item is not specified, deletes the whole list and the associated variable from cache
new_list


# ## Dictionaries

# In[29]:


print(my_dict["Hobby"]) # using square brackets
print(my_dict.get("Name")) # using the function "get()"


# In[30]:


x = my_dict.keys() # get the list keys
my_dict["Nationality"] = ["French", "Russian", "French / Ukranian", "French / Russian", "French"] # add new key to the dictionary
print(my_dict)
# it is possible to use the function "update()"


# In[31]:


y = my_dict.items() # all the items of the dictionary including keys and elements
print(y)


# In[32]:


new_dict = my_dict.copy() #same as for list, to copy dict


# In[33]:


my_dict.pop("Hobby")
print(my_dict)


# In[34]:


my_dict.popitem() # removes the last inserted item
print(my_dict)


# In[35]:


del my_dict['Age']
print(my_dict)


# In[36]:


my_dict.clear()
print(my_dict)


# In[37]:


del my_dict


# In[38]:


new_dict


# In[40]:


friends = {
    "friend 1": {
         'Name': 'Cécé',
         'Age': 30,
         'Hobby': 'Videogaming',
         'Nationality': 'French'},
    
    "friend 2": {
         'Name': 'Vivi',
         'Age': 31,
         'Hobby': 'Sleep',
         'Nationality': 'French / Ukranian'},

    "friend 3": {
         'Name': 'Oxy',
         'Age': 31,
         'Hobby': 'Wine',
         'Nationality': 'Russian'},
    
    "friend 4": {
         'Name': 'Mickaël',
         'Age': 49,
         'Hobby': 'Music',
         'Nationality': 'French'}
}


# In[42]:


print(friends['friend 1']['Age'])


# In[41]:


print(friends["friend 2"])


# # Other list methods

# In[ ]:


# for and while loops
# list comprehension: newlist = [expression for item in iterable if condition == True]

# count() -- Returns the number of elements with the specified value
# index() -- Returns the index of the first element with the specified value
# reverse() -- Reverses the order of the list


# # Other dictionaries methods

# In[ ]:


# for loops to run through my_dict.keys(), my_dict.values or my_dict.items()
# update() -- Updates the items for a specified key

