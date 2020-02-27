import numpy as np
import matplotlib.pyplot as plt

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32.0)/1.8


def fahrenheit_to_approx_celsius(fahrenheit):
    return (fahrenheit - 30)/2


fahrenheit_range = np.linspace(-20, 120, 20)

celsius_range = fahrenheit_to_celsius(fahrenheit_range)
approx_celsius_range = fahrenheit_to_approx_celsius(fahrenheit_range)

plt.title("F2C Shortcut Graph")
plt.xlabel("Celsius")
plt.ylabel("Fahrenheit")
plt.plot(celsius_range, fahrenheit_range, "--", label = "celsius vs fahrenheit", marker="o")
plt.plot(approx_celsius_range, fahrenheit_range, "--", label = "approx. celsius vs fahrenheit",marker="o")
plt.legend()
plt.savefig("F2c_shortcut_plot_graph.png")
plt.show()

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke40> python .\f2c_shortcut_plot.py
"""
