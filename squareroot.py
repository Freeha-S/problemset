# takes a positive floating point number as input and outputs
# an approximation of its square root.
#$ python squareroot.py
#Please enter a positive number: 14.5
#The square root of 14.5 is approx. 3.8.


import math #import math module

# input a value from user and assign that value to variable num
while True: # loop for getting valid input
    try:
        num = float(input("Enter the Positive float number:"))
    except ValueError: # exception if not a float input
        print(" Not a valid input ")
        continue
    if num < 0: # check if the input is less than 0
        print("Number must not be negative.")
        continue
    else:
        break #if number is positive float than exit the loop

# print result of num  get squareroot by math.sqrt() and round to 1 decimal places 
print("The square root of",num ,"is approx",round(math.sqrt(num),1))