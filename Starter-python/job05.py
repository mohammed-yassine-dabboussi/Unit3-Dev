val1 = int(input("Valeur 1 : "))
val2 = int(input("Valeur 2 : "))
if val1 == val2:
    print("Valeurs égales")
elif val1 < val2:
    for i in range(val1+1,val2):
        print(i)
else: 
    i = val1
    while i > val2+1:        
        i = i-1
        print(i)