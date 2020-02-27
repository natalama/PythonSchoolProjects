import numpy as np

TIME_0 = 0.
POPULATION_0 = 5000
CARRYING_CAPACITY = 50000
POPULATION_GROWTH_RATE = 0.2


# Still very weird to not separate these methods in a utility .py file or class
# so that it will be perfectly reusable/movable
def findInitialCondition(populationAtTime, time):
    return ((CARRYING_CAPACITY/populationAtTime) -1)/(np.exp(-1*POPULATION_GROWTH_RATE*time));


def findPopulation(initialCondition, time):
    return CARRYING_CAPACITY/(1+(initialCondition*(np.exp(-1*POPULATION_GROWTH_RATE*time))));


initialCondition = findInitialCondition(POPULATION_0,  TIME_0) # get the initial condition
startTime = 0  # start time
endTime = 48  # end time
n = 12

interval = (endTime-startTime)/n

times = []  # represents the list of times
populations = []  # represents the list of populations
currentTime = startTime
while (currentTime <= endTime):
     # I decided to use math.floor since 49969.xxxx means that the 49970th bacteria isn't born yet
    population = np.floor(findPopulation(initialCondition, currentTime))
    times.append(currentTime)
    currentTime += interval
    populations.append(population)

# very ugly naming, but it was specified in the problem/requirements. oh well..
tN1 = []
# not sure if tn1[0} will hold the list of t and tN[1] will hold N
tN1.insert(0,times)
tN1.insert(1,populations)

print("a. ) ")

print("Time | Population")
for index in range(0, n+1):
    print(f"{tN1[0][index]:4.0f} | {tN1[1][index]:.0f}")

print("-----------------")

print("b. ) ")

# trying list comprehension for the first time.
tN2 = ((tN1[0][index], tN1[1][index]) for index in range(0, len(tN1[0])))

for time_population_element in tN2:
    print(f"{time_population_element[0]:4.0f} | {time_population_element[1]:.0f}")

r"""
Terminal> python .\population_table2.py
a. )
Time | Population
   0 | 5000
   4 | 9912
   8 | 17748
  12 | 27526
  16 | 36580
  20 | 42924
  24 | 46551
  28 | 48389
  32 | 49263
  36 | 49666
  40 | 49849
  44 | 49932
  48 | 49969
-----------------
b. )
   0 | 5000
   4 | 9912
   8 | 17748
  12 | 27526
  16 | 36580
  20 | 42924
  24 | 46551
  28 | 48389
  32 | 49263
  36 | 49666
  40 | 49849
  44 | 49932
  48 | 49969
"""
