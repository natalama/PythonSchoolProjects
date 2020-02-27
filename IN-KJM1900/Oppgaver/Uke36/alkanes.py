# alkanes.py

CARBON_ATOMIC_MASS = 12.011
HYDROGEN_ATOMIC_MASS = 1.0079


#computes total mass based on atomic mass and number of atoms
def computeTotalMass(atomicMass, amount):
    return atomicMass*amount


# if carbon is n, then hydrogen is 2n+2
# param: n_carbon = number of carbon atoms
# returns number total mass of the alkane
def computeAlkeneTotalMass(n_carbon):
    totalHydrogenMass = computeTotalMass(HYDROGEN_ATOMIC_MASS, (2*n_carbon)+2)
    totalCarbonMass = computeTotalMass(CARBON_ATOMIC_MASS, n_carbon)
    return totalHydrogenMass + totalCarbonMass


# gets the molecular formula for a certain alkene
def getAlkeneFormula(n_carbon):
    return f"C{n_carbon}H{((2*n_carbon)+2)}"


# I'm not sure about the range
for n in range(2, 10):
    alkane = f"M({getAlkeneFormula(n)})"
    print(f"{alkane:9} = {computeAlkeneTotalMass(n):.3f} g/mol")

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke36> python .\alkanes.py
M(C2H6)   = 30.069 g/mol
M(C3H8)   = 44.096 g/mol
M(C4H10)  = 58.123 g/mol
M(C5H12)  = 72.150 g/mol
M(C6H14)  = 86.177 g/mol
M(C7H16)  = 100.203 g/mol
M(C8H18)  = 114.230 g/mol
M(C9H20)  = 128.257 g/mol
"""
