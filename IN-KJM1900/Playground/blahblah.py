import numpy as np
from math import exp
from math import sqrt
import matplotlib.pyplot as plt

print("Problem 5.4. Oscillating spring")

print("a)")


n = 101
t = np.zeros(n)
y = np.zeros(n)

gamma = 0.15
k = 4
m = 9
A = 0.3

def y(x):
    gamma = 0.15
    k = 4
    m = 9
    A = 0.3
    z = A*exp((-gamma)*x)*np.cos(sqrt((k/m)*x))
    return z

interval = (25 - 0) /n

for index in range(n):
    t[index] = 0 + (index*interval)
    y[index] = A*exp((-gamma)*t[index])*np.cos(sqrt((k/m)*t[index]))
print(t)
print("---------------------------------------------------------------")
print(y)


print(" ")
print("b)")

t = np.linspace(0,25,101)
y = y(t)

print(len(t))
print(len(y))
plt.plot(t, y)
