import csv
import os
import hashlib

def partone(input):
    for i in range(0, 100000000000):

        result = hashlib.md5((input + str(i)).encode()).hexdigest()
        if len(result) > 5 and result[0:5] == "00000":
            return i
        

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2015/day4")
with open("input.txt") as data:
    file_to_read = data.read()
print(file_to_read)
print(partone(file_to_read))