val1 = input("Valeur 1 : ")
val2 = input("Valeur 2 : ")
a=int(val1)
b=int(val2)
if a == b:
    print("Valeurs égales")
elif a < b:
    for i in range(a+1,b):
        print(i)
else: 
    for i in range(b-1,a):
        print(i)