liste = ['Python', '5', 'py', '4', 'PHP', '8']
x='7'
# affichage de la liste
print("liste originale : " + str(liste))
#remplacement
res = [elem.replace('5', x) for elem in liste]
# print result
print("liste apres replacement : " + str(res))