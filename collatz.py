#input any positive integer and outputs the
# successive values of the following calculation.
#  At each step calculate the next value
# by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
#it by three and add one. Have the program end if the current value is one.
#Please enter a positive integer: 10
#10 5 16 8 4 2 1

i= int(input("Enter the Positive integer:"))

while i > 1:
    if i%2 == 0:
        i= i//2
        print(i)
    else:
        i=i*3+1
        print(int(i))