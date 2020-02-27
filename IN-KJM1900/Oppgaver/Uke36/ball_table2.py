v0 = 18.5
g = 9.8
n = 10

a = 0        # nedre grense
b = 2*v0/g   # øvre grense
h = (b-a)/n  # lengde på hvert delintervall

# løs med for-løkke

y_values = []
t_values = []


print("Using for loop: ")
print("t       y(t)")  # overskrift
for i in range(n+1):
    t = a + (i*h)
    t_values.append(t)
    y = v0*t - 0.5*g*t**2
    y_values.append(y)

for index in range(0, len(t_values)):
    print(f"{t_values[index]:.2f}    {y_values[index]:.2f}")
print("------------------------------")
print("Using while loop: ")

# with while
print("t       y(t)")  # overskrift

y_values = []
t_values = []

epis = 1e-8  # toleranse
t = 0
while(t <= b):
    t_values.append(t)
    y = v0*t - 0.5*g*t**2
    y_values.append(y)
    t += h

index = 0
while index < len(t_values):
    print(f"{t_values[index]:.2f}    {y_values[index]:.2f}")
    index += 1

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke36> python .\ball_table2.py
Using for loop:
t       y(t)
0.00    0.00
0.38    6.29
0.76    11.18
1.13    14.67
1.51    16.76
1.89    17.46
2.27    16.76
2.64    14.67
3.02    11.18
3.40    6.29
3.78    0.00
------------------------------
Using while loop:
t       y(t)
0.00    0.00
0.38    6.29
0.76    11.18
1.13    14.67
1.51    16.76
1.89    17.46
2.27    16.76
2.64    14.67
3.02    11.18
3.40    6.29
3.78    0.00
"""
