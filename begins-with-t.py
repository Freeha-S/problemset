#outputs whether or not today is a day
# that begins with the letter T. 
#Yes - today begins with a T.
import datetime

i = datetime.datetime.today().weekday()
print(i)
if i in range(1,4,2):
    print("Yes - today begins with a T")
else:
    print("No -today not begins with T ")