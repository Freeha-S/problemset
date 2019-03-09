#outputs whether or not today is a day
# that begins with the letter T. 
#Yes - today begins with a T.
#import datetime module
import datetime
# assign todays day to variable i it returns number value
i = datetime.datetime.today().weekday()
#print(i)
#print(datetime.datetime.today().weekday())
# 0=monday, 1=tuesday, 2=wednesday, 3 = thursday, 4=friday, 5=saturday,6= sunday
#so if i is in 1,3 its day with T i give range 1 to 4 with increment of 2
#its check if i 1 or 3 if true print start with T else not begin with T
if i in range(1,4,2):
    print("Yes - today begins with a T")
else:
    print("No -today not begins with T ")