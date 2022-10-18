#Job 12 parcourir le contenu d'un fichier txt et compter le nombre caractère spéciaux
import re
with open("data.txt") as f:
    contents = f.read()
    #compter tous le mots du fichier 
    CountMot=len(contents.split())
    #Compter les caractéres spéciaux
    CountMotCS=len(contents.split("?"))
print(CountMot-CountMotCS)