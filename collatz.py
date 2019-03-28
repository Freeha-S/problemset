# This Programme  input any positive integer  from use and outputs the
# successive values of the following calculation.
# At each step calculate the next value
# by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
# it by three and add one. Have the program end if the current value is one.
# Please enter a positive integer: 10
# 10 5 16 8 4 2 1
# @Freha

# Input a positive integer
# input a value from user and assign that value to variable i
while True: # loop for getting valid input
    try:
        i = int(input("Enter the Positive integer:"))
    except ValueError: # exception if not an integer input
        print(" Not a valid input ")
        continue
    if i < 0: # check if the input is less than 0
        print("Number must not be negative.")
        continue
    else:
        break  #if number is positive than exit the loop


print(i,end=" ")  #print the value of i end=" " to print the text on sameline and remove the newline insert at the end
#
# loop until  value of i is greater than 1
while i > 1:
    
    if i%2 == 0: # check if i is divisible by 2 means even
        
        i= i//2 #divide the i by 2 and assign value to i
        
        print(i,end=" ") #print value of i add end=" " to print the text on sameline and remove the newline insert at the end
    else:
       
        i=i*3+1  #if number is not divisible by 2 mean odd multiply by 3 and add 1 and assign result to i
        
        print(int(i),end=" ") # print i