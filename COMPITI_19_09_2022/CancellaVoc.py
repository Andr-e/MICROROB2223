#!/usr/bin/env python
# coding: utf-8

# In[12]:


word = input("Metti una parola: ")


# In[14]:


list_cn = [i for i in word if(i!= "a" and i != "e" and i != "i" and i != "o" and i != "u")]
print(list_cn)

