#outputs today’s date and time in the format ”Monday, January 
# 10th 2019 at 1:15pm”.$ python datetime.py
#Monday, January 10th 2019 at 1:15pm
import datetime

d = datetime.datetime.today()


time = d.strftime(" %A, %B %d %Y at %I:%M %p")

print(time)
