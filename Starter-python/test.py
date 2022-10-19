def myfunction(*param) :
    liste = [] # creer une liste
    for i in param :  #remplir la liste
        liste.append(i)
    
    del liste[2]

    for i in liste :
            print(i)

myfunction(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("")