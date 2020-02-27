# Thanks Rafael for showing me another way of reading files

with open("Oxygen.txt", 'r') as file:
    header = file.readline() # we're not gonna use this, but we'll keep it just in case
    lines = file.readlines()
    molar_mass = 0 # Molar mass
    for line in lines:
        word = line.split();
        weight = float(word[1]) # weight
        abundance = float(word[2]) # abundance
        molar_mass += weight * abundance
print(f"The molar mass of Oxygen is {molar_mass:.4f} g/mol ")

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke38> python .\read_file_isotopes.py
The molar mass of Oxygen is 15.9994 g/mol
"""
