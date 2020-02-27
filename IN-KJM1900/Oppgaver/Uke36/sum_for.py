"""
This is the original code:
<start of code>
s = 0
M = 3
for i in range(M):
    s += 1/2*k**2
print(s)
<end of code>

without running the code, I know that there are cerain errors:

1. k isn't defined
2. i isn't used (not really an error, but it's just strange)
3. there are missing parentheses. The correct formula should be s+= 1/((2*k)**2)
4. range(M) makes range from 0 to M-1. it should be range(1,M+1)

now, let's try to correct this by correcting the most obvious one: replace i with k
"""
print(f"""without running the code, I know that there are cerain errors:

1. k isn't defined
2. i isn't used (not really an error, but it's just strange)
3. there are missing parentheses. it says that the formula is 1/((2*k)**2)
4. range(M) makes range from 0 to M-1

now, let's try to correct this by correcting the most obvious one: replace i with k
""")

print("Trying to find the error using method 2...")
s = 0
M = 3

for k in range(M):
    s += 1/2*k**2
    print(f"immediate value of s: {s}")
print(f"Final value of S: {s}")

print("These are the results that I got by hand calculation: ")
s = 0
M = 3

print("1/(2**2) + 1/(4**2) + 1/(6**2) = 1/4+1/16+1/36 = 0.3402777777777778 ")
print("Getting the correct sum using for loop...")
for k in range(1, M+1):
    s += 1.0/((2*k)**2)
print(f"s = {s}")
print("------------------------------------")
print("Getting the same sum using while loop...")
s = 0
k = 1.
while k <= M:
    s += 1/((2*k)**2)
    k += 1
print(f"s = {s}")
print(f"s with two decimal places = {s:.2f}")

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke36> python .\sum_for.py
without running the code, I know that there are cerain errors:

1. k isn't defined
2. i isn't used (not really an error, but it's just strange)
3. there are missing parentheses. it says that the formula is 1/((2*k)**2)
4. range(M) makes range from 0 to M-1

now, let's try to correct this by correcting the most obvious one: replace i with k

Trying to find the error using method 2...
immediate value of s: 0.0
immediate value of s: 0.5
immediate value of s: 2.5
Final value of S: 2.5
These are the results that I got by hand calculation:
1/(2**2) + 1/(4**2) + 1/(6**2) = 1/4+1/16+1/36 = 0.3402777777777778
Getting the correct sum using for loop...
s = 0.3402777777777778
------------------------------------
Getting the same sum using while loop...
s = 0.3402777777777778
"""
