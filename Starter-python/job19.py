#def tri1(*args) :
#    liste1 = [] # creer une liste
#    liste2 = [] # créer une deuxième liste pour le nouveau ordre croissant 
#    for i in args :  #remplir la liste
#        liste1.append(i)
    
   
#    LengthList = len(liste1) #length calcule le nombre de case d'une liste
    
#    j = 0
#    while j < LengthList:
#        k=LengthList
#        while k > 0:
#            min= liste1[0] 
#            i = 0
#            while i < len(liste1):
#                min = liste1[i]
#                
#                i += 1
#            #liste2[j]=min
#            k -= 1
#        j += 1 
    
#    for i in liste2 :
#           print(i,end=" ")

def tri2(*args):
    liste = []# creer une liste
    for i in args:#remplir la liste
        liste.append(i)

    for n in range(len(liste)):
         #variable de décision
        D = liste[n]
        j=n-1
        while j>=0 and liste[j]>D:
            liste[j+1] = liste[j]  #décaler les éléments de la liste
            j-=1
        liste[j+1] = D
    print(liste)

#tri1(9, 24, 5, 12, 11, 8, 7, 22, 17, 27)
tri2(6, 4, 2, 9, 3, 5, 5, 1, 8)