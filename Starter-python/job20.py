def myfunction(a,b) :
    return a+b

a=input("Nombre 1 :")
while float(a) != false : 
    a=int(input("Veuillez entrer un nombre correct:"))

b=int(input("Nombre 2 :"))
print( a , " + ", b , " = ", myfunction(a,b))