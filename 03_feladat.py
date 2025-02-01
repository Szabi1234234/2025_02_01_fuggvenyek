# Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab 
# hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!
szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def harommal_oszthatok(szamok_):
#     harommal_oszthatok = []
#     for szam in szamok_:
#         if szam % 3 == 0:
#             harommal_oszthatok.append(szam)
#     print(harommal_oszthatok)
#     return len(harommal_oszthatok)
    
# print(szamok)
# print(harommal_oszthatok(szamok))


def harommaloszthatokb(szamok):

    szamaim = 0 
for szam in szamok:
    if szam % 3 == 0:
        szamaim += 1
return szamaim
print(szamaim)
print(harommaloszthatokb(szamok))

    