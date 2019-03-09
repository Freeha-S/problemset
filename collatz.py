#input any positive integer and outputs the
# successive values of the following calculation.
# At each step calculate the next value
# by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
#it by three and add one. Have the program end if the current value is one.
#Please enter a positive integer: 10
#10 5 16 8 4 2 1
#@Freha

# Input a positive integer
i= int(input("Enter the Positive integer:"))
#print value of i add end=" " to print the text on sameline and remove the newline insert at the end
print(i,end=" ")
# loop until 1
while i > 1:
    # check if i is divisible by 2 means even
    if i%2 == 0:
        #divide the i by 2 
        i= i//2
        # print result
        print(i,end=" ")
    else:
        #if number is not divisible by 2 mean odd multiply by 3 and add 1 and print result
        i=i*3+1
        print(int(i),end=" ")