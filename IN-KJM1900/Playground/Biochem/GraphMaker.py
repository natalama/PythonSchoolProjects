import numpy as np
import matplotlib.pyplot as plt
import sys


def reciprocal(x):
    return 1/x

include_wrong_source=True # inkluder data med feilkilde hvis satt til Trie
trial_numbers = [sys.argv[index] for index in range(1,len(sys.argv))]
concentrations = [np.loadtxt(f"Substratkonsentrasjon_Trial{trial_number}.csv", dtype="float", delimiter=';') for trial_number in trial_numbers]
enzyme_kinetic_names = [f"Trial{trial_number}_Enzyme_Kinetics"+".csv" for trial_number in trial_numbers]

for enzyme_kinetic_name in enzyme_kinetic_names:
    include_wrong_source = enzyme_kinetic_names.index(enzyme_kinetic_name) == 0 #
    enzyme_kinetics = np.loadtxt(enzyme_kinetic_name, dtype='float', delimiter=';', skiprows = 1)
    time_list = enzyme_kinetics[:,0]
    absorbances = []
    V0_list = []
    for index in range(1, len(enzyme_kinetics[0])):
        absorbance = enzyme_kinetics[:,index]
        absorbances.append(absorbance)
        [V0, I] = np.polyfit(time_list, absorbance, 1)
        V0_list.append(V0)
        line = np.poly1d([V0,I])
        plt.plot(time_list, absorbance, "o", time_list, line(time_list), label= f"Forsøk {index}")
    plt.legend()
    plt.ylabel(r'Absorbans', fontsize=15)
    plt.xlabel("tid [min]", fontsize=15)
    plt.grid(color='grey', linestyle ='-', linewidth =0.4)
    plt.show()
    plt.plot(concentrations[enzyme_kinetic_names.index(enzyme_kinetic_name)], V0_list, "o-")
    plt.ylabel(r'Reaksjonshastighet', fontsize=15)
    plt.xlabel("Substratkonsentrasjon [enheter]", fontsize=15)
    plt.grid(color='grey', linestyle ='-', linewidth =0.4)
    plt.show()
    plt.plot()
    V0_rec_list = [reciprocal(V0) for V0 in V0_list]
    S_rec_list = [reciprocal(concentration) for concentration in concentrations[enzyme_kinetic_names.index(enzyme_kinetic_name)]]
    [Km_vmax,vmax_rec] = np.polyfit(S_rec_list, V0_rec_list, 1)
    vmax=reciprocal(vmax_rec)
    km=Km_vmax * vmax
    print('slope=', km/vmax,'\n','V_max=', vmax,'\n','Reaction constant =',km)
    line = np.poly1d([Km_vmax, vmax_rec])
    plt.plot(S_rec_list, V0_rec_list, "o", S_rec_list, line(S_rec_list))
    plt.ylabel(r'1/v', fontsize=15)
    plt.xlabel("1/[s]", fontsize=15)
    plt.grid(color='grey', linestyle ='-', linewidth =0.4)
    plt.show()
