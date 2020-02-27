import numpy as np
import matplotlib.pyplot as plt


def P(V,T,n):
    R = 8.314
    return n*R*T/V


V_array = np.linspace(1, 20, 1000)
P_array = P(V_array, 290, 1)

plt.plot(V_array,P_array, linestyle = ' ', marker = 'o')
plt.xlabel("Volum(dm$^3$)")
plt.ylabel("Trykk(Pa)")
plt.title('Trykkmålinga')
plt.grid()
plt.show()
