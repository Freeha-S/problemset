#asks the user to input any positive integer 
# outputs the sum of all numbers between one and that number.
# reference to check input https://stackoverflow.com/a/23294659
#by Freha 
def sum(num):
    
   ans=0 # variable to store the answer
                # decrease the number in each iteration and add to ans variable that has initial value of 0 
   while num >0: # while loop to iterate from start value num to the 1 
      ans= ans+num  #add the number in ans
      num=num-1 # decrease the number by 1
   return ans  #return the sum of all number from the given number upto 1

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
       #if number is positive than exit the loop
        break

# call the sum function and print the return value with message
print("The sum of all numbers between one and ",i," is = ",sum(i))