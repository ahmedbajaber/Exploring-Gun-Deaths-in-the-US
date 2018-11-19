#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import datetime
f = open('guns.csv', 'r')
csvreader = csv.reader(f)
data = list(csvreader)

print(data[0:5])

# In[3]:


headers = data[0]
data = data[1:]
#print(headers)
print(data[0:5])


# In[4]:


year_counts = {}
years = [row[1] for row in data]

for i in years:
    
    if i in year_counts:
        year_counts[i] = year_counts[i] + 1
    else:
        year_counts[i] = 1
print(year_counts)


# In[5]:


import datetime
data = data[1:]
dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]
dates[:5]


# In[6]:


date_counts ={}

for i in dates:
    if i not in date_counts:
        date_counts[i] = 1
    else:
        date_counts[i] = date_counts[i] + 1
date_counts


# In[7]:


sex = [row[5] for row in data]
sex_counts = {}

for i in sex:
    if i in sex_counts:
        sex_counts[i] = sex_counts[i] + 1
    else:
        sex_counts[i] = 1
sex_counts


# In[8]:


race = [row[7] for row in data]
race_counts = {}

for i in race:
    if i in race_counts:
        race_counts[i] = race_counts[i] + 1
    else:
        race_counts[i] = 1
race_counts


# In[9]:


g = open('census.csv', 'r')
csvreader = csv.reader(g)
census = list(g)
census


# In[10]:


race_counts


# In[14]:


mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}
race_per_hundredk = {}

for i in race_counts:
    value = race_counts[i]/mapping[i]
    mult = value * 100000
    
    if race_counts[i] not in race_per_hundredk:
        race_per_hundredk[i] = mult 
race_per_hundredk


# In[15]:


intents = [row[3] for row in data]
intents


# In[19]:


races = [row[7] for row in data]

homicide_race_counts = {}

for i,race in enumerate(races):
    
    if intents[i] == 'Homicide':
        if race not in homicide_race_counts:
            homicide_race_counts[race] = 1
        else:
            homicide_race_counts[race] += 1
homicide_race_counts            


# In[ ]:





# In[20]:


homicide_per_hundredk = {}
for i in homicide_race_counts:
    value = homicide_race_counts[i]/mapping[i]
    mult = value * 100000
    
    if homicide_race_counts[i] not in homicide_per_hundredk:
        homicide_per_hundredk[i] = mult
        
        
homicide_per_hundredk


# In[ ]:


'''
Findings
It appears that gun related homicides in the US disproportionately affect people in the Black and Hispanic racial categories.
'''


