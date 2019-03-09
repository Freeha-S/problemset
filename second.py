##reads in a text file and outputs every second line. The program
##should take the filename from an argument on the command line.
##$ python second.py moby-dick.txt
##Title: Moby Dick; or The Whale
##CHAPTER 1
##Call me Ishmael. Some years ago--never mind how long
##particular to interest me on shore, I thought I would sail about a
# https://stackoverflow.com/a/33404310 reference
#@ Freha
import sys
# import sys to get command line argument
arg1 = sys.argv[1]
# assign the second argument from command line to arg1
# open the file in read mode
f =  open(arg1 ,"r") 
# read the first line of the file
line = f.readline()

# print the first line of the file
print(line)  
# start the counter 
count = 0 
#loop through lines of file 
for line in f:
   # increment count and see it is divisible by 2 (to print every second line)
    count += 1
    if count % 2 == 0:
        # print the line
        print(line, end="\n")

f.close()
# close file    
    