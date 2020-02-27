import numpy as np

CARRYING_CAPACITY = 50000
POPULATION_GROWTH_RATE = 0.2

def findInitialCondition(populationAtTime, time):
    return ((CARRYING_CAPACITY/populationAtTime) -1)/(np.exp(-1*POPULATION_GROWTH_RATE*time));


def findPopulation(initialCondition, time):
    return CARRYING_CAPACITY/(1+(initialCondition*(np.exp(-1*POPULATION_GROWTH_RATE*time))));
