# Imaginary numbers exist, so I think that cmath is much better than math in this case
import sys
import cmath

# gadd ikke å lage metoder for de 3. kunne gjort det bedre.
try:
    a = float(sys.argv[1])
except IndexError:
    a = float(input("Du mangler a. Vennligst skriv verdien til a: "))

try:
    b = float(sys.argv[2])
except IndexError:
    b = float(input("Du mangler b. Vennligst skriv verdien til b: "))

try:
    c = float(sys.argv[3])
except IndexError:
    c = float(input("Du mangler c. Vennligst skriv verdien til c: "))


# this part is called discriminant in math
discriminant = (b**2) - (4*a*c)

root_1 = (-b-cmath.sqrt(discriminant))/(2*a)
root_2 = (-b+cmath.sqrt(discriminant))/(2*a)

print(f"Roots: {root_1} and {root_2}")

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke38> python .\quadratic_roots_error.py
Du mangler a. Vennligst skriv verdien til a: 1
Du mangler b. Vennligst skriv verdien til b: 0
Du mangler c. Vennligst skriv verdien til c: -1
Roots: (-1+0j) and (1+0j)
"""
