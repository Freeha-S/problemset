#prints all numbers between 1,000 and 10,000 
# that are divisible by 6 but not 12.

i=1000

while i<10000:
    if i % 6 == 0:
        if i % 12 !=0:
            print (i)
    i= i + 1