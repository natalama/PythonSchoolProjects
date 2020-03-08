import matplotlib.pyplot as plt
import numpy as np

# H =  enthalpy (kJ/mol)
# S = Entropy change (J/mol*K)
# T = Temperature in kelvin
def compute_gibbs_free_energy(T, H, S):
    return H - (T*S)


"""G = H - TS
-S is m and H is our b in y = mx+b"""



# temperatures are in kelvin


MIN_TEMPERATURE = 298
MAX_TEMPERATURE = 1273


temperatures = np.arange(MIN_TEMPERATURE, MAX_TEMPERATURE, 1)
molecular_symbols = []
enthalpies = []
entropies = []
molecule_graph_names = []
delta_h_list = []
minus_delta_s_list = []


with open('Ellingham_data_med_labels.txt') as file:
    # some unknown python bug makes file.readlines(length) not go over that line on the loop.
    for index in range(0,3): #skip first three lines
        file.readline()
    for line in file.readlines():
        print(line)
        words = line.split()
        molecular_symbols.append(words[0])
        enthalpies.append(int(words[1]))
        entropies.append(int(words[2])/1000)
        molecule_graph_names.append(words[3])
print(molecular_symbols)
print(enthalpies)
print(entropies)
print(molecule_graph_names)

"""
def compute_intersection_points(m1,m2,b1,b2):
    if m2-m1 == 0:
        # they do not meet (parallel)
        return np.nan, np.nan
    xi = (b1-b2) / (m2-m1)
    yi = m1 * xi + b1
    print('(xi,yi)', xi, yi)
    return xi, yi
"""

# x1,y1 - first point of first line
# x2,y2 = last point of first line
# x3,y3 = first point of second line
# x4,y4 = last point of second line
def findIntersection(x1,y1,x2,y2,x3,y3,x4,y4):
    px= ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
    py= ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
    return [px, py]

x1 = 0
x2 = 0
x3 = 0
x4 = 0
y1 = 0
y2 = 0
y3 = 0
y4 = 0


for molecular_symbol, enthalpy, entropy, molecule_graph_name in zip(molecular_symbols, enthalpies, entropies, molecule_graph_names):
    gibbs_energies = []
    for temperature in temperatures:
        gibbs_energies.append(compute_gibbs_free_energy(temperature, enthalpy, entropy))
    minus_delta_s, delta_h = np.polyfit(temperatures, gibbs_energies,1)
    delta_h_list.append(delta_h)
    minus_delta_s_list.append(minus_delta_s)
    if molecular_symbol == 'CO':
        x1 = temperatures[0]
        y1 = gibbs_energies[0]
        x2 = temperatures[-1]
        y2 = gibbs_energies[-1]
    if molecular_symbol == 'CO2':
        x3 = temperatures[0]
        y3 = gibbs_energies[0]
        x4 = temperatures[-1]
        y4 = gibbs_energies[-1]
    plt.plot(temperatures, gibbs_energies, label=molecule_graph_name)



c_co_x, c_co_y = findIntersection(x1, y1, x2, y2, x3, y3, x4, y4)
print('skjæringspunktet mellom linjene C/CO og CO/CO2:', c_co_x, c_co_y)
plt.scatter(c_co_x, c_co_y, color = 'black', label = 'Skjæringspunkt C/CO & CO/CO2')
plt.title('Natalie Matic')
plt.legend()
plt.xlabel('Temperatur(K)')
plt.ylabel('$\Delta G (kJ)$')
plt.show()
