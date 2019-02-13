# displays a plot of the functions x, x2 and 2x in the range [0, 4].
import matplotlib.pyplot as plt

x=[0,1,2,3,4]
twox = [0,2,4,6,8]
squaretox = [0,2,4,8,16]
# plotting first line
plt.plot(x,twox,label="2x")
#plotting second line
plt.plot(x, squaretox, label= '2 raise to x')
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