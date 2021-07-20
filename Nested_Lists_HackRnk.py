# https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen



#!/usr/bin/env python
# coding: utf-8

# In[18]:


if __name__ == '__main__':
    
    Temp = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Temp.append([name,score])
        


# In[48]:


score = []
for x in Temp:
    score.append(x[1])
    
Temp.append(["Demm",23.56])    


# In[49]:


sorted(list(set(score)))


# In[51]:


for x in (Temp):
    
    if x[1] == sorted(list(set(score)))[1]:
        
        print(x[0])


# In[ ]:




