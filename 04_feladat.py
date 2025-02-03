# Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere 
# mellett fogadhat több paramétert is! Az opcionális paraméterek száma alapján döntse el milyen síkidomról
#  van szó, és számolja ki a kerületét (0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter: téglalap,
#   2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!


def kerulet(elso_param, *opcionalis_param):
    if len(opcionalis_param) == 0:
        # Négyzet (minden oldal egyenlő)
        kerulet = 4 * elso_param
        print(f"Négyzet kerülete: {kerulet}")
    elif len(opcionalis_param) == 1:
        # Téglalap (elso_param: szélesség, opcionalis_param[0]: magasság)
        kerulet = 2 * (elso_param + opcionalis_param[0])
        print(f"Téglalap kerülete: {kerulet}")
    elif len(opcionalis_param) == 2:
        # Háromszög (elso_param: oldal1, opcionalis_param[0]: oldal2, opcionalis_param[1]: oldal3)
        kerulet = elso_param + opcionalis_param[0] + opcionalis_param[1]
        print(f"Háromszög kerülete: {kerulet}")
    else:
        # Sokszög (több mint 3 oldal)
        kerulet = elso_param + sum(opcionalis_param)
        print(f"Sokszög kerülete: {kerulet}")

# Példák a függvény használatára
kerulet(5)  # Négyzet
kerulet(5, 10)  # Téglalap
kerulet(3, 4, 5)  # Háromszög
kerulet(2, 3, 4, 5)  # Sokszög