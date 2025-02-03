# 5. Feladat
# Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír! 
# A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvények, amely
#  a lista legkisebb elemével tér vissza. A program írja ki, hogy melyik volt a megadott legkisebb szám!
szamok = []
def legkisebb(szamok):
    while True:
        try:
            szam = int(input("MOndj pozitiv szamokat "))
            szamok.append(szam)
            if szam < 0:
                break
            

        except ValueError:
                print("Nem jo")

def frlegkisebb(szamok):
    return min(szamok)


print(frlegkisebb(szamok))