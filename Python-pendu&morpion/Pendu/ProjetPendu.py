#Projet jeu (Le pendu) Mohammed Yassine Dabboussi 
#                      La Plateforme 2022

import random

# convertir une chaine à une liste
def ConvertChaineToList(string):
    liste = []
    liste[:0] = string
    return liste

#Choix du niveau
niveau = input("Bonjour, à quel niveau souhaites tu jouer? ")
while (niveau != "débutant") and (niveau != "intermédiaire") and (niveau != "expert") :
    niveau = input("Bonjour, à quel niveau souhaites tu jouer? ")
    
# Donner une valeur à la valeur vie selon le niveau
if niveau=="débutant":
        vie=10
elif niveau=="intermédiaire":
        vie=7
elif niveau=="expert":
        vie=4

#choisir aléatoirement un mot du dictionnaire 
import random # bibliothèque de random(aléatoire)

# ouvrirle fichier texte
with open("dico_france.txt", "r", encoding= "iso 8859-1") as f: 
    
    
    #lire le fichier texte
    contents = f.read().splitlines()

    # choisir un numéro aléatoire entre 1 et la dernière ligne du fichier texte
    NumAleatoire=random.randint(1, len(contents))

    for i in range(len(contents)):#parcourir toutes lignes 
        mot=contents[NumAleatoire-1] # -1 car le i commence par 0 et le fichier texte commence par 1
        
    print(mot) # afficher le mot du jeu !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
f.close()    

#Longueur du mot à deviner 
LenMot=len(mot)

#afficher le nombre de vie
print("Nombre de vie(s) restante(s) : ", vie)

#créer deux listes (1 pour le mot du jeu) (2 pour le mot à proposer)
Liste1=ConvertChaineToList(mot)
print("Liste 1 ", Liste1)
Liste2=['_'] * LenMot #créer une liste avec des tirets 
print(Liste2)

#Proposer des lettres jusqu'à la fin des vies
while vie > 0 :
        LettreProposees = input("Lettre proposées : ")
        print("")
        vie -=1

#perte ou victoire 
if vie == 0:
        print("vous avez perdu")
#elif mot == mot à deviner :
#        print("Vous avez gagné ")