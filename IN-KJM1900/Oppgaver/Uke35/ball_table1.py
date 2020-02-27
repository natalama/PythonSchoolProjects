v0 = 18.5
g = 9.8
n = 10

a = 0        # nedre grense
b = 2*v0/g   # øvre grense
h = (b-a)/n  # lengde på hvert delintervall

# løs med for-løkke

print("t       y(t)")  # overskrift
for i in range(n+1):
    t = a + (i*h)
    y = v0*t - 0.5*g*t**2
    print(f"{t:.2f}    {y:.2f}")

# with while
print("t       y(t)")  # overskrift


epis = 1e-8  # toleranse
t = 0
while(t <= b):
    y = v0*t - 0.5*g*t**2
    print(f"{t:.2f}    {y:.2f}")
    t += h
