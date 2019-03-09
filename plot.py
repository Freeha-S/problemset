# displays a plot of the functions x, x2 and 2x in the range [0, 4].
#import matplotlib
import matplotlib.pyplot as plt
# values of x from 0 to 4
x=[0,1,2,3,4]
# get the value for square of x
xsquares = []
for num in range(5):
    xsquares.append(num**2)
#print(xsquares)
# get the value of 2x
twox = []
for num in range(5):
    twox.append(2**num)
#print(twox)
#twox = [1,2,4,8,16]
#xsquares = [0,1,4,9,16]
# plotting first line
plt.plot(x,twox,label="2 raise to x")
#plotting second line
plt.plot(x, xsquares, label= 'x square')
#values of axis
plt.axis([0, 5, 0, 18])
#naming the x axis
plt.xlabel('x - axis') 
#naming the y axis
plt.ylabel('y - axis') 

# giving a title to my graph 
plt.title('Graph!') 
  
# show a legend on the plot 
plt.legend() 
#function to show the plot
plt.show()