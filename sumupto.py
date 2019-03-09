#asks the user to input any positive integer 
# outputs the sum of all numbers between one and that number.
#by Freha
def sum(num):
    # variable to store the answer
    ans=0
    # while loop to iterate from start value to the 1 
    # decrease the number in each iteration and add to ans variable that has initial value of 0 
    while num >0:
    #add the number in ans
       ans= ans+num
    #decrease the number by 1
       num=num-1
    #return the sum of all number from the given number upto 1
    return ans
# input a value from user and assign that value to variable i
i = int(input("Enter the Positive integer:"))
# call the sum function and print the return value
print("The sum of all numbers between one and ",i," is = ",sum(i))