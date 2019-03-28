# This programme prints all numbers between 1,000 and 10,000 
# that are divisible by 6 but not by 12.
# @ Freha


i=1000 # initialize a variable with value 1000

while i<10000: # use while loop 1o iterate until i < 10000
     # %  is used to get remainder if remainder is 0 its mean it is divisible otherwise not divisible
    if i % 6 == 0 and i % 12 != 0: #check if i is  divisible by 6 and if not divisible by 12
        print (i) #print value of i if both condition met
    i= i + 1  #increment value of i by 1