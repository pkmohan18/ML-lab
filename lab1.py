#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
file=open('lab1data.csv')
data=list(csv.reader(file))
length=len(data[0])-1
h=['0']*length
print("Initial hypothesis:",h)
print("Data:")
for i in data:
    print(i)
data.pop(0)
for i in range(len(data)):
    if data[i][length]=='yes':
        for j in range(len(data[i])-1):
            if h[j]=='0':
                h[j]=data[i][j]
            if h[j]!=data[i][j]:
                h[j]='?'
print("\nFinal hypothesis:",h)


# In[ ]:




