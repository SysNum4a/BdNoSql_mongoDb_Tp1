#!/bin/python3

import pymongo
import matplotlib.pyplot as plt
from random import randint
client = pymongo.MongoClient("10.71.250.75", 27017)
print(client)
# db = client.db1

database = client["science"]
conferences = database["conferences"]
journals = database["journals"]
members = database["members"]
publis = database["publis"]
print(members)
# Q1
print("1 =================================")
print("1 membres aléatoires")
# affiche un membre au hasard
print(members.find_one())

print("Find")


# Q2
print("2 =================================")
print("5 membres aléatoires")
for i in range(0,5):
    randId = randint(0, members.count_documents({}))
    query = {"_id":randId}
    print(members.find_one(query))


# Q3
print("3 =================================")
print("les membres de l'equipe ACRO")
mCde = members.find({"equipe":"ACRO"})
for membre in mCde:
    print(membre)
print(type(mCde))


# Q4
print("4 =================================")
print("Nom et prenom des membres du pole Calcul")
mCalc = members.find({"pole":"CALCUL"}, {"nom":1,"prenoms":1})
# mCalc = members.find({"pole":"CALCUL"})
for membre in mCalc:
    print(membre)

# Q5
print("5 =================================")
print("Nombre de membre de l'equipe LIRICA")
nbMLiri = members.count_documents({"equipe":"LIRICA"})
print(nbMLiri)


# Q6
print("6 =================================")
print("Membre du LIS dont le nom commence par 'C'")
mLis = members.find({"nom":{"$regex":'^C'}})
for membre in mLis:
    print(membre)


# Q7
print("7 =================================")
print("Membre du LIS dont le nom contient la lettre 'S'")
# mLis = members.find({"nom":{"$regex":'[Ss]'}})
# mLis = members.find({"nom":{"$regex":'s',"$options":'i'}})
mLis = members.find({"nom":{"$regex":'(?i)s(?-i)'}})
for membre in mLis:
    print(membre)


# Q8
print("8 =================================")
print("Membre du pole SD triés par ordre alhabétique")
mSd = members.find({"pole":"SD"}, {"nom":1,"prenoms":1})
mSd.sort("nom", pymongo.ASCENDING)
print(mSd)
for membre in mSd:
    print(membre)

# Q9
print("9 =================================")
print("Répartition des membres par équipes et par poles")
poles = members.distinct("pole")
equipes = members.distinct("equipe")
print(poles)
print(equipes)

dictPole = {}
dictEquipe = {}
for pole in poles:
    dictPole[pole] = members.count_documents({"pole":pole})
for equipe in equipes:
    dictEquipe[equipe] = members.count_documents({"equipe":equipe})
print(dictPole)
print(dictEquipe)

fig, (ax1,ax2) = plt.subplots(1,2)
fig.suptitle("Répartition des membres par pôles et par aquipes")
ax1.pie(dictPole.values(), labels=dictPole.keys())
ax1.set_title("Répartition par pôles")
ax2.pie(dictEquipe.values(), labels=dictEquipe.keys())
ax2.set_title("Répartition par équipes")
plt.show()



client.close()

# mCalc = members.find({"pole":"CALCUL"})
# mCalcNom = mCalc.distinct("nom")

# mCalcNom = members.distinct("nom", {"pole":"CALCUL"})
# mCalcPre = members.distinct("prenoms", {"pole":"CALCUL"})
# print(mCalcNom)

# mCalcNom = mCalc.distinct("nom")
# mCalcPrenom = mCalc.distinct("prenoms")
# print(mCalcNom)
# print(mCalcPrenom)

quit()

# extrait la colonne _id
print("=================================")
m2 = members.distinct("_id")
for i in range(0,5):
    print(m2[i])
    

# query = {"_id":"2172"}
# conference = conferences.find_one({"_id":"2172"})

# print(db.members.find_one())
# print(conference)


client.close()
