#Projet jeu (Morpion) Mohammed Yassine Dabboussi 
#                     La Plateforme 2022


#fonction pour affiché la matrice du jeu 
def affichageMatrice(M):
    for i in range (len(M)): 
        for j in range (len(M)):
            print(M[i][j], end= " ")
        print("")    

#fonction ajouter le choix du joueur 1 à la ligne et la colonne souhaité
def placer_X(a,b,c):
    if M[a-1][b-1]=="-":
        M[a-1][b-1]="X"#-1 pour adapter le choix du joueur avec les indices de la matrice 
        c=0
    else:
        c=1
    return c

#fonction ajouter le choix du joueur 2 à la ligne et la colonne souhaité
def placer_O(a,b,c):
    if M[a-1][b-1]=="-":
        M[a-1][b-1]="O"#-1 pour adapter le choix du joueur avec les indices de la matrice 
        c=0
    else: 
        c=1
    return c


######################
#Programme Principale#
######################

#Premier choix de l'utilisateur pour jouer ou voir les scores
jouerOuScore=input("Bonjour souhaites tu jouer ou voir les scores ? ")

#si l'utilisateur souhaite jouer  
if jouerOuScore=="Jouer" or jouerOuScore=="jouer":
    
    #Saisie des noms des joueurs 
    nomJoueur1=input("Username 1 Croix : ")
    nomJoueur2=input("Username 2 Rond  : ")
    
    #initialisation de la matrice et le nombre de lignes et de colonnes 
    M=[['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
    
    #Premier affichage  
    affichageMatrice(M)   
    
    compteur_jeu=0
    rejouer=1

    while compteur_jeu<4:

        #Début du jeu 
        affInput1 =nomJoueur1+" joue (ligne puis colonne) : " # pour l'affichage à l'input nom du joueur avec le message 
        affInput2 =nomJoueur2+" joue (ligne puis colonne) : "
        
        while rejouer==1:
            #joueur 1 joue
            jeu1=input(affInput1)

            #Récupere les choix de joueur 1 et le mettre en entier  
            jeu1_ligne= int (jeu1[0])
            jeu1_colonne= int (jeu1[2])
            #appeler la fonction pour mettre en place les choix du joueur 1
            placer_X(jeu1_ligne,jeu1_colonne,rejouer)
            rejouer=placer_X(jeu1_ligne,jeu1_colonne,rejouer)
            affichageMatrice(M)  

        
        
        while rejouer==0:
            #joueur 2 joue
            jeu2=input(affInput2)

            #Récupere les choix de joueur 2 et le mettre en entier  
            jeu2_ligne= int (jeu2[0])
            jeu2_colonne= int (jeu2[2])
            #appeler la fonction pour mettre en place les choix du joueur 2 
            placer_O(jeu2_ligne,jeu2_colonne,rejouer)
            rejouer=placer_O(jeu1_ligne,jeu1_colonne,rejouer)
            affichageMatrice(M)  

        compteur_jeu += 1

        
        


#Si l'utilisateur souhaite voir que les scores     
elif jouerOuScore=="Scores" or jouerOuScore=="scores":
    print("scores")