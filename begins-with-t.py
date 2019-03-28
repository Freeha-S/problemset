#Outputs whether or not today is a day
#that begins with the letter T. 
#output if today begin with T "Yes - today begins with a T".

import datetime  #import datetime module 
#The datetime module supplies classes for manipulating dates and times

#classmethod datetime.today() Return the current local datetime
# .weekday() Return the day of the week as an integer, where Monday is 0 and Sunday is 6. of today

i = datetime.datetime.today().weekday() # assign the day of the week integer value to variable i 

#print(datetime.datetime.today().weekday())
# 0=Monday, 1=Tuesday, 2=Wednesday, 3 = Thursday, 4=Friday, 5=Saturday, 6= Sunday

#so if i is  1 or 3 its day with T i give range 1 to 4 with increment of 2
#its check if i 1 or 3 if true print start with T else not begin with T
if i in range(1,4,2):
    print("Yes - Today begins with a T")
else:
    print("No - Today not begins with T ")