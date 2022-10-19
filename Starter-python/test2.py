def tri(*args):
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

tri(9, 24, 5, 12, 11, 8, 7, 22, 17, 27)