# -*-coding: utf-8 -*-
# tatt fra eksempelfila
import numpy as np
import matplotlib.pyplot as plt

def polyprotic_acid(pH, Ka1, Ka2):
	p = 10**(-pH)    						# p = [H+]  (proton)
	a0 = 1/(1 + Ka1/p + Ka1*Ka2/p**2)
	a1 = a0*Ka1/p
	a2 = a1*Ka2/p
	return a0, a1, a2


N = 1000
start_pH = 3
stop_pH = 18
pH = np.linspace(start_pH, stop_pH, N)
Ka1 = 1.1e-7
Ka2 = 1e-14
Ka3 = 0
H2S, HS, S = polyprotic_acid(pH, Ka1, Ka2)


plt.plot(pH, H2S, label='$H_{2}S$')
plt.plot(pH, HS, label='$HS^{1-}$')
plt.plot(pH, S, label='$S^{2-}$')
plt.legend()
plt.axis([start_pH, stop_pH, -0.01, 1.01])
plt.title("Natalie Matic, Hydrogensulfid")
plt.ylabel(r'$\alpha $')
plt.xlabel('pH')
plt.savefig("lab1_KJM1121.png", bbox_inches='tight')
plt.show()
