#!/bin/python3

import pymongo
import matplotlib.pyplot as plt
from random import randint
import csv 
client = pymongo.MongoClient("10.71.250.75", 27017)
print(client)
# db = client.db1

db = client["science"]
conferences = db["conferences"]
journals = db["journals"]
members = db["members"]
publis = db["publis"]


# D'aprés https://www.core.edu.au/conference-portal#h.p_ID_44, les rangs C, B, A, etc sont un moyen d'informer sur l'importance de la conférenrence (en terme de qualité mais égallement de porté national/international).
# C'est un comité académique qui est en charge de prendre la decision du rang attribué à la conférence.

# Q1
print("===================================")
print("1 =================================")
print("===================================")
print("rang des conférence STACS, FOCS, SODA, MFCS")
# confList = ["STACS", "FOCS", "SODA", "MFCS"]
# for c in confList:
    # conf = db.conferences.find_one({"confAcronym":c})
    # print("Rang de " + conf["confAcronym"] + " : " + conf["rank"])
conf = db.conferences.find({"confAcronym":{"$in":["STACS", "FOCS", "SODA", "MFCS"]}})
for c in list(conf):
    print("Rang de " + c["confAcronym"] + " : " + c["rank"])

# Q2
print("===================================")
print("2 =================================")
print("===================================")
print("quels sont les rangs présent dans les données")
rangs = db.conferences.distinct("rank")
print("Nombre de rang présents dans les données : " + str(len(rangs)))
for r in rangs:
    print(r)

# Q3
print("===================================")
print("3 =================================")
print("===================================")
print("quels sont les conf de rang national France")
conf = db.conferences.find({"rank":"National: France"})
for c in list(conf):
    print(c["conference"] + " rang =  " + c["rank"])


# Q4
print("===================================")
print("4 =================================")
print("===================================")
print("quels sont les conf qui ont le méme accronyme?")
conf = db.conferences.aggregate( [{"$group":{"_id": "$confAcronym", "count": {"$sum":1}}}, {"$match": {"count":{"$gt":1}}}] )
for c in conf:
    print(c)


# Q5
print("===================================")
print("5 =================================")
print("===================================")
print("Combien y a t'il de conférences européennes?")
dictPays = {}
listPaysUE = []
with open("../../data/curiexplore-pays.csv", "r") as fdCsv:
    dictPays = csv.DictReader(fdCsv, delimiter=";")
    for row in dictPays:
        if row["european_union"] == "True":
            listPaysUE.append(row["name_en"])
nbConfEu = 0
for p in listPaysUE:
    conf = db.conferences.find({"rank":{"$regex":p,"$options":'i'}})
    nbConfEu = nbConfEu + len(list(conf))
print(nbConfEu)


listPaysUERegex = []
for p in listPaysUE:
    listPaysUERegex.append("/"+p+"/")
    
conf = db.conferences.find({"rank":{"$in":["France"]}})
print(len(list(conf)))
# mLis = members.find({"nom":{"$regex":'s',"$options":'i'}})




quit()
[
  {
    _id: '1398',
    conference: 'International Symposium on Mathematical Foundations of Computer Science',
    confAcronym: 'MFCS',
    source: 'CORE2023',
    rank: 'A'
  }
]

