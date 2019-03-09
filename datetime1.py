#outputs today’s date and time in the format ”Monday, January 
# 10th 2019 at 1:15pm”.$ python datetime.py
#Monday, January 10th 2019 at 1:15pm
# @ Freha
# import datetime module
import datetime
# get todays date in variable d
d = datetime.datetime.today()

# use formate string to print elements in d string 
time = d.strftime(" %A, %B %d %Y at %I:%M %p")
print(time)
