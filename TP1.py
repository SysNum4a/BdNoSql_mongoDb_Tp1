
import pymongo
import matplotlib.pyplot as plt
from random import randint

client = pymongo.MongoClient("localhost", 27017)
# db = client.db1

database = client["db1"]
conferences = database["conferences"]
journals = database["journals"]
members = database["members"]
publis = database["publis"]

# Q1
print("1 =================================")
print("1 membres aléatoires")
# affiche un membre au hasard
print(members.find_one())


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
mLiri = members.find({"equipe":"LIRICA"})
print(len(mLiri.to_list()))


# Q6
print("6 =================================")
print("Membre du LIS dont le nom commence par 'C'")
mLis = members.find({"nom":{"$regex":'^C'}})
for membre in mLis:
    print(membre)
# print(len(mLis.to_list()))

# Q7
print("7 =================================")
print("Membre du LIS dont le nom contient la lettre 'S'")
mLis = members.find({"nom":{"$regex":'[Ss]'}})
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
dictPole = {}
dictEquipe = {}
dictPole["SD"] = len(members.find({"pole":"SD"}).to_list())
dictPole["ACS"] = len(members.find({"pole":"ACS"}).to_list())
dictPole["CALCUL"] = len(members.find({"pole":"CALCUL"}).to_list())
dictPole["SI"] = len(members.find({"pole":"SI"}).to_list())

print(dictPole)
dictEquipe["CDE"] = len(members.find({"equipe":"CDE"}).to_list())
dictEquipe["COSE"] = len(members.find({"equipe":"COSE"}).to_list())
dictEquipe["DIAPRO"] = len(members.find({"equipe":"DIAPRO"}).to_list())
dictEquipe["MOFED"] = len(members.find({"equipe":"MOFED"}).to_list())
dictEquipe["MOPS"] = len(members.find({"equipe":"MOPS"}).to_list())
dictEquipe["SAVS"] = len(members.find({"equipe":"SAVS"}).to_list())
dictEquipe["ACRO"] = len(members.find({"equipe":"ACRO"}).to_list())
dictEquipe["CANA"] = len(members.find({"equipe":"CANA"}).to_list())
dictEquipe["COALA"] = len(members.find({"equipe":"COALA"}).to_list())
dictEquipe["DALGO"] = len(members.find({"equipe":"DALGO"}).to_list())
dictEquipe["GMOD"] = len(members.find({"equipe":"GMOD"}).to_list())
dictEquipe["LIRICA"] = len(members.find({"equipe":"LIRICA"}).to_list())
dictEquipe["LSC"] = len(members.find({"equipe":"LSC"}).to_list())
dictEquipe["MOVE"] = len(members.find({"equipe":"MOVE"}).to_list())
dictEquipe["DANA"] = len(members.find({"equipe":"DANA"}).to_list())
dictEquipe["DIAMS"] = len(members.find({"equipe":"DIAMS"}).to_list())
dictEquipe["DYNI"] = len(members.find({"equipe":"DYNI"}).to_list())
dictEquipe["QARMA"] = len(members.find({"equipe":"QARMA"}).to_list())
dictEquipe["R2I"] = len(members.find({"equipe":"R2I"}).to_list())
dictEquipe["TALEP"] = len(members.find({"equipe":"TALEP"}).to_list())
dictEquipe["I&M"] = len(members.find({"equipe":"I&M"}).to_list())
dictEquipe["SIIM"] = len(members.find({"equipe":"SIIM"}).to_list())
print(dictEquipe)
plt.pie(dictPole.values(), labels=dictPole.keys())
plt.pie(dictEquipe.values(), labels=dictEquipe.keys())
plt.show()
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
    


print("=================================")



print("=================================")
# query = {"_id":"2172"}
# conference = conferences.find_one({"_id":"2172"})

# print(db.members.find_one())
# print(conference)


client.close()
