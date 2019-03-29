#this programme outputs today’s date and time in the format 
# ”Monday, January  10th 2019 at 1:15pm”.
# @ Freha


import datetime # import datetime module
d = datetime.datetime.today() # get todays date in variable d
st=[1,21,31]
da= int(d.day) # as day is string in daytime object so need to cast it to integer to use in if
#strftime(format) method, to create a string representing the datetime under the control of an explicit format string.
#%A Weekday as locale’s full name.
#%B Month as locale’s full name
#%d Day of the month as a zero-padded decimal number
#%Y Year with century as a decimal number
#I Hour (12-hour clock) as a zero-padded decimal number.
#%M Minutes as a zero-padded decimal number
#%p Locale’s equivalent of either AM or PM.
if da in range(2,23,10):
    time = d.strftime(" %A, %B %dnd %Y at %I:%M%p") # use strftime function to format elements in d string 
elif da in range(3,34,20):
    time = d.strftime(" %A, %B %drd %Y at %I:%M%p") # use strftime to format elements in d string
elif da in st:
    time = d.strftime(" %A, %B %dst %Y at %I:%M%p") # use formate string to print elements in d string
else:
    time = d.strftime(" %A, %B %dth %Y at %I:%M%p") # use formate string to print elements in d string
print(time) # print the time string
