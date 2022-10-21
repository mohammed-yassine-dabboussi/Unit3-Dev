#Projet jeu (Le pendu) Mohammed Yassine Dabboussi 
#                      La Plateforme 2022

import random

# fonction pour convertir une chaine à une liste
def ConvertChaineToList(string):
    liste = []
    liste[:0] = string
    return liste


print("***Jeu Pendu***")
print("")

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
with open("dico_france.txt", "r", encoding= "iso 8859-1") as f: #encoding= "iso 8859-1" pour les accents 
    
    
    #lire le fichier texte
    contents = f.read().splitlines()

    # choisir un numéro aléatoire entre 1 et la dernière ligne du fichier texte
    NumAleatoire=random.randint(1, len(contents))

    for i in range(len(contents)):#parcourir toutes lignes 
        mot=contents[NumAleatoire-1] # -1 car le i commence par 0 et le fichier texte commence par 1
        
    print("le mot deviner pour le test (à supprimer  ligne 44)", mot) # afficher le mot à deviner 
f.close()    

#Longueur du mot à deviner 
LenMot=len(mot)

#afficher le nombre de vie
print("Nombre de vie(s) restante(s) : ", vie)

#créer deux listes (1 pour le mot du jeu) (2 pour le mot à proposer)
Liste1=ConvertChaineToList(mot)#Liste 1 contient le mot à deviner
Liste2=['_'] * LenMot #créer une liste avec des tirets qui a la même taille que la longueur du mot à deviner

#changer le prémier élément de la liste en miniscule
#if  ord(Liste1[0])> 64 and ord(Liste1[0]< 91): # ord donne le code ascii d'un caractère
#    Liste1[0]=chr(ord(Liste1[0])+32)

#Proposer des lettres jusqu'à la fin des vies
ch1=""
ch2=" "

#Premier affichage de lettres proposés


while vie > 0 and Liste1 != Liste2:

        #Saisie de la lettre et garder chaque lettre à la fin
        
        lettreProposee=input("Quelle lettre propose tu ? ")
        
        #Pour afficher Lettres proposées
        ch1=ch1+lettreProposee+" "
        ch2="Lettres proposées : " + ch1 + " "
        print(ch2)
        
        vie -=1
        print("Nombre de vie(s) restante(s) : ", vie)
        
        #condition si la lettre proposée existe dans le mot à deviner
        j=0 
        for i in Liste1:
            if i == lettreProposee:
                #remplacement
                Liste2[j]=i
            j += 1
        for i in Liste2:
                    print(i, end=" ")
        print("")


print("")
#perte ou victoire 
if vie == 0 or Liste1 != Liste2:
        print("*** Vous avez perdu ***")
elif Liste1==Liste2 :
        print("*** Vous avez gagné ***")