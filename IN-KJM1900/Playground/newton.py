import numpy as np
import sys


def f(x):
    return np.sin(x)


# veit ikke om dette stemmer
def derivert_f(x):
    return np.cos(x)


x = np.zeros(3)
x[0] = sys.argv[1]


# neste element er basert på forrige lement
for n in range(1,3):
    x[n] = x[n-1] - (f(x[n-1])/derivert_f(x[n-1]))

print("from newton's method:")
for element in x:
    print(f"{element:.14f}")
print(f"from numpy: {np.pi:.14f}")
