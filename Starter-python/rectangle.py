largeur = int(input("Veuillez entrer la largeur : "))
hauteur = int(input("Veuillez entrer la hauteur: "))
for i in range(hauteur):
    if i==0 or i==hauteur-1:
        print('|',end="")        
        for i in range(largeur-2):
            print ("-",end="")
        print("|")
    else:
        print('|',end="")  
        for i in range(largeur-2):
            print (" ",end="")
        print("|")