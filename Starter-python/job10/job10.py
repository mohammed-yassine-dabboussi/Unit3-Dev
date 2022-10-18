texte=input("Votre text : ")

fichier = open("output.txt", "w")
fichier.write(texte)
fichier.close()
fichier = open("output.txt", "r")
print (fichier.read())
fichier.close()