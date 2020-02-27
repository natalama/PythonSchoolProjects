import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

#7   Troposfærisk ozon
#7.1 Lesing av måledata
n=242
rad_time=np.zeros(n)
rad=np.zeros(n)

infile=open("light.txt","r")
line=infile.readline()
for i in range(n):
    line=infile.readline()
    words=line.split()
    rad_time[i]=float(words[1])
    rad[i]=float(words[2])
infile.close()

rad_func= interpolate.interp1d(rad_time,rad)


#7.2
sigma_=1e11
k1a=1e-30
k1b=1
k2=1e10
k3=1e-11

k1=lambda t: k1a+k1b*rad_func(t)

t=5
n=1000
dt=t/n
N=20
time_array=np.linspace(0,t,n+1)

O_trop=np.zeros(n+1)
O3_trop=np.zeros(n+1); O3_trop[0]=8e11
NO_trop=np.zeros(n+1); NO_trop[0]=1.3e8
NO2_trop=np.zeros(n+1); NO2_trop[0]=5e11

dO=lambda O,O3,NO,NO2,t: k1(t)*NO2-k2*O
dO3=lambda O,O3,NO,NO2,t: k2*O-k3*NO*O3
dNO=lambda O,O3,NO,NO2,t: k1(t)*NO2-k3*NO*O3+sigma_
dNO2=lambda O,O3,NO,NO2,t: k3*NO*O3-k1(t)*NO2

#Funksjoner og deriverte til å sette inn i Backward Euler
fO=lambda Oprev,O,O3,NO,NO2,t: O-Oprev-dt*dO(O,O3,NO,NO2,t)
dfO=lambda O,O3,NO,NO2,t: 1+dt*k2

fO3=lambda O3prev,O,O3,NO,NO2,t: O3-O3prev-dt*dO3(O,O3,NO,NO2,t)
dfO3=lambda O,O3,NO,NO2,t: 1+dt*k3*NO

fNO=lambda NOprev,O,O3,NO,NO2,t: NO-NOprev-dt*dNO(O,O3,NO,NO2,t)
dfNO=lambda O,O3,NO,NO2,t: 1+dt*k3*O3

fNO2=lambda NO2prev,O,O3,NO,NO2,t: NO2-NO2prev-dt*dNO2(O,O3,NO,NO2,t)
dfNO2=lambda O,O3,NO,NO2,t: 1+dt*k1(t)

for i in range(n):
    O_prev=O_trop[i]
    O3_prev=O3_trop[i]
    NO_prev=NO_trop[i]
    NO2_prev=NO2_trop[i]
    t_prev=time_array[i]
    O_est=O_prev+dt*dO(O_prev,O3_prev,NO_prev,NO2_prev,t_prev)
    O3_est=O3_prev+dt*dO3(O_prev,O3_prev,NO_prev,NO2_prev,t_prev)
    NO_est=NO_prev+dt*dNO(O_prev,O3_prev,NO_prev,NO2_prev,t_prev)
    NO2_est=NO2_prev+dt*dNO2(O_prev,O3_prev,NO_prev,NO2_prev,t_prev)
    t_next=time_array[i+1]
    for j in range(N):
        O_newt=O_est-fO(O_prev,O_est,O3_est,NO_est,NO2_est,t_next)/dfO(O_est,O3_est,NO_est,NO2_est,t_next)
        O3_newt=O3_est-fO3(O3_prev,O_est,O3_est,NO_est,NO2_est,t_next)/dfO3(O_est,O3_est,NO_est,NO2_est,t_next)
        NO_newt=NO_est-fNO(NO_prev,O_est,O3_est,NO_est,NO2_est,t_next)/dfNO(O_est,O3_est,NO_est,NO2_est,t_next)
        NO2_newt=NO2_est-fNO2(NO2_prev,O_est,O3_est,NO_est,NO2_est,t_next)/dfNO2(O_est,O3_est,NO_est,NO2_est,t_next)
        O_est=O_newt
        O3_est=O3_newt
        NO_est=NO_newt
        NO2_est=NO2_newt
    O_trop[i+1]=O_est
    O3_trop[i+1]=O3_est
    NO_trop[i+1]=NO_est
    NO2_trop[i+1]=NO2_est

plt.title("Kinetisk simulering av troposfærisk O")
plt.xlabel("Tid [dager]")
plt.ylabel("Konsentrasjon [molekyler*cm**-3]")
plt.plot(time_array,O_trop)
plt.show()

plt.title("Kinetisk simulering av troposfærisk O3")
plt.xlabel("Tid [dager]")
plt.ylabel("Konsentrasjon [molekyler*cm**-3]")
plt.plot(time_array,O3_trop)
plt.show()

plt.title("Kinetisk simulering av troposfærisk NO")
plt.xlabel("Tid [dager]")
plt.ylabel("Konsentrasjon [molekyler*cm**-3]")
plt.plot(time_array,NO_trop)
plt.show()

plt.title("Kinetisk simulering av troposfærisk NO2")
plt.xlabel("Tid [dager]")
plt.ylabel("Konsentrasjon [molekyler*cm**-3]")
plt.plot(time_array,NO2_trop)
plt.show()
