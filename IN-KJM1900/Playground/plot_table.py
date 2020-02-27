import numpy as np
import matplotlib.pyplot as plt
import sys

g = 9.81
n = 101

for v0 in sys.argv[1:]:
    v0 = float(v0);
    t_stop = 2**v0/g
    t = np.linspace(0, t_stop,n)
    y = v0*t - 0.5*g*t**2
    plt.plot(t, y)

plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.show()
