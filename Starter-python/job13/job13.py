nb=int(input("Entrez un nombre entier :"))
f = open("data.txt", "r") 
fichier = f.read()
liste = fichier.split()
CountMot = 0
for i in range (len(liste)) :
    if len(liste[i]) == nb :
        CountMot += 1
print (CountMot, "mot avec",nb,"caractères")
f.close()