##reads in a text file and outputs every second line. The program
##should take the filename from an argument on the command line.
##$ python second.py moby-dick.txt
##Title: Moby Dick; or The Whale
##CHAPTER 1
##Call me Ishmael. Some years ago--never mind how long
##particular to interest me on shore, I thought I would sail about a
# https://stackoverflow.com/a/33404310 reference
#@ Freha

import sys # import sys to get command line argument

arg1 = sys.argv[1] # assign the second argument from command line to arg1 variable

f =  open(arg1 ,"r") # open the file thats name was given as argument in read mode

fline = f.readline() # read the first line of the file

print(fline) # print the first line of the file because i want to print title

# start the counter 
count = 0 
#loop through lines of file 
for line in f:
   # increment count and see it is not divisible by 2 (to print every second line as second line index is 1)
    count += 1
    if count % 2 != 0:  #printing line 1,3,5... as in general we start counting by 1 but in python index satrt from zero so
        #second line index is 1
        # print the line
        print(line, end="\n")
   
f.close()
# close file    
    