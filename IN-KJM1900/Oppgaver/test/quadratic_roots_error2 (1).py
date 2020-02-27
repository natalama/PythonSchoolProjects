# quadratic_roots_error2

#Før
"""
from math import sqrt

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
r = sqrt(b**2-4*a*c)

if r < 0:
    raise ValueError

except ValueError:
    print("disse verdiene gir ikke noe reelt svar")



positiv_x = (-b+r)/2*a
negativ_x = (-b-r)/2*a

print(f"positiv x-verdi er {positiv_x} og negativ x-verdi er {negativ_x}")
"""
# -------------------------------------------------------

# Trinn 1: har "tilbakestilt" koden
"""
from math import sqrt

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
r = sqrt(b**2-4*a*c)

positiv_x = (-b+r)/2*a
negativ_x = (-b-r)/2*a

print(f"positiv x-verdi er {positiv_x} og negativ x-verdi er {negativ_x}")
"""
# -------------------------------------------------------

# trinn 2: satte hele koden under try, og så er det except for å fange opp feilen
# da blir det slik:
"""
from math import sqrt

try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    r = sqrt(b**2-4*a*c)

    positiv_x = (-b+r)/2*a
    negativ_x = (-b-r)/2*a

    print(f"positiv x-verdi er {positiv_x} og negativ x-verdi er {negativ_x}")
except ValueError:
    print("disse verdiene gir ikke noe reelt svar")
"""

# trinn 3: sjekk om b**2-4*a*c er mindre enn 0 istedenfor r < 0
# raise ValueError  hvis b**2-4*a*c < 0
# da blir det sånn:
from math import sqrt

try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    d = b**2-4*a*c
    if d < 0:
        raise ValueError
    r = sqrt(d)

    positiv_x = (-b+r)/2*a
    negativ_x = (-b-r)/2*a

    print(f"positiv x-verdi er {positiv_x} og negativ x-verdi er {negativ_x}")
except ValueError:
    print("disse verdiene gir ikke noe reelt svar")
