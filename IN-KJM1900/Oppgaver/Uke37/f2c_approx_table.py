def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32.0)/1.8


def fahrenheit_to_approx_celsius(fahrenheit):
    return (fahrenheit - 30)/2


# end of range is set to 101 so that 100 can be included
# The range is 0, 10, 20... 100, so we need to set 10 as the last argument
# (interval)
fahrenheit_range = range(0, 101, 10)

# Headers
print("Fahrenheit | Celsius | Approx. Celsius")

# it wasn't specified that making list was required, so I didn't make it
for fahrenheit in fahrenheit_range:
    # not the best programming practice, but  I didn't bother bother storing celsius and approximate celsius in variables
    print(f"{fahrenheit:10.2f} | {fahrenheit_to_celsius(fahrenheit):7.2f} | \
    {fahrenheit_to_approx_celsius(fahrenheit):11.2f} ")

r"""
Terminal> python .\f2c_approx_table.py
Fahrenheit | Celsius | Approx. Celsius
      0.00 |  -17.78 |          -15.00
     10.00 |  -12.22 |          -10.00
     20.00 |   -6.67 |           -5.00
     30.00 |   -1.11 |            0.00
     40.00 |    4.44 |            5.00
     50.00 |   10.00 |           10.00
     60.00 |   15.56 |           15.00
     70.00 |   21.11 |           20.00
     80.00 |   26.67 |           25.00
     90.00 |   32.22 |           30.00
    100.00 |   37.78 |           35.00
"""
