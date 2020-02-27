import sys


g = 9.81
v0 = float(sys.argv[1])  # f.eks. 3;
t = float(sys.argv[2])  # f.eks. 0.6
y = v0*t - 0.5*g*t**2
print(y)

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke38> python ball_cml.py 3 0.6
0.034199999999999786
"""
