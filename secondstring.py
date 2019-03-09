# takes a user input string and outputs every second word.
#$ python secondstring.py
#Please enter a sentence: The quick brown fox jumps over the lazy dog.
#The brown jumps the dog
#@ Freha

# Input a message
message = input("Please enter a sentance:")
#split the message into words get list of words
words = message.split()

# get the numbers of words
length = len(message.split())

#print the every second word start from 0 to length increment by 2
for x in range (0,length,2):
   
    print(words[x], end=" ")
