import numpy.random as rnd

N = 10000
my_list = [rnd.randint(1,7) for index in range(N)]
seksere = my_list.count(6)
enere = my_list.count(1)


print("Antall enere: ", enere)
print("Antall seksere: ", seksere)
print("frekvens seksere: ", seksere/N)
