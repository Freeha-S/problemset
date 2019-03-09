#asks the user to input a positive integer and tells the user
#whether or not the number is a prime.
##Please enter a positive integer: 19
#That is a prime.


def prime(num):
   # set a variable j value to 2
   j= 2
   # message with default value a prime number
   message = "a Prime Number"
   #start a loop for divide by 2 until num-1
   while j < num-1:
      # if number is devisible by the j
      if num % j == 0:
         #change the value of message to not prime
         message = "not a Prime Number"
         # assign the num value to j to stop loop
         j=num
      else:
         #increase the value of j
         j = j + 1
   #return the message 
   return message

# input a number
num = int(input("Enter the Positive integer:"))
# print i and the call prime and get message if prime or not
print(num," is ",prime(num))