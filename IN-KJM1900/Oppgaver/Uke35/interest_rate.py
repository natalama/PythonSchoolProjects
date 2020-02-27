
# coding: utf-8

# In[2]:


"""adds the total interest to the initAmount after certain number of years
params: 
initAmount = Initial Amount
interest = Any number representing interest in percent
years = number of years
we prefer all units to be in float, but converted the interest and years in float
in an attempt to prevent human error 
 """
def addInterest(initAmount, interest, years):
    interestPercent = float(interest)/100.0
    totalAmount = initAmount*((1+interestPercent)**years)
    return totalAmount

initialAmount = 1000.
interest = 5.
years = 3
totalAmount = addInterest(initialAmount,interest,years);
#currencies usually have two decimal places.
print (f"Total Amount after {years} years: {totalAmount:5.2f}");

"""
PS C:\Users\Min PC\Downloads> python .\interest_rate.py
Total Amount after 3 years: 1157.63
"""