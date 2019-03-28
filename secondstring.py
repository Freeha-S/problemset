# This programme takes a user input string and outputs every second word.
#$ python secondstring.py
#Please enter a sentence: The quick brown fox jumps over the lazy dog.
#The brown jumps the dog
#@ Freha

message = input("Please enter a sentance:") # Input a string and assign it to message
words = message.split() #split the message into words get list of words
length = len(message.split()) # get the numbers of words
for x in range (0,length,2): #print the every second word start from 0 index to length increment by 2
     print(words[x], end=" ")
