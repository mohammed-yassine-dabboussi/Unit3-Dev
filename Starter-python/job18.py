def myfunction(*param) :
    liste = [] # creer une liste
    
    for i in param :  #remplir la liste
        liste.append(i)
    liste.sort() # sort est une fonction prédéfini pour trier une liste en ordre croissant

    for i in liste :
            print(i,end=" ")

myfunction(5, 8, 7, 4, 6, 1, 5, 3, 9)
print("")