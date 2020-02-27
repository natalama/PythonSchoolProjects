# Imaginary numbers exist, so I think that cmath is much better than math in this case
import sys
import cmath

roots = []


a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])


# this part is called discriminant in math
discriminant = (b**2) - (4*a*c)

root_1 = (-b-cmath.sqrt(discriminant))/(2*a)
root_2 = (-b+cmath.sqrt(discriminant))/(2*a)

print(f"Roots: {root_1} and {root_2}")

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\uke38> python .\quadratic_roots_cml.py 1 0 -1
Roots: (-1+0j) and (1+0j)
"""
