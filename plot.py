# displays a plot of the functions x, x2 and 2x in the range [0, 4].
# @ Freha

#import matplotlib
import matplotlib.pyplot as plt

x=[0,1,2,3,4] # values of x from 0 to 4 0 and 4 inclusive

y=x #as first function f(y) = x

# get the value for square of x
xsquares =  []
for num in range(5):
    xsquares.append(num**2) # f(y) =xsquare
#xsquares = [0,1,4,9,16]   
#print(xsquares)

# get the value of 2 raise to powerx
twox = []
for num in range(5):
    twox.append(2**num) # f(y) =2 raise to power x 
#twox = [1,2,4,8,16]
#print(twox)

#fig = plt.figure()# thjis is also the part to print datapoints https://stackoverflow.com/a/22272358
#ax = fig.add_subplot(111)
#plt.plot(x,y,linewidth=2, label="f(y)=x") # plot first line 

#for xy in zip(x,y):                      # i tried the code to print data points still working on it                 
  #  ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # https://stackoverflow.com/a/22272358
  
plt.plot(x,y,linewidth=2, label="f(y)=x") # plot first line 
plt.plot(x, xsquares,linewidth=2, label= 'f(y)=x square') #plotting second line
plt.plot(x,twox,linewidth=2,label="f(y)=2 raise to x") # plotting third function line

plt.axis([0, 5, 0, 18]) # set values of axis x axis 0 -5 and y axis 0-18

plt.xlabel('x - axis') #naming the x axis
plt.ylabel('y - axis') #naming the y axis

plt.title('Graph!') # giving a title to my graph 
plt.legend() # show a legend on the plot 

plt.show() #function to show the plot