#asks the user to input a positive integer and tells the user
#whether or not the number is a prime.
##Please enter a positive integer: 19
#That is a prime.


def prime(num):

   if num <= 1: #if number is 0 and 1 its not prime so return the messaage ont prime
      return "not a Prime Number"
   
   j= 2 # set a variable j value to 2
   message = "a Prime Number"  # message with default value a prime number
  
   while j < num-1:  #start a loop start from 2 until num-1
      if num % j == 0: # if number is devisible by the j
         message = "not a Prime Number"  #change the string value of message to not prime
         break # assign the num value to j to stop loop
      else:
         j = j + 1  #increase the value of j
   return message #return the message 

# input a value from user and assign that value to variable num
while True: # loop for getting valid input
    try:
        num = int(input("Enter the Positive integer:"))
    except ValueError: # exception if not an integer input
        print(" Not a valid input ")
        continue
    if num < 0: # check if the input is less than 0
        print("Number must not be negative.")
        continue
    else:
       break #if number is positive than exit the loop

print(num," is ",prime(num)) # print num and the call prime function and get message if prime or not