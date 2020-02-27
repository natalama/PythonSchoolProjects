import numpy as np


def get_Nth_term(n):
    return ((-1)**n)/(np.log(np.log(n)))

print("Start value of N:")
start_n = float(input())
print("End value of n")
end_n = float(input())

sum_nth_term = 0

while(start_n < end_n):
    nth_term = get_Nth_term(start_n)
    sum_nth_term += nth_term
    print(nth_term)
    start_n += 1
print(f"total sum: {sum_nth_term}", )
