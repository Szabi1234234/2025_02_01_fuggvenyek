# Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab 
# hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!

# 3.2 Feladat
# Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje ki a függvény!
#  (Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)
szamok_lista = []
def harommaloszthatokb(szamok):
    szamaim = 0
    for szam in szamok:
        if szam % 3 == 0:
            szamaim += 1
            
    return szamaim


szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
        try:
            szam = int(input("adj meg számokat "))
            if szam < 0:
                break
            szamok_lista.append(szam)
        except ValueError:
            print("Kérlek, érvényes számot adj meg!")

print(harommaloszthatokb(szamok))

    