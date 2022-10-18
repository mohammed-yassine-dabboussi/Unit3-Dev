#Job 11 parcourir le contenu d'un fichier xml et compter le nombre de noms de domaine
with open("domains.xml") as f:
    contents = f.read()
    count = contents.count("domain")
print(count)