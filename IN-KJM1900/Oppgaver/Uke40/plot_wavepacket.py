import numpy as np
import matplotlib.pyplot as plt



def f(x, t):
    return (np.exp(-1*(x-(3*t))**2)) * np.sin(3*np.pi*(x-1))


t_start = 0
x_interval = np.linspace(-4.0, 4.0, 10000000)
t_values = f(x_interval, t_start)

plt.title("Plot_Wavepacket")
plt.xlabel("x")
plt.ylabel("f(x,t)")
plt.plot(x_interval, t_values)
plt.savefig("plot_wavepacket.png")
plt.show()
