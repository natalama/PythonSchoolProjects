import numpy as np


# gets the temperatures based on the dat file
# parameter: filename - must include file extension
# return: a list of names
def extract_data(filename):
    temperatures = []
    with open(filename, "r") as file:
        header = file.readline()
        lines = file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                temperatures.append(float(word))
    return temperatures


def print_stats(title, data):
    print(title)
    print(f"max temperature: {np.max(data)}")
    print(f"min temperature: {np.min(data)}")
    print(f"mean temperature: {np.mean(data)}")


def write_formatting(filename, list_1, list_2):
    newfile = open(filename, "w+")
    print(f"writing data to {filename} ...")
    for temp_oct_1945, temp_oct_2014 in zip(list_1, list_2):
        newfile.writelines(f"{temp_oct_1945:5.2f}    {temp_oct_2014:5.2f}\n")
    print(f"data written to {new_filename} successfully!")


oct_1945 = extract_data("temp_oct_1945.dat")
oct_2014 = extract_data("temp_oct_2014.dat")

print_stats("October 1945", oct_1945)
print("--------------------")
print_stats("October 2014", oct_2014)
print("--------------------")
new_filename = "temp_formatted.txt"
write_formatting(new_filename, oct_1945, oct_2014)

r"""
Terminal> python .\temp_read_write.py
October 1945
max temperature: 11.6
min temperature: 2.1
mean temperature: 6.506451612903225
--------------------
October 2014
max temperature: 13.6
min temperature: 2.3
mean temperature: 8.85483870967742
--------------------
writing data to temp_formatted.txt ...
data written to temp_formatted.txt successfully!
"""
