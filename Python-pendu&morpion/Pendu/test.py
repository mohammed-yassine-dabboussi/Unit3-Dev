
# convertir une chaine à une liste
def ConvertChaineToList(string):
    liste = []
    liste[:0] = string
    return liste
 
 

mot = "ABCD"
Liste1=ConvertChaineToList(mot)
Liste2=ConvertChaineToList(mot)
#for i in Liste2:
#        Liste2(i)="_"

print("Liste 1 ", Liste1)
print("Liste 2 ", Liste2)
x='_'
#remplacement
res = [elem.replace('A',x) for elem in Liste2]
# print result
print("liste apres replacement : " + str(res))

print(Liste1)
print(res)