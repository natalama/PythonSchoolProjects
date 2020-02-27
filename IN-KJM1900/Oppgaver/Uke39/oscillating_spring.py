import numpy as np
import matplotlib.pyplot as plt


mass_rock = 9 # kg
length = 0.3 # meters
FRICTION_COEFFICIENT = 0.15 # s**-1
SPRING_CONSTANT = 4. # kg s**-2


# parameters: t - time in seconds
# returns vertical position of the rock
def y(t):
    return (length*np.exp(-1*FRICTION_COEFFICIENT*t))*np.cos(np.sqrt((SPRING_CONSTANT/mass_rock)*t))


def print_lists(t_array, y_array):
    for index in range(len(t_array)):
        print(f"{t_array[index]:2.18f} {y_array[index]:2.18f}")


# Please don't blame me about the output.
size = 101
t_array = np.zeros(size)

y_array = np.zeros(size)
end_time = 25.
start_time = 0.
interval = (end_time - start_time)/(size-1)
current_time = 0

print("Using method 1: with for-loop")
for index in range(size):
    current_time = start_time + (interval*index)
    t_array[index] = current_time
    y_array[index] = y(current_time)
print_lists(t_array, y_array)
print("end of method 1, copying the lists for future use")

t_array_exercise_1 = t_array.copy()
y_array_exercise_1 = y_array.copy()

print("Using method 2: linspace and vectorized ")

t_array_2 = np.linspace(start_time, end_time, size)
y_array_2 = y(t_array)
print_lists(t_array_2, y_array_2)
print("end of method 2...")
print("making graphs..")
plt.title("exercise 1 vs exercise 2")
plt.plot(t_array_2,y_array_2, label = "exercise 2")
plt.plot(t_array_exercise_1,y_array_exercise_1, label = "exercise 1")
plt.xlabel("time (seconds)")
plt.ylabel("vertical position (meter)")
plt.legend()
plt.savefig("oscillating_spring_graph.png")
plt.show()
r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke39> python .\oscillating_spring.py
Using method 1: with for-loop
0.000000000000000000 0.299999999999999989
0.250000000000000000 0.273053176703060896
0.500000000000000000 0.247966718894815252
0.750000000000000000 0.224626735901728075
1.000000000000000000 0.202925830176467592
1.250000000000000000 0.182762744496022145
1.500000000000000000 0.164042027666606055
1.750000000000000000 0.146673717790536978
2.000000000000000000 0.130573042197463685
2.250000000000000000 0.115660133187206360
2.500000000000000000 0.101859758774149239
2.750000000000000000 0.089101067663707470
3.000000000000000000 0.077317347729973659
3.250000000000000000 0.066445797300337575
3.500000000000000000 0.056427308587748998
3.750000000000000000 0.047206262644454398
4.000000000000000000 0.038730335242560636
4.250000000000000000 0.030950313116744881
4.500000000000000000 0.023819920032916261
4.750000000000000000 0.017295652173709861
5.000000000000000000 0.011336622357430538
5.250000000000000000 0.005904412631524745
5.500000000000000000 0.000962934804905312
5.750000000000000000 -0.003521701494450676
6.000000000000000000 -0.007581313629215667
6.250000000000000000 -0.011245764002368871
6.500000000000000000 -0.014543071700469415
6.750000000000000000 -0.017499518066203288
7.000000000000000000 -0.020139746518744655
7.250000000000000000 -0.022486856924209746
7.500000000000000000 -0.024562494803030899
7.750000000000000000 -0.026386935646401072
8.000000000000000000 -0.027979164599994392
8.250000000000000000 -0.029356951759925077
8.500000000000000000 -0.030536923313324527
8.750000000000000000 -0.031534628743968118
9.000000000000000000 -0.032364604312033328
9.250000000000000000 -0.033040433006292717
9.500000000000000000 -0.033574801156809497
9.750000000000000000 -0.033979551886482433
10.000000000000000000 -0.034265735570558842
10.250000000000000000 -0.034443657464468300
10.500000000000000000 -0.034522922652010971
10.750000000000000000 -0.034512478458033596
11.000000000000000000 -0.034420654462226502
11.250000000000000000 -0.034255200243556549
11.500000000000000000 -0.034023320978092020
11.750000000000000000 -0.033731711006561867
12.000000000000000000 -0.033386585481902695
12.250000000000000000 -0.032993710201270232
12.500000000000000000 -0.032558429721506903
12.750000000000000000 -0.032085693851855383
13.000000000000000000 -0.031580082612769629
13.250000000000000000 -0.031045829744990115
13.500000000000000000 -0.030486844848605806
13.750000000000000000 -0.029906734227607982
14.000000000000000000 -0.029308820511441333
14.250000000000000000 -0.028696161121263049
14.500000000000000000 -0.028071565645021508
14.750000000000000000 -0.027437612182052842
15.000000000000000000 -0.026796662714655951
15.250000000000000000 -0.026150877561036887
15.500000000000000000 -0.025502228961102200
15.750000000000000000 -0.024852513843820555
16.000000000000000000 -0.024203365822255265
16.250000000000000000 -0.023556266459888883
16.500000000000000000 -0.022912555849509453
16.750000000000000000 -0.022273442543698608
17.000000000000000000 -0.021640012873848664
17.250000000000000000 -0.021013239692633346
17.500000000000000000 -0.020393990572958997
17.750000000000000000 -0.019783035494624818
18.000000000000000000 -0.019181054048216954
18.250000000000000000 -0.018588642184146669
18.500000000000000000 -0.018006318533213998
18.750000000000000000 -0.017434530323629009
19.000000000000000000 -0.016873658918051336
19.250000000000000000 -0.016324024992908637
19.500000000000000000 -0.015785893381024190
19.750000000000000000 -0.015259477597418558
20.000000000000000000 -0.014744944067046633
20.250000000000000000 -0.014242416072187054
20.500000000000000000 -0.013751977436211952
20.750000000000000000 -0.013273675959528951
21.000000000000000000 -0.012807526622601630
21.250000000000000000 -0.012353514570115989
21.500000000000000000 -0.011911597889567400
21.750000000000000000 -0.011481710196791759
22.000000000000000000 -0.011063763040254453
22.250000000000000000 -0.010657648135239050
22.500000000000000000 -0.010263239438442219
22.750000000000000000 -0.009880395072880467
23.000000000000000000 -0.009508959112446098
23.250000000000000000 -0.009148763234912493
23.500000000000000000 -0.008799628251680935
23.750000000000000000 -0.008461365522080931
24.000000000000000000 -0.008133778259582282
24.250000000000000000 -0.007816662736848220
24.500000000000000000 -0.007509809396153650
24.750000000000000000 -0.007213003871309663
25.000000000000000000 -0.006926027926873753
end of method 1, copying the lists for future use
Using method 2: linspace and vectorized
0.000000000000000000 0.299999999999999989
0.250000000000000000 0.273053176703060896
0.500000000000000000 0.247966718894815252
0.750000000000000000 0.224626735901728075
1.000000000000000000 0.202925830176467592
1.250000000000000000 0.182762744496022145
1.500000000000000000 0.164042027666606055
1.750000000000000000 0.146673717790536978
2.000000000000000000 0.130573042197463685
2.250000000000000000 0.115660133187206360
2.500000000000000000 0.101859758774149239
2.750000000000000000 0.089101067663707470
3.000000000000000000 0.077317347729973659
3.250000000000000000 0.066445797300337575
3.500000000000000000 0.056427308587748998
3.750000000000000000 0.047206262644454398
4.000000000000000000 0.038730335242560636
4.250000000000000000 0.030950313116744881
4.500000000000000000 0.023819920032916261
4.750000000000000000 0.017295652173709861
5.000000000000000000 0.011336622357430538
5.250000000000000000 0.005904412631524745
5.500000000000000000 0.000962934804905312
5.750000000000000000 -0.003521701494450676
6.000000000000000000 -0.007581313629215667
6.250000000000000000 -0.011245764002368871
6.500000000000000000 -0.014543071700469415
6.750000000000000000 -0.017499518066203288
7.000000000000000000 -0.020139746518744655
7.250000000000000000 -0.022486856924209746
7.500000000000000000 -0.024562494803030899
7.750000000000000000 -0.026386935646401072
8.000000000000000000 -0.027979164599994392
8.250000000000000000 -0.029356951759925077
8.500000000000000000 -0.030536923313324527
8.750000000000000000 -0.031534628743968118
9.000000000000000000 -0.032364604312033328
9.250000000000000000 -0.033040433006292717
9.500000000000000000 -0.033574801156809497
9.750000000000000000 -0.033979551886482433
10.000000000000000000 -0.034265735570558842
10.250000000000000000 -0.034443657464468300
10.500000000000000000 -0.034522922652010971
10.750000000000000000 -0.034512478458033596
11.000000000000000000 -0.034420654462226502
11.250000000000000000 -0.034255200243556549
11.500000000000000000 -0.034023320978092020
11.750000000000000000 -0.033731711006561867
12.000000000000000000 -0.033386585481902695
12.250000000000000000 -0.032993710201270232
12.500000000000000000 -0.032558429721506903
12.750000000000000000 -0.032085693851855383
13.000000000000000000 -0.031580082612769629
13.250000000000000000 -0.031045829744990115
13.500000000000000000 -0.030486844848605806
13.750000000000000000 -0.029906734227607982
14.000000000000000000 -0.029308820511441333
14.250000000000000000 -0.028696161121263049
14.500000000000000000 -0.028071565645021508
14.750000000000000000 -0.027437612182052842
15.000000000000000000 -0.026796662714655951
15.250000000000000000 -0.026150877561036887
15.500000000000000000 -0.025502228961102200
15.750000000000000000 -0.024852513843820555
16.000000000000000000 -0.024203365822255265
16.250000000000000000 -0.023556266459888883
16.500000000000000000 -0.022912555849509453
16.750000000000000000 -0.022273442543698608
17.000000000000000000 -0.021640012873848664
17.250000000000000000 -0.021013239692633346
17.500000000000000000 -0.020393990572958997
17.750000000000000000 -0.019783035494624818
18.000000000000000000 -0.019181054048216954
18.250000000000000000 -0.018588642184146669
18.500000000000000000 -0.018006318533213998
18.750000000000000000 -0.017434530323629009
19.000000000000000000 -0.016873658918051336
19.250000000000000000 -0.016324024992908637
19.500000000000000000 -0.015785893381024190
19.750000000000000000 -0.015259477597418558
20.000000000000000000 -0.014744944067046633
20.250000000000000000 -0.014242416072187054
20.500000000000000000 -0.013751977436211952
20.750000000000000000 -0.013273675959528951
21.000000000000000000 -0.012807526622601630
21.250000000000000000 -0.012353514570115989
21.500000000000000000 -0.011911597889567400
21.750000000000000000 -0.011481710196791759
22.000000000000000000 -0.011063763040254453
22.250000000000000000 -0.010657648135239050
22.500000000000000000 -0.010263239438442219
22.750000000000000000 -0.009880395072880467
23.000000000000000000 -0.009508959112446098
23.250000000000000000 -0.009148763234912493
23.500000000000000000 -0.008799628251680935
23.750000000000000000 -0.008461365522080931
24.000000000000000000 -0.008133778259582282
24.250000000000000000 -0.007816662736848220
24.500000000000000000 -0.007509809396153650
24.750000000000000000 -0.007213003871309663
25.000000000000000000 -0.006926027926873753
end of method 2...
making graphs..
"""