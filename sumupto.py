#asks the user to input any positive integer 
# outputs the sum of all numbers between one and that number.

ans=0

i = int(input("Enter the Positive integer:"))

while i>0:
    ans= ans+i
    i=i-1
print(ans)