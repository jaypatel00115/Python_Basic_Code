
# Simple while loop use in Python
# program to display numbers from 1 to 5

i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1

# Application of the while loop in Python
# program to calculate the sum of numbers until the user enters zero
total = 0

number = int(input('Enter a number: '))
# add numbers until number is zero
while number != 0:  #'!=' this sign represent the not equalt to...
    total += number    # total = total + number
    
    # take integer input again
    number = int(input('Enter a number: '))

print('total =', total)
