#prints all numbers between 1,000 and 10,000 
# that are divisible by 6 but not 12.
# @Freha
# start variable with value 1000
i=1000
# while loop iterate until 10000
while i<10000:
    #check if divisible by 6
    if i % 6 == 0:
        #check if not divisible by 12
        if i % 12 !=0:
            #print value of i
            print (i)
    #increment value of i by 1
    i= i + 1