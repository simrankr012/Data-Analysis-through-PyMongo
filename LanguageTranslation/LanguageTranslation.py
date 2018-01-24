
# coding: utf-8

# In[129]:

import pymongo
import goslate
from translate import Translator
 
from collections import Counter
from pymongo import MongoClient
client=MongoClient('163.172.130.232',27017)
client.admin.authenticate(username,password,mechanism='SCRAM-SHA-1')
db=client.database_name
col=db.collection_name


#{HOTEL AMENITIES :[Business Centre with Internet Access, Room Service, Shuttle Bus Service, Free Parking,Laundry Service, Concierge, Babysitting],
#ROOM AMENITIES:[Air Conditioning ,Minibar]}
# Task is to convert these amenities to different languages so that whenever visits the hotel page they can easily see translated version in their language

data=col.find({'amenities':{'$ne':{}}}) #finding only the records where the amenities are not null



trans_dict={} #creating dictionary which will store the translated version of amenities

anames=[] #list of amenities under categories 
translator= Translator(to_lang="fr") #specifying the language to translate to. code fr indicates french language 
for i in data:
    a=i["amenities"] #according to the data I had , there was a specific field for hotel amenities
    
    for j in a.items():
        amenities_catg=j[0]
        
        
        ament_catg_translation = translator.translate(amenities_catg) #translating the amenities categories like room, hotel amenities , etc
        
        
        amenities_list=j[1]
        
        for k in amenities_list:
            
            
            for l in k.items():
                ann=l[1]
                if ann==[]:
                    pass
                else:
                    amenities_name=ann
                    translation1 = translator.translate(amenities_name) #translating the list of amenities under categories 
                    
                    anames.append(translation1)
                    if ament_catg_translation in trans_dict: #creating translated dictionary
                        pass
                        
                    else:
                        trans_dict.update({ament_catg_translation:anames})

print trans_dict

#output

#{'Internet': [u'Tennis', u'S\xe8che-cheveux', u'Salle de bain privative', u'\xc9quipements de repassage', u"Gratuit! Une connexion Wi-Fi est disponible dans tout l'\xe9tablissement gratuitement.", 
#u'Gratuit! Un parking priv\xe9 gratuit est disponible sur place (r\xe9servation impossible).', u'Non-fumeurs', u'Les animaux ne sont pas accept\xe9s.', u'Barbecue', u'Cha\xeenes satellite', 
#u'Le lecteur de DVD', u'T\xe9l\xe9', u'Machine \xe0 caf\xe9', u'Plaque de cuisson', u'Four', u'S\xe8che-linge', u'Ustensiles de cuisine', u'Lave-vaisselle', u'Four micro-ondes', u'R\xe9frig\xe9rateur']}