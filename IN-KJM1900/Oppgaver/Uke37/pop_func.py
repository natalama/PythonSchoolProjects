import numpy as np

TIME_0 = 0
POPULATION_0 = 5000
CARRYING_CAPACITY = 50000
POPULATION_GROWTH_RATE = 0.2

# quite weird to not have the functions in a separate class/file.
# It makes it reusable and movable anywhere,
# but I'll follow the comment from previous week


def findInitialCondition(populationAtTime, time):
    return ((CARRYING_CAPACITY/populationAtTime) -1)/(np.exp(-1*POPULATION_GROWTH_RATE*time));


def population(t, k, B, C):
    # kinda weird to use the variables t,k,B,C, but it's required
    return B/(1+(C*(np.exp(-1*k*t))))


# get the initial condition
initialCondition = findInitialCondition(POPULATION_0,  TIME_0)
startTime = 0.  # start time
endTime = 48.  # end time
n = 12

interval = (endTime-startTime)/n

times = []  # represents the list of times
populations = []  # represents the list of populations

currentTime = startTime
while (currentTime <= endTime):
    # I decided to use math.floor since 49969.xxxx means that the 49970th bacteria isn't born yet
    pop = np.floor(population(currentTime, POPULATION_GROWTH_RATE, CARRYING_CAPACITY, initialCondition))
    times.append(currentTime)
    currentTime += interval
    populations.append(pop)

print("Time   | Population")
for index in range(0, n+1):
    print(f"{times[index]:3.0f}    | {populations[index]:.0f}")

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke37> python .\pop_func.py
Time   | Population
  0    | 5000
  4    | 9912
  8    | 17748
 12    | 27526
 16    | 36580
 20    | 42924
 24    | 46551
 28    | 48389
 32    | 49263
 36    | 49666
 40    | 49849
 44    | 49932
 48    | 49969
"""
