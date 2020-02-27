# Imaginary numbers exist, so I think that cmath is much better than math in this case
import cmath

roots = []

# Keeping it simple. no validations or anything.

print("Vennligst oppgi verdien til a: ", end='')
a = float(input())
print("Vennligst oppgi verdien til b: ", end='')
b = float(input())
print("Vennligst oppgi verdien til c: ", end='')
c = float(input())


# this part is called discriminant in math
discriminant = (b**2) - (4*a*c)

root_1 = (-b-cmath.sqrt(discriminant))/(2*a)
root_2 = (-b+cmath.sqrt(discriminant))/(2*a)

print(f"Roots: {root_1} and {root_2}")

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\uke38> python .\quadratic_roots_input.py
Vennligst oppgi verdien til a: 1
Vennligst oppgi verdien til b: 0
Vennligst oppgi verdien til c: -1
Roots: (-1+0j) and (1+0j)
"""
