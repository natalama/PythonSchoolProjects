import numpy as np
import matplotlib.pyplot as plt

#konstants
g = 9.81 # gravitational constant - m/s^2
m = 30. # masse - kg
k = 0.01 # lufmotstandskoeffisient

#Tid
tid = 4. #sluttid i sekunder
N = 10000 #antall iterasjoner
dt = tid/N

#initial values
v0 = 0
s0 = 0

# arrays or lufmotstandskoeffisient
a = np.zeros(N)
v = np.zeros(N)
s = np.zeros(N)
t = np.zeros(N)

v[0] = v0
s[0] = s0

for i in range(N-1):
    a[i] = g-k*v[i]**2/m
    v[i+1] = v[i] + a[i]*dt
    s[i+1] = s[i] + v[i]*dt
    t[i+1] = t[i] + dt
a[-1] = g-k*v[-1]**2/m

tol = 1E-5
for j in range(len(s)):
    if s[j] > (15-tol) and s[j] < (15+tol):
        tid_pos = t[j]
        break

print(tid_pos)

plt.figure(figsize=(10,10))
plt.subplot(3,1,1)
plt.plot(t,a)
plt.subplot(3,1,2)
plt.plot(t,v)
plt.subplot(3,1,3)
plt.plot(t,s)
plt.tight_layout()
plt.show()
