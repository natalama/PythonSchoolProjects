import matplotlib.pyplot as plt
import numpy as np


# konsentrasjon = np.asarray([0, 0.125, 0.25, 0.5, 0.75, 1.0, 1.5])  # konsentrasjon her
# absorbance = np.asarray([0, 0.007, 0.316, 0.747, 0.910, 1.019, 1.155])  # absorbans her

konsentrasjon = np.asarray([0, 0.125, 0.25, 0.5, 0.75, 1.0, 1.5])  # konsentrasjon her
absorbance = np.asarray([0, 0.007, 0.316, 0.747, 0.910, 1.019, 1.155])  # absorbans her

poly = np.polyfit(konsentrasjon, absorbance, 4)

#  lage linear funksjon
# y = ax + b
 y = lambda a,b,x: a*x+b

# y = lambda a,b,c,x: a*x**2 + b*x + c
# g = lambda a,b,c,x: a*x**2+b*x+c

plt.title("Absorbans vs Konsentrasjon")
plt.plot(konsentrasjon, y(float(poly[0]), float(poly[1]), konsentrasjon))
plt.plot(konsentrasjon, absorbance, 'o')
plt.xlabel("konsentrasjon (mg/ml)")
plt.ylabel("absorbance")
plt.legend()
plt.savefig("graph.png")
plt.show()
