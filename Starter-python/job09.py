hauteur = int(input("Veuillez entrer la hauteur: "))
b = hauteur*2
j=b/2
h=b/2
for i in range(hauteur):
    for i in range(b+1):
        if i == j-1:
            print("/",end="")
        elif i == h+1:
            print ("\\",end="")
        #elif i == hauteur:
        #    print("",end="")
        else:
            print(" ",end="")
    print ("",end="")
    j = j-1
    h = h+1
    print()