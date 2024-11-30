# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{} is Even".format(num))  # {} is the replacment for the numbr 
else:
   print("{} is Odd".format(num))
