
# coding: utf-8

# In[22]:


# Given in the problem.
"""N(t) = B /(1 + Ce**−(k*t))
N(t) = population
B – carryingCapacity = maximum size of the
that the environment can sustain indefinitely
N(t) = population at the specified time
t = Time
C = given by initial conditions
k tells us something about how fast the population grow

B = 50000
k = 0.2 h**−1

Find:_
C if population = 5000 at t = 0

Find number of bacteria after 24 hours

Solution:
C = (B/N(t) - 1)/e**(-kt)
"""
import numpy as np

CARRYING_CAPACITY = 50000
POPULATION_GROWTH_RATE = 0.2

time_0 = 0.
population_0 = 5000
time_24 = 24.


def findInitialCondition(populationAtTime, time):
    return ((CARRYING_CAPACITY/populationAtTime) -1)/(np.exp(-1*POPULATION_GROWTH_RATE*time))


def findPopulation(initialCondition, time):
    return CARRYING_CAPACITY/(1+(initialCondition*(np.exp(-1*POPULATION_GROWTH_RATE*time))))


initialCondition = findInitialCondition(population_0, time_0)
print(f"Intitial condition: {initialCondition}")
# population is obviously in whole number;can't have 0.27 bacterias
print(f"Population after {time_24:.0f} hours:{findPopulation(initialCondition, time_24):.0f}")

# had to add r at the start of comment due to unicode error
# https://stackoverflow.com/questions/1347791/unicode-error-unicodeescape-codec-cant-decode-bytes-cannot-open-text-file
r"""#PS C:\Users\Min PC\Downloads> python .\population.py
#Intitial condition: 9.0
#Population after 24 hours:46552"""
