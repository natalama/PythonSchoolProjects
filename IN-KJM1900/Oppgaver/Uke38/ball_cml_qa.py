import sys


g = 9.81
v0 = 0.0

try:
    v0 = float(sys.argv[1])  # f.eks. 3;
except IndexError:
    print("v0 kreves. Vennligst skriv verdien til v0: ", end = '')
    while True:
        try:
            v0 = float(input())
        except ValueError:
            print("Ugyldig verdi. Vennligst skriv verdien til v0: ",end = '')
        else:
            break;

try:
    t = float(sys.argv[2])  # f.eks. 0.6;
except IndexError:
    print("t kreves. Vennligst skriv verdien til t:", end = '')
    while True:
        try:
            t = float(input())
        except ValueError:
            print("Ugyldig verdi. Vennligst skriv verdien til t: ", end = '')
        else:
            break;


y = v0*t - 0.5*g*t**2
print(y)

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke38> python ball_cml_qa.py
v0 kreves. Vennligst skriv verdien til v0: test
Ugyldig verdi. Vennligst skriv verdien til v0: test2
Ugyldig verdi. Vennligst skriv verdien til v0: 3
t kreves. Vennligst skriv verdien til t:abcd
Ugyldig verdi. Vennligst skriv verdien til t: 0.6
0.034199999999999786
"""
