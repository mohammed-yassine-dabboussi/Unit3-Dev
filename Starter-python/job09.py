hauteur = input("Veuillez entrer la hauteur: ")
a=int(hauteur)
b=a*2
i=1
for i in range(a):
    for i in range(b):
        if ((b*2)%i) == 0:
            print("*",end="")
        else:
            print (i,end="")
    print ("",end="")
    print()
print()