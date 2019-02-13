# takes a positive floating point number as input and outputs
# an approximation of its square root.
#$ python squareroot.py
#Please enter a positive number: 14.5
#The square root of 14.5 is approx. 3.8.
import math

num = float(input("Enter the Positive number:"))

print(round(math.sqrt(num),2))