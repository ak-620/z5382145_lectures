lst1 = ['a']
print(f'This is lst1: {lst1}')

lst2 = ['b', lst1]
print(f'This is lst 2: {lst2}')

lst2[1].append('c')
print(f"This is lst2 after modifying it: {lst2}")

print(f"This is lst2 after modifying it: {lst1}")

#Another example

lst1 = ['a']
print(f'This is lst1: {lst1}')

lst3 = ['b', ['a']]
print(f'This is lst3: {lst3}')

lst3[1].append('c')
print(f"This is lst3 after appending 'c': {lst3}")

print(f"This is lst1 after modifying lst3: {lst1}")


happy = 5
if happy:
    print("I am happy")

import pandas as pd

#Part(a)
series_abc = {'a': 1, 'b':2, 'c':3}

hours = input('Enter number of hours you worked this week: ')
#Python 3 output numeric value as a string in input () function
hours = int(hours)
normal_rate = 51.45
overload_rate = 88.9

if hours > 35 :
    pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
else :
    pay = hours * normal_rate

print(f'This weekly payment is {pay}')

letters_lst = {"a", "b", "c", "d"}

for letters in letters_lst:
    print (letters)

# omitting the 'step' parameter
for i in range(0, 5):
    print(f"i is now {i}")

### Sample Solution
numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]

temp_largest = numbers[0]
for number in numbers:
    if number > temp_largest:
        temp_largest = number
    print (number,temp_largest)

print(f'The largest value is {temp_largest}')

# while loop
the_sum = 0
i = 1
while i <= 100:
    the_sum = the_sum + i
    i = i + 1
print (the_sum)

for even in range (0,10,2):
    print(even)
    if even > 2:
        break

for odd in range(1, 10, 2):
    for even in range(0, 10,2):
        if even > 2:
            break
    print(even, odd)