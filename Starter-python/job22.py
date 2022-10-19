def myUpper(chaine1):
    a=len(chaine1)
    b=0
    c=0
    chaine3=""
    for i in range(a):
        b=ord(chaine1[i]) # ord donne le code ascii d'un caractère
        if (b > 96) & (b < 123):
            c=ord(chaine1[i])-32
            chaine3=chaine3+chr(c)
        else:
            chaine3=chaine3+chaine1[i]
    print(chaine3)

def myLower(chaine1):
    a=len(chaine1)
    b=0
    c=0
    chaine3=""
    for i in range(a):
        b=ord(chaine1[i]) # ord donne le code ascii d'un caractère
        if (b > 64) & (b < 91):
            c=ord(chaine1[i])+32
            chaine3=chaine3+chr(c)
        else:
            chaine3=chaine3+chaine1[i]
    print(chaine3)

def myTitle(chaine1):
    a=len(chaine1)
    b=0
    c=0
    chaine3=""
    for i in range(a):
        b=ord(chaine1[i]) # ord donne le code ascii d'un caractère
        if b==32:
            c=ord(chaine1[i+1])+32
            chaine3=chaine3+chr(c)
        else:
            chaine3=chaine3+chaine1[i+1]
    print(chaine3)

def myClean(chaine1):
    a=len(chaine1)
    b=0
    c=0
    chaine3=""
    for i in range(a):
        b=ord(chaine1[i]) # ord donne le code ascii d'un caractère
        if (b != 32) & (chaine1[i]!=chaine1[i+1]):
            chaine3=chaine3+chaine1[i]
    print(chaine3)

chaine1 = input("1er input : ")
chaine2 = input("2eme input : ")

if chaine2 == "upper":
    myUpper(chaine1)
elif chaine2 == "lower":
    myLower(chaine1)
elif chaine2 == "title":
    myTitle(chaine1)
elif chaine2 == "clean":
    myClean(chaine1)

