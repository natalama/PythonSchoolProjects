import matplotlib.pyplot as plt
import numpy as np

# H =  enthalpy (kJ/mol)
# S = Entropy change (J/mol*K)
# T = Temperature in kelvin
def compute_gibbs_free_energy(T, H, S):
    return H - (T*S)


#temperatures are in kelvin
MIN_TEMPERATURE = 298
MAX_TEMPERATURE = 1273


temperatures = np.arange(MIN_TEMPERATURE , MAX_TEMPERATURE , 1)
molecular_symbols = []
enthalpies = []
entropies = []
molecule_graph_names = []

with open('Ellingham_data_med_labels.txt') as file:
    #some unknown python bug makes file.readlines(length) not go over that line on the loop.
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


for enthalpy, entropy, molecule_graph_name in zip(enthalpies, entropies, molecule_graph_names):
    gibbs_energies = []
    for temperature in temperatures:
        gibbs_energies.append(compute_gibbs_free_energy(temperature, enthalpy, entropy))
    plt.plot(temperatures, gibbs_energies, label=molecule_graph_name)
plt.title('Natalie Matic')
plt.legend()
plt.xlabel('Temperatur(K)')
plt.ylabel('$\Delta G (kJ)$')
plt.show()
