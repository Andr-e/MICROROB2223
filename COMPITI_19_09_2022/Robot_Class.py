#!/usr/bin/env python
# coding: utf-8

# In[1]:


def verifica(peso, tipologia):
    if(tipologia == "umanoide" and peso > 100):
        print("il robot morde")
    else:
        print("non morde")


# In[2]:


class Robot:
    def __init__(self, nome, peso, tipologia):
        self.nome = nome
        self.peso = peso
        self.tipologia = tipologia
        verifica(peso, tipologia)


# In[4]:


robot1 = Robot ("Piov", 151, "umanoide")


# In[ ]:




