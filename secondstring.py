# takes a user input string and outputs every second word.
#$ python secondstring.py
#Please enter a sentence: The quick brown fox jumps over the lazy dog.
#The brown jumps the dog
message = input("Please enter a sentance:")

words = message.split()
length = len(message.split())

#print(length)
for x in range (0,length,2):
   
    print(words[x])
