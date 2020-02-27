from numpy import pi as PI
import numpy as np
import matplotlib.pyplot as plt


N_START = 1
N_END = 4


def f(x,n):
    part_2 = 0
    for n_elem in range (N_START, n+1):
        part_2 += np.cos(((2*n_elem) - 1) *x)/((2*n_elem -1)**2)
    approx_abs = (PI/2) - ((4/PI)* part_2)
    return approx_abs



x_axis = np.linspace(-PI, PI, 101)
n_range = np.arange(N_START,N_END+1)



plt.plot(x_axis, abs(x_axis), "--", label = "exact abs")

for n in n_range:
    approx_abs_x = f(x_axis, n)
    plt.plot(x_axis, approx_abs_x, "--", label = f"n = {n}")

plt.title("Approx. abs")
plt.xlabel("x")
plt.ylabel("f(x,t)")
plt.legend()
plt.savefig("approx_abs_graph.png")
plt.show()

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke40> python .\approx_abs.py
"""
