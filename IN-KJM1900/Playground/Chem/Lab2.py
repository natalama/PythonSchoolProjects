import math

DONE_COMMAND = "done"
GAS_CONSTANT = 0.0821


def extract_data(filename):
    dict_temp_pressure = {}
    with open(filename, "r") as file:
        header = file.readline()
        lines = file.readlines()
        for line in lines:
            words = line.split()
            dict_temp_pressure.update({words[0]: float(words[1].strip("'"))})
    return dict_temp_pressure


dict_temp_pressure = extract_data("temp_pressure.txt")


def celsius_to_kelvin(celsius):
    return celsius + 273

def cm_to_mm(centimeters):
    return centimeters*10

def ml_to_l(milliliters):
    return milliliters/1000

def compute_pressure_vanndamp(temperature):
    temperature = f"{temperature:.1f}"
    if temperature in dict_temp_pressure:
        pressure_vanndamp = dict_temp_pressure[temperature]
    else:
        float_temp = float(temperature)
        float_temp_1 = float_temp-1
        float_temp_2 = float_temp+1
        pressure_1 = dict_temp_pressure[str(float_temp_1)]
        pressure_2 = dict_temp_pressure[str(float_temp_2)]
        pressure_vanndamp = (((pressure_1 - pressure_2)/(float_temp_1 - float_temp_2)) * (float(temperature) - float_temp_2))+pressure_2
    return pressure_vanndamp


def compute_pressure_vannsoeyle(height_vannsoeyle):
    return 0.0000967 * height_vannsoeyle


def compute_pressure_hydrogen_gas(p0, pressure_vanndamp, pressure_vannsoeyle):
    return (p0 - pressure_vanndamp) - pressure_vannsoeyle


def compute_molar_mass(temperature, pressure_hydrogen_gas, volume_gass, mass_element):
    return ((GAS_CONSTANT*temperature)/(pressure_hydrogen_gas*volume_gass))*mass_element


def Funk_gjennomsnitt(liste):
    sum_av_x = sum(liste)        # vi bruker python funksjonen sum til å summere over alle verdier i listen
    lengde_av_liste = len(liste) # bruker python funksjonen len til å finne ut verdien til n (antall målepunkter)
    gj_snitt = sum_av_x / lengde_av_liste
    return gj_snitt


# Funksjon som regner ut standardavvik og realtivt standardavvik
def Funk_standardavvik(liste):
    gjennomsnitt = Funk_gjennomsnitt(liste)
    n = len(liste)
    sum_differanse_kvadrat = 0
    for val in liste:
        differanse_kvadrat=(val-gjennomsnitt)**2
        sum_differanse_kvadrat=differanse_kvadrat + sum_differanse_kvadrat

    std_avvik = ((1/(n-1))*sum_differanse_kvadrat)**0.5
    rel_std_avvik = std_avvik/gjennomsnitt
    return std_avvik, rel_std_avvik


# lagre input her
list_mass_magnesium = []
list_gas_volume = []
list_p0 = []
list_temperature = []
list_pressure_vann =[]
list_height_vannsoeyle = []

# disse dataene må vi beregne
list_pressure_vanndamp = []
list_pressure_vannsoeyle = []
list_pressure_H2 = []
list_molar_mass_magnesium = []


print("Henter dataene fra fila...")
with(open("input_data.txt")) as infile:
    list_mass_magnesium = [float(mass) for mass in infile.readline().split()]
    list_gas_volume = [float(gas_volume) for gas_volume in infile.readline().split()]
    list_p0 = [float(p0) for p0 in infile.readline().split()]
    list_temperature = [float(temperature) for temperature in infile.readline().split()]
    list_height_vannsoeyle = [cm_to_mm(float(vannsoeyle)) for vannsoeyle in infile.readline().split()]

print("Beregner resultatene...")
for mass_magnesium, gas_volume, p0, temperature, height_vannsoeyle in zip(list_mass_magnesium, list_gas_volume, list_p0, list_temperature, list_height_vannsoeyle):

    pressure_vanndamp = compute_pressure_vanndamp(temperature)
    pressure_vannsoeyle = compute_pressure_vannsoeyle(height_vannsoeyle)
    pressure_hydrogen_gas = compute_pressure_hydrogen_gas(round(p0, 4), round(pressure_vanndamp, 4), round(pressure_vannsoeyle, 4))

    list_pressure_vannsoeyle.append(pressure_vannsoeyle)
    list_pressure_vanndamp.append(pressure_vanndamp)
    list_pressure_H2.append(pressure_hydrogen_gas)
    list_molar_mass_magnesium.append(compute_molar_mass(celsius_to_kelvin(temperature), pressure_hydrogen_gas,4, ml_to_l(gas_volume), mass_magnesium))
print("Ferdig med å beregne...")
print("Skriver ut resultatene...")

for i in range(len(list_pressure_H2)):
    print(f"Replika {i+1}")
    print(f"P_vanndamp = {list_pressure_vanndamp[i]}")
    print(f"P_vannsoeyle = {list_pressure_vannsoeyle[i]:.4f}")
    print(f"P_H2 = {list_pressure_H2[i]}")
    print(f"list_molar_mass_magnesium = {list_molar_mass_magnesium[i]}")
    print("-----------------------------")
metal_molar_mass_standardavvik, metal_molar_mass_relativtstandardavvik = Funk_standardavvik(list_molar_mass_magnesium)
print('gjennomsnitt:', Funk_gjennomsnitt(list_molar_mass_magnesium), 'g/mol')
print('standardavvik:', metal_molar_mass_standardavvik, 'g/mol')
print('relativt standardavvik:', metal_molar_mass_relativtstandardavvik  * 100, '%')
