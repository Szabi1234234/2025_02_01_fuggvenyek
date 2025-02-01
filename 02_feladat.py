szamok = [1, 3, 5, 7, 9, 2]
def paros_e(szamok):
    for szam in szamok:
        if szam % 2 == 0:
            return True
    return False

print(paros_e(szamok))
