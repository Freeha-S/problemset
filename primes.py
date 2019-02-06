#asks the user to input a positive integer and tells the user
#whether or not the number is a prime.
#$ python primes.py
#Please enter a positive integer: 19
#That is a prime.
i = int(input("Enter the Positive integer:"))
j= 2
message = "A Prime Number"
while j < i-1:
 if i % j == 0:
    message = "Not a Prime Number"
    j=i
 else:
    j = j + 1
print(message)