# Imaginary numbers exist, so I think that cmath is much better than math in this case
import math

roots = []

def get_discriminant(a, b, c):
    return (b**2) - (4*a*c)


def get_roots(a, b, c):
    discriminant = get_discriminant(a,b,c)
    root_1 = (-b-math.sqrt(discriminant))/(2*a)
    root_2 = (-b+math.sqrt(discriminant))/(2*a)
    return [root_1, root_2]


# Keeping it simple. no validations or anything.

run_program = """
while True:
    try:
        a = float(input("Vennligst oppgi verdien til a: "))
        b = float(input("Vennligst oppgi verdien til b: "))
        c = float(input("Vennligst oppgi verdien til c: "))
        discriminant = get_discriminant(a, b, c)
        if (discriminant < 0):
            raise ValueError
    except ValueError:
        print("a , b, og c gir ikke reelle røtter, Vennligst sørg for at a, b, og c gir reelle røtter")
    else:
        roots = get_roots(a, b, c)
        print("Røttene: ")
        for root in (roots):
            print(root)
        break
"""


test_program = """
print("Kjører tester nå... ")
print("Test case 1: bør gi reelle røtter")
test_quadratic_root_real_roots()
print("Test case 1 er vellykket!")
print("Test case 2: bør gi komplekse røtter")
test_quadratic_root_complex_roots()
print("Test case 2 er vellykket!")
print("Ferdig med testing! ")
"""


def test_quadratic_root_real_roots():
    a = 1
    b = 0
    c = -1
    discriminant = get_discriminant(a, b, c)
    assert discriminant > 0, f"{a}, {b}, {c} bør gi reele røtter"


def test_quadratic_root_complex_roots():
    a = 1
    b = 1
    c = 1
    discriminant = get_discriminant(a, b, c)
    assert discriminant < 0, f"{a}, {b}, {c} bør gi reele røtter"



to_do = input("Skriv 'run' for å kjøre programmet, 'test' for å teste programmet, eller hva som helst for å avslutte programmet: ")

if (to_do == "run"):
    exec(run_program)
elif (to_do == "test"):
    exec(test_program)
else:
    print("Programmet er avsluttet")

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\uke38> python .\quadratic_roots_error.py
Skriv 'run' for å kjøre programmet, 'test' for å teste programmet, eller hva som helst for å avslutte programmet: exit

Programmet er avsluttet
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\uke38> python .\quadratic_roots_error.py
Skriv 'run' for å kjøre programmet, 'test' for å teste programmet, eller hva som helst for å avslutte programmet: test

Kjører tester nå...
Test case 1: bør gi reelle røtter
Test case 1 er vellykket!
Test case 2: bør gi komplekse røtter
Test case 2 er vellykket!
Ferdig med testing!
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\uke38> python .\quadratic_roots_error.py
Skriv 'run' for å kjøre programmet, 'test' for å teste programmet, eller hva som helst for å avslutte programmet: run
Vennligst oppgi verdien til a: 1
Vennligst oppgi verdien til b: 0
Vennligst oppgi verdien til c: -1
Røttene:
-1.0
1.0
"""
