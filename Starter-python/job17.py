def myfunction(*param) :
    liste = [] # creer une liste
    for i in param :  #remplir la liste
        liste.append(i)

    for i in liste : #parcourir la liste et afficher le nombre paires
        if i % 2 == 0 : # condition si le reste de la division des nombres sur 2 est égale à 0
            print(i,end=" ")

myfunction(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("")