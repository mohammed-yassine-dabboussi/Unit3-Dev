def myfunction(*param) :
    liste = [] # creer une liste
    liste2 = [] # créer une deuxième liste pour le nouveau ordre croissant 
    for i in param :  #remplir la liste
        liste.append(i)
    
   
    LengthList = len(liste)
    j = 0
    
    while j < LengthList:
        
        for i in param:  
            min= list[0]  
            if liste[i] < min:
                min = liste[i]
                del liste[i]
                
            
        liste2[j]=min 
    j += 1 
    
    for i in liste :
            print(i,end=" ")

myfunction(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("")