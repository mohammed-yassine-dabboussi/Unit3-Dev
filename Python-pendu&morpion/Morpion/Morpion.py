#Projet jeu (Morpion) Mohammed Yassine Dabboussi 
#                      La Plateforme 2022


jouerOuScore=input("Bonjour souhaites tu jouer ou voir les scores ? ")
#fonction pour affiché la matrice du jeu 
def affichageMatrice(M):
    for i in range (len(M)): 
        for j in range (len(M)):
            print(M[i][j], end= " ")
        print("")    


#condition pour Joueur ou affiche le score 
if jouerOuScore=="Jouer" or jouerOuScore=="jouer":
    print("Jouer")
    
    #Saisie des noms des joueurs 
    nomJoueur1=input("Username 1 Croix : ")
    nomJoueur2=input("Username 2 Rond  : ")
    
    #initialisation de la matrice et le nombre de lignes et de colonnes 
    M=[['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
    
    #Premier affichage  
    affichageMatrice(M)   
    
    #Début du jeu 
    
    jeu1=print(nomJoueur1, " joue (ligne puis colonne) : ")

    

elif jouerOuScore=="Score" or jouerOuScore=="score":
    print("score")