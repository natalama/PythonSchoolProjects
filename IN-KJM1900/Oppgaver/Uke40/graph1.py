import matplotlib.pyplot as plt
import numpy as np


# skjønte ikke helt problemstillinga, for å være ærlig. Håper ikke det blir så feil. :)

def points_between_two_points(t, point_1, point_2):
    return (t*point_1) + ((1.0-t)*point_2)


get_variables = """
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

points_between_x = points_between_two_points(T_RANGE, x1, x2)
points_between_y = points_between_two_points(T_RANGE, y1, y2)


"""

T_RANGE = np.linspace(0, 1, 1000)  # T_RANGE will be between 0 and 1

x1 = 0.0
x2 = 0.0
y1 = 0.0
y2 = 0.0

fig, (axis1, axis2, axis3) = plt.subplots(nrows=1, ncols=3)

plt.title("Graphs")

print("Making horizontal line. y1 and y2 should be of same value")
exec(get_variables)
axis1.set_title("Horizontal line")
axis1.plot(points_between_x, points_between_y, marker='.')
print("----------------------------")
print("Making vertical line. x1 and x2 should be of same value")
exec(get_variables)
print("----------------------------")
print("Making a normal line. put any value you want")
axis2.set_title("Vertical line")
axis2.plot(points_between_x, points_between_y, marker='.')

exec(get_variables)
axis3.set_title("Normal line")
axis3.plot(points_between_x, points_between_y, marker='.')


figure = plt.gcf() # get current figure
figure.set_size_inches(8, 6)
plt.savefig("x_graph.png", dpi=100)
plt.show()

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke40> python .\graph1.py
Making horizontal line. y1 and y2 should be of same value
x1 = 1
y1 = 1
x2 = 6
y2 = 1
----------------------------
Making vertical line. x1 and x2 should be of same value
x1 = 1
y1 = 1
x2 = 1
y2 = 8
----------------------------
Making a normal line. put any value you want
x1 = 3
y1 = 4
x2 = 7
y2 = 8
"""
