# I will reuse the functions that i had in population
# import the utility class
import PopulationUtils as popUtils
import math

TIME_0 = 0.
POPULATION_0 = 5000

# get the initial condition
initialCondition = popUtils.findInitialCondition(POPULATION_0,  TIME_0)
startTime = 0  # start time
endTime = 48  # end time
n = 12

interval = (endTime-startTime)/n

times = []  # represents the list of times
populations = []  # represents the list of populations

currentTime = startTime
while (currentTime <= endTime):
    population = math.floor(popUtils.findPopulation(initialCondition, currentTime))
    times.append(currentTime)
    currentTime += interval
    populations.append(population)

print("Time   | Population")
for index in range(0, n+1):
    print(f"{times[index]:3.0f}    | {populations[index]:.0f}")

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke36> python .\population_table.py
Time   | Population
  0    | 5000
  4    | 9913
  8    | 17749
 12    | 27526
 16    | 36580
 20    | 42924
 24    | 46552
 28    | 48390
 32    | 49263
 36    | 49666
 40    | 49849
 44    | 49932
 48    | 49970
"""
