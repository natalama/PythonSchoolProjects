print("Problem 2.6. Table showing population growth")

g = 9.81
v0= 5

n=12
a = (48)/n


B = 50000
k = 0.2
t_=0

from math import exp

t = []
N = []

for b in range(0,n+1,1):
    N_= B/(1+9*exp((-k)*t_))
    t.append(t_)
    N.append(N_)
    t_ = t_ + a
    print("%4.0f %4.0f"%(t[b], N[b]))
