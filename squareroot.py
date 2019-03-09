# takes a positive floating point number as input and outputs
# an approximation of its square root.
#$ python squareroot.py
#Please enter a positive number: 14.5
#The square root of 14.5 is approx. 3.8.

#import math module
import math
# add a positive number
num = float(input("Enter the Positive number:"))
# print result of num  get squareroot by math.sqrt() and round to 2 decimal places 
print("The square root of",num , " is approx ",round(math.sqrt(num),1))