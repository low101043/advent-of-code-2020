import csv
import os

print(os.getcwd())
with open("2020/day9/day9Input1.txt") as data:
    file_to_read = data.read()

number_to_add = ""
numbers = []

for letter in file_to_read:
    if (letter == "\n" and number_to_add != ""):
        number_as_int = int(number_to_add)
        numbers.append(number_as_int)
        number_to_add = ""
    else:
        number_to_add += letter

print(numbers)
print(len(numbers))

#Use list to store previous values.  Use set to store all upcoming values.  Not efficient but it'll work!

previous_values = numbers[:25]
print(previous_values)

index = 25
final_answer = -100
finished = False
while index < len(numbers) and not finished:
    next_value = numbers[index]
    list_of_all = []
    for i, number in enumerate(previous_values):
        for j, number2 in enumerate(previous_values):
            if (i == j):
                pass
            elif (number == number2):
                pass
            else:
                list_of_all.append(number2 + number)
    
    set_of_all = set(list_of_all)
    #print(set_of_all)

    found = False
    for value in list(set_of_all):
        #print(value)
        #print(next_value)
        if (value == next_value and not found):
            found = True
            #print(previous_values)
            old_values = previous_values[1:]
            #print(old_values)
            old_values.append(value)
            previous_values = old_values
            #print(previous_values)
            
    print(previous_values)
    if (not found):
        #print("Here")
        finished = True
        final_answer = next_value
    else:
        index += 1

print(final_answer)

finished_again = False
i = 0
range_of_numbers = []
while i < len(numbers) and not finished_again:
    j = i +1
    got_some = False
    added = numbers[i]
    print(added)
    while (j < len(numbers) and not got_some):
        added += numbers[j]
        if (added == final_answer):
            print(added)
            print(numbers[i])
            print(numbers[j])
            range_of_numbers = numbers[i:j+1]
            
            got_some = True
            finished_again = True
        else:
            j +=1
    if (not finished_again):
        i += 1
    
small = min(range_of_numbers)
large = max(range_of_numbers)
print(small+large)
