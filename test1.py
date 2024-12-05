#Készítsen python kódot ami bekér egy egész hőmérséklet értéket 
#és kiírja hogy az adott értéken milyen halmazállapotú a víz.

homersekletC = 0
def homerseklet():
    if homersekletC <= 0:
        return "Sziárd halmazállapt." #igaz ág
    elif homersekletC < 100:
        return "Folyékony halmazállapot."
    else:
        return "Légnemű halmazállapt." #hamis ág
    

homersekletC = int(input("Kérek egy hőmérséklet értéket: ")) 
print(homerseklet())