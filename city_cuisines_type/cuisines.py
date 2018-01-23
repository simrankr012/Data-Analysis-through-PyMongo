
# coding: utf-8

# In[1]:

import pymongo
from collections import Counter
from pymongo import MongoClient
client=MongoClient('163.172.130.232',27017)
client.admin.authenticate(username,password,mechanism='SCRAM-SHA-1')
db=client.databasename
col=db.collection_name


# In[ ]:

cui_list=[]
cui_dict={}
#reading the data from collection and making a dictionary containing count of different cuisines city wise
data=col.find({'cuisines':{'$ne':[]}}) #reading only the data where cuisines field is not null

# In[26]:

cuisine=[]
for i in cui_col:
    cui_type=i["cuisines"]
    for j in cui_type:
        ct=j.split(",")
        for k in ct:
            cuisine.append(k.strip())



ct={}


# In[99]:

for i in data:
    
    city=i["city"]
    for j in i["cuisines"]:
        if city in ct:
            if j in ct[city]:
                ct[city][j]+=1
            else:
                ct[city].update({j:1})
        else:
            ct.update({city:{j:1}})


# In[100]:

print ct
#example of output : city: Sao Paulo, {cuisine type: count}
#u'Sao Paulo': {u' Italian ': 2, u' Pub ': 1, u' Pizza ': 9, u' Brazilian, South American ': 6, u' Contemporary, Seafood ': 1, u' Italian, Pizza ': 2, 
#u' American, Fast food, Diner ': 1, u' Lebanese, Mediterranean ': 1, u' Chinese, Japanese, Brazilian, South American, Minority Chinese ': 1,
# u' Japanese, Sushi, Asian ': 4, u' Barbecue ': 6, u' German ': 1, u' American, Steakhouse ': 1, u' Mexican ': 1, u' Japanese ': 4,
# u' Brazilian, Bar, Pub, South American ': 1, u' Chinese ': 3, u' Japanese, Sushi ': 3, u' French ': 1, u' Fast food ': 8, u' French, European ': 1, 
#u' Brazilian, Cafe, South American ': 1, u' Bar, Pub ': 3, u' Cafe ': 5, u' Italian, Barbecue ': 1},