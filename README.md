# Problem Set

This repositery contains my solution to the problem set 2019 for the Module
Programming and Scripting at GMIT.@Freha

## What each File contains

1. **sumupto.py** contains my solution for  problem 1 in problem set.<br />
        <p>*It ask user to input any positive integer and outputs the sum of all numbers between one and that number. first in program it check the input to make sure number is positive (refernce:https://stackoverflow.com/a/23294659), if valid input it call the function sum and pass this input as an argument that fuction use while loop to calculate sum and return that sum value that  is printed* </p>
 ---       
2.  **begins-with-t.py** contains my solution for  problem 2 in problem set.<br />
        <p>*It displays whether or not today is a day that begins with the letter T. datetime module is imported The datetime module supplies classes for manipulating dates and times. method datetime.today().weekday() Return the day of the week as an integer, where Monday is 0 and Sunday is 6, of the current local datetime. that value was assigned to a variable and as only days 1 (Tuesday) and 3(Thursday) are the days started with T for if - else statement is used to print output* </p>
 ---      
3. **divisors.py** contains my solution for  problem 3 in problem set.<br />
        <p>*It prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12. In this programme first initialize a variable with value 1000 than use while loop to increment the value of i by 1 in each iteration and use if statement to check if number is divisible by 6 and not divisible by 12 use the % operator is used to get remainder if remainder is 0 its mean it is divisible otherwise not divisible print the number if both conditions met* </p>
---       
4. **collatz.py** contains my solution for  problem 4 in problem set.<br />
         <p>*It asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and,if it is even,divide it by two,but if it is odd, multiply it by three and add one. In this programme first ask user to input number use while loop and conditions to check if its valid input than print the input and use while loop  to iterate and do the calculation required in problem to check if the number is odd or even use remainder of divide by 2 as remainder will be 0 if number is even and here end=" " in print is used to print the output on same line* </p>
 ---       
5. **primes.py** contains my solution for  problem 5 in problem set.<br />
        <p>*It asks the user to input a positive integer and tells the user whether or not the number is a prime. prime number is a number that can be divided by itsel and 1 only. 0 and 1 are not prime. in this programme first input a number and check if it is positive number and than pass this number to function prime() that check the number and return the message if number is prime or not. in thatfunction if number is greater than 1 than try to divide it by numbers from 2 to num-1 if it is divisible on any than stop the loop and return the message not prime*</p>
---
6. **secondstring.py** contains my solution for  problem 6 in problem set.<br />
        <p>*It takes a user input string and outputs every second word. in this program split() method is used and list of words is assigned to words variable. The split() method splits a string into a list.You can specify the separator, default separator is any whitespace. len() method is used to get the length of list and as  index of list start from 0 so use  for loop to print 0,2,4,6... index elements of words list*</p>
 ---     
7. **squareroot.py** contains my solution for  problem 7 in problem set.<br />
        <p>*It takes a positive ﬂoating point number as input and outputs an approximation of its square root. In this programme first check for valid input and than math.sqrt(num) method is used to get square root to use this method first math module is imported and round function to round the result to 1 decimal place. The built-in Python function round() takes in two numbers, one to be rounded, and one that specifies the number of decimal places to include.*</p>
---        
8. **datetime.py** contains my solution for  problem 8 in problem set.<br />
        <p>*It outputs today’s dateand time in the format“Monday,January 10 2019 at 1:15pm”. To print the datetime in a specific format strftime() method is used. use the if -elif-else to manage the st,nd,rd and th in string*</p>
        
         The strftime(format) method is used , to create a string representing the time under the control of an explicit format string. 
          - %A Weekday as locale’s full name.
          - %B Month as locale’s full name
          - %d Day of the month as a zero-padded decimal number
          - %Y Year with century as a decimal number
          - %I Hour (12-hour clock) as a zero-padded decimal number.
          - %M Minutes as a zero-padded decimal number
          - %p Locale’s equivalent of either AM or PM.here 

        
 ---     
9. **second.py** contains my solution for  problem 9 in problem set.<br />
         <p>*It reads in a textﬁle and outputs every secondline. This program takes the ﬁlename from an argument on the command line. reference https://stackoverflow.com/a/33404310  import sys module to get command line argument *</p>
 ---      
10. **plot.py** contains my solution for  problem 10 in problem set.<br />
          <p>*It displays a plot of the functions x, x square and 2 raise to power x in the range [0,4]. use matplotlib to plot the graph. Import matplotlib.pyplot reference > https://matplotlib.org/tutorials/introductory/pyplot.html create a simple graph *</p>
          
           I also found a simple method using numphy i tried it and code is in plot2.py
                import numpy as np
                import matplotlib.pyplot as plt

                # evenly sampled x value 0 to 4 at intervals 1
                x = np.arange(0, 4, 1)

                # red dashes, blue squares and green triangles
                plt.plot(x, x, 'r--', x, x**2, 'bs', x, 2**x, 'g^')
                plt.show()
        
## Reference
1. https://matplotlib.org/tutorials/introductory/pyplot.html
2. https://matplotlib.org/gallery/pyplots/pyplot_three.html#sphx-glr-gallery-pyplots-pyplot-three-py