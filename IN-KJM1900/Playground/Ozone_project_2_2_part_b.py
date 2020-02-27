import numpy as np
import matplotlib.pyplot as plt

#DEFINE CONSTANTS
K1 = 3.0E-12
K2 = 1.2E-33
K3 = 5.5E-4
K4 = 6.9E-16
M = 9.0E17

# define initial values here
O_initial = 0
O_2_initial = 0.21*M # 0 0.21[M]
O_3_initial = 0


# RATE LAW
def der_O_1(O1, O2, O3):
    return (2*K1*O2) - (K2*O2*O1*M) + (K3*O3) - (K4*O1*O3)


def der_O_2(O1, O2, O3):
    return (-1*K1*O2) - (K2*O2*O1*M) + (K3*O3) + (2*K4*O1*O3)


def der_O_3(O1, O2, O3):
    return K2*O2*O1*M - K3*O3 - K4*O1*O3


start_t = 0
end_t = 1E8
interval_t = 1000

# backward equations
# f(x+dx) - f(x) - fder(x+dx)*dx = 0
# w = f(x+dx) y = fx
# W = O[d+dt], y = O
# F([O]t+dt) = [O]t+dt - [O]t - ((2k1[O2] − k2[O2][O][M] + k3[O3] − k4[O][O3])t+dt)*dt = 0
def backward_F_O(w, O1, O2, O3, interval):
    return O1 - der_O_1(O1, O2, O3) * interval - w


# F([O2]t+dt) = [O2]t+dt - [O2]t - ((−k1[O2] − k2[O2][O][M] + k3[O3] + 2k4[O][O3])t+dt)*dt = 0
def backward_F_O_2(w, O1, O2, O3,interval):
    return O2 - der_O_2(O1, O2, O3) * interval - w


# F([O3]t+dt) = [O3]t+dt - [O3]t - ((k2[O2][O][M] − k3[O3] − k4[O][O3])t+dt)*dt = 0
def backward_F_O_3(w, O1, O2, O3,interval):
    return O3 - der_O_3(O1, O2, O3) * interval - w


# derived backward equations!!!
#Fder([O]t+dt) = 1 - (-k2[O2][M] -k4[03])*dt
def derived_backward_F_O(O2, O3, interval):
    return 1 + interval * ((K2 * O2 * M) + (K4*O3))


#Fder([O2]t+dt) = 1 - (-k1 - k2[O][M])*dt
def derived_backward_F_O_2(O, interval):
    return 1 + (K1 + (K2*O*M))* interval


#Fder([O3]t+dt) = 1 - (k3 - k4[O])*dt
def derived_backward_F_O_3(O1, interval):
    return 1 + (K3 + (K4*O1)) * interval


def backward_euler(O_initial, O_2_initial, O_3_initial, interval, start, end, tol = 1E-6):
    iterations = int((end-start)/interval)+1
    O = np.zeros(iterations, dtype = 'float')
    O_2 = np.zeros(iterations, dtype = 'float')
    O_3 = np.zeros(iterations, dtype = 'float')
    t = np.zeros(iterations)
    t[0] = start
    #initial values
    O[0] = O_initial
    O_2[0] = O_2_initial
    O_3[0] = O_3_initial
    #backward algorithm
    np.seterr(all='raise')
    for i in range(iterations-1):
            O_prev = O[i]
            O_2_prev = O_2[i]
            O_3_prev = O_3[i]

            # Use forward euler to make a good "guess" for the next value
            O_est = O_prev + interval * der_O_1(O_prev, O_2_prev, O_3_prev)
            O_2_est = O_2_prev + interval * der_O_2(O_prev, O_2_prev, O_3_prev)
            O_3_est = O_3_prev + interval * der_O_3(O_prev, O_2_prev, O_3_prev)
            for j in range(50):
                backward_O_1 = backward_F_O(O_prev, O_est, O_2_est , O_3_est, interval)
                backward_O_2 = backward_F_O_2(O_2_prev, O_est, O_2_est, O_3_est, interval)
                backward_O_3 = backward_F_O_3(O_3_prev, O_est, O_2_est, O_3_est, interval)

                der_backward_O_1 = derived_backward_F_O(O_2_est, O_3_est, interval)
                der_backward_O_2 = derived_backward_F_O_2(O_est, interval)
                der_backward_O_3 = derived_backward_F_O_3(O_est, interval)

                O_1_next = O_est - backward_O_1/der_backward_O_1
                O_2_next = O_2_est - backward_O_2/der_backward_O_2
                O_3_next = O_3_est - backward_O_3/der_backward_O_3
                if(abs(O_est - O_1_next) <= tol):
                    O_est = O_1_next
                    O_2_est = O_2_next
                    O_3_est = O_3_next
                    break
                O_est = O_1_next
                O_2_est = O_2_next
                O_3_est = O_3_next
            O[i+1] = O_est
            O_2[i+1] = O_2_est
            O_3[i+1] = O_3_est
            t[i+1] = t[i] + interval
    return t, O,O_2, O_3


time, O, O2, O3 = backward_euler(O_initial, O_2_initial, O_3_initial, interval_t, start_t, end_t)

steady_state_o3 = np.sqrt((K1*K2)/(K3*K4))*O_2_initial*(M**0.5)
print(K3)
print(steady_state_o3)
print(K2*O_2_initial*M)
steady_state_o = (K3*steady_state_o3)/(K2*O_2_initial*M)
BE_O3_last_value = O3[-1]
BE_O_last_value = O[-1]

print("O_3 from BE: ", BE_O3_last_value)
print("O_3 from SS: ", steady_state_o3)
print("O from BE: ", BE_O_last_value)
print("O from SS: ", steady_state_o)
print(f"Relationship between Steady-state approximation and the values found with BE-algorithm: {steady_state_o3/BE_O3_last_value:.0f} , {steady_state_o/BE_O_last_value:.0f}")


plt.plot(time, O, label = "$[O]$")
plt.plot(time, O3, label = "$[O_3]$")
plt.xlabel("time")
plt.ylabel("ratelikning")
plt.yscale('log')
plt.legend()
plt.show()
