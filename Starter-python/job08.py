largeur = input("Veuillez entrer la largeur : ")
hauteur = input("Veuillez entrer la hauteur: ")
a = int(hauteur)
b = int(largeur)
for i in range(a):
    if i==0 or i==a-1:
        print('|',end="")        
        for i in range(b-2):
            print ("-",end="")
        print("|")
    else:
        print('|',end="")  
        for i in range(b-2):
            print (" ",end="")
        print("|")