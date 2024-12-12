import math
def torlesztoreszlet(p, r, n):
    kamatlab = r / 100 / 12 #Éves kamat százaléból havi tört formában
    return (p * kamatlab * (1 + kamatlab) ** n) / ((1 + kamatlab) ** n - 1)


if __name__ == "__main__":
    hitelosszeg = float(input("Kérem a hitel összegét (forint): "))
    eves_kamat = float(input("Kérem aaz éves kamatlábat (%): "))
    futamido = float(input("Kérem a futamidőt (hónapokban): "))
    
    havi_torleszto = torlesztoreszlet(hitelosszeg,eves_kamat,futamido)

    print(f"A havi törlesztőrészlet: {round(havi_torleszto)} Ft")