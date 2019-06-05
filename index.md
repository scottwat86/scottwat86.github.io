## Welcome to my GitHub Pages

# BIO
Hello world! My name is Scott and I grew up in California and Washington. I graduated in 2010 from University of Washington with a BS in Engineering. Although I had several experiences with technology in my youth, from building my first computer at age 10, to experimenting with Red Hat Linux command line, I never went pro. In my mid-career as a project manager I've decided to make the leap move into technology. This site is dedicated to my data science and programming journey. Lets learn some Python 3!

# Background
Red Hat Linux - 1 year (self taught)  
Unix/Linux System Admin - 3 month (CEU @ UW)  
Javascript - 3 month (self taught)  
Java - 3 month (TCC college course)  
MATLAB - 6 months (college course in FEM modeling of structual elements)  


"A journey of a thousand miles begins with a single step."  -Laozi


# EU  Python Tutorial:  
https://www.python-course.eu/python3_history_and_philosophy.php

05-30-2019
* For Loops


05-22-2019
* input via the keyboard
* Conditional Statements
* Loops, while Loop
* For Loops

05-21-2019  
* Sets and Frozen Sets
* An Extensive Example for Sets

05-20-2019  
* List Manipulations
* Shallow and Deep Copy
* Dictionaries

05-19-2019  
* Sequential Data Types: Lists and Strings

05-17-2019  
* The Origins of Python
* Starting with Python: The Interactive Shell
* Executing a Script
* Indentation
* Data Types and Variables
* Operators


# Python Exercises  
Thanks to Jeffrey Hu for the resource:  
https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt  



## 06-04-2019
Worked through Sections 1.1 through 1.3 of Python Cookbook review what I read. This time I'm typing up, commenting and modifying the examples to better retain and remember. Also worked on Finxter for ~0.5hr.

## 06-02-2019
Setup repository for LPTHW exercises documented below. Learned to push them to Github using the git command. Worked on ~ 1hr of Finxter problems including researching and typing out the portions I didn't not understand.

## 06-01-2019
Finxter execersizes for ~ 1hr. 
Exercises 23		-	Learning Python 3 the Hardway

## 05-31-2019   
About half way done with EX 22 which is a review of all the previous content. I'm making a pretty extensive review sheet with some other code tricks I've picked up elsewhere. Will be looking into start a project soon as I've almost got the basics down. 
Exercises 16-22		-	Learning Python 3 the Hardway


## 05-30-2019  
Quite frankly struggling keeping up on the 3HR/day ... 20HR/Week study regiment. First two weeks went smoothly so I guess I should've expected a bump in the road sooner or later. Hopefully life settles down between car trouble and work deadlines so that I can really focus.

Exercises 17-18		-	Learning Python 3 the Hardway   
EU Python Tutorial 	-	For Loops

## 05-29-2019  
Worked on refining my Atom enviroment and and ~2.5hr of Fixnter training.  
Fixnter Rank: Experienced Intermediate  
Exercises 16		-	Learning Python 3 the Hardway   


## 05-28-2019
Short night tonight. Need to catch of from the slacking weekend but have a day job deadline to finish.  
Exercises 12 - 15		-	Learning Python 3 the Hardway   


## 05-27-2019
Completed roughly __1hr of puzzles on__. Interesting puzzles that center around interpreting code rather than writing. Again great as a tool in the toolbox but probably not practical as a stand alone. The difference between writing and reading.
https://app.finxter.com/learn/computer/science/ 

Chapters  1 - 4			-	Learning MORE Python 3 the Hardway  
Exercises 9 - 11		-	Learning Python 3 the Hardway  
 

## 05-26-2019
Completed EX1 - EX8 on Learning Python3 the hard way and then hit the paywall. Found a copy of the book for free but it doesn't seem to follow the same foremat as the website EX. The book is mainly text where the site is examples to transcribe. Not exactly the most problem solving focused methodology but I can see how process and good habits matter and practice makes perfect!
https://learnpythonthehardway.org/python3/preface.html  

Exercises 1-8		-	Learning Python 3 the Hardway 

## SKIPPED 05-24-2019  ROAD TRIP

## 05-23-2019
Joined Triage though it may take a while to find a pull request that I can troubleshoot confidently. At the minimum this site will get me exposed to real world programming issues. Its how I found Namba and optimization problems for SciPy.

# performance testing code  -> didn't realize that Python was so inefficient compared to C++
```markdown
from datetime import datetime
startTime = datetime.now()

#do something 

#Python 3: 
print(datetime.now() - startTime)
```

Down the rabbit hole ... background research on the packages to learn down the line:

__Arrays & Engineering Computation__
* NumPy 		-Arrays and linear algebra
* SciPy			-Various functions to operate on numpy arrays & scientific and engineering applications.

__Optimization__
* Namba			-Creates Just-in-time(JIT) machine code to speed up array/numerical calculatons similar to C/C++/FORTRAN

__Visualizations__
* Matplotlib		-general purpose & 
* pandas		-quick plots
* seaborn		-statistical plots
* bokeh			-interactive plots & web browsers for presentation

https://python-graph-gallery.com/  
https://realpython.com/python-matplotlib-guide/  


__Machine Learning__
* scikit-learn		-classification, regression, clustering algorithms incl. support vector machines, random forests, 
			 gradient boosting, k-means and DBSCAN

Brought me back to my MATLAB days. Their are some great resources out there. 

Data Camp Quick Ref -> Strongly considering picking up a subscription
https://www.datacamp.com/community/data-science-cheatsheets


## 05-22-2019

__Guessing Game While Loop__
```markdown

# Simple guessing game

import random  

number = random.randint(1,101)
i=0
guess = int(input("You have 4 tries. \nEnter a number between 0-100: "))
while guess != number :
    if guess < 0 or guess > 100:
        guess = int(input("Number is outside of range. \nTry again: "))
    i += 1
    guess = int(input("That is not it. \nTry again: "))
    if 3 == i:
        print("Fail! \nYou guessed too many times!")
        break
else:
    print('You got it. Congrats!')  # Doesn not execut if  break occurs
    

# Simple for loop with food on the brain

ingredients = ['ham', 'cheese', 'bacon', 'hamburger', 'mayo'] 
yuck=0 

for food in ingredients: #simple for loop with food on the brain
    if food == 'mayo':
        print(food + ". Yuck!")
        yuck += 1
        continue
    elif yuck >3:
        break
        
    print("Yum! " + food + ".")
else:
    print('Mayo is gross!')
print("I'm full!")   
```


## 05-20-2019

10 Python tips and tricks:  
https://www.youtube.com/watch?v=C-gEQdGVXbk&t=814s

# RW

__(1) Assigning value with ternary conditional__
``` markdown
condition = True

x = 1 if condition else 0
```


__(2) readability of large numbers__
```markdown
x = 100_000_000  #instead of x = 100000000
print(f'{total:,}')   # Formats input with ','
```


__(3) Context Manager (eg openning/closing files/databases -> managing resources)__
```markdown

#import os
#os.getcwd() #shows the working dir for opening the file

with open('test.txt', 'r') as f:
	file_contents = f.read()    #automatically closes file once completed the read

print(file_contents)
```


__(4) Enumerate() -> adds a counting var to iterable__
```markdown
names = ['Corey', 'Scott', 'Brian']

for index, name in enumerate(names, start=1):  # starts at index=1
	print(index, name) #returns index and value
```


__(5) Accesing index and value in two lists__
``` markdown
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

for index, name in enumerate(names):
	hero = heroes[index]
	print(f'{name} is actually {hero}')   #pulls corresponding values with index from each list
```


__(6) Interrelated list unpacking ->  Zip()__
``` markdown
names = ['Peter Parker']   #stops on the shortest list
heroes = ['Spiderman']   
universes = ['Marvel']  

#zip creates a single tuple of 3 strings
for name, hero, universe in zip(names, heroes, universes):  
	print(f'{name} is actually {hero} from {universe}')
```
Output: "Peter Parker is actually Spiderman from Marvel"


__(7) Unpacking variable length and throw away data list/tuples__
```markdown
a, _, *c, d = [1,2,3,4,5,]

#'_' throws away 2

print(c) # c = 3,4 
```

__(8) Adding/retrieving attributes dynamically (value is variable)__
```markdown
class Person():
	# name = 'Jack'
	pass 	# As long as no arg in class use 'pass'

person = Person()
first_key = 'name'   # attribute name
first_val = 'Corey'  # attribute 

setattr(person, first_key, first_val) 
first = getattr(person, first_key, first_val)

print(first) 

#              key       value
person_info = {'height': 70,   'weight': 175}
for key, value in person_info.items():   #items() returns index, value of dict
	setattr(person,key,value)

print(person.height)  #returns height value in inch
print(person.weight)

delattr(person,'height') #deletes attr 'height'

dir(person) # to list the methods and attributes on a class
```


__(9) Sensitive info -> enter your password__
```markdown
from getpass import getpass

usr = input('Username:')
pw = getpass('Password:')  # password doesn't show up in terminal


__Module Docs__
help() # returns details about module / documentation

```


## 05-19-2019
# EX 6/100
``` markdown

'''
Question: Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 * C * D)/H] 

Following are the fixed values of C and H:
C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence.
EX 100,150,180  -> Output:   18,22,24'''

import math

C = 50 
H = 30
result = []

# Gets a series of numbers from user
print("\n---------------------------\n" +  "Q = SQRT[(2 * C * D)/H]\n" + "C =" + str(C) + "\n" + "H =" + str(H) + "\n---------------------------\n")

# 1sr reads string input
# 2nd splits the string input by ","  
# 3rd maps string to int, saves to list 
values = map(int, input("Enter numbers seperated by commas:\nD = ").split(","))

# different way to map NOT USED
# values =[x for x in input("Enter a Value").split(',')]

# Calculations
for D in values:
    result.append(math.sqrt(2*C*D/H))    
    
#prints answer after converting to str
print('Q = ' + str(result) + "\n\n The End\n")
```


# EX 7 /100

``` markdown
'''
'''
Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1.

EX:  Inputs: 3,5 -> Output: [0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''

# User input for row and columns of array
row_N, col_N = map(int, input("Enter number of rows and columns seperated by comma: ").split(','))

#Produces empty array rows=x col=y
array = [[0 for col in range(col_N)]for row in range(row_N)]

for row in range(row_N):
  for col in range(col_N): 
    array[row][col] = row*col 

print(array) 
```


## 05-17-2019
Found a new python 3 course that is pretty thorough and well written. It also has great tips for existing programmers making the transition to python.

https://www.python-course.eu/python3_history_and_philosophy.php

I'll be reading more along with the more advanced Python Cookbook. Complete:


## 05-16-2019
# Python Cookbook 1.3

``` markdown
'''
Problem: You want to keep a limited history of the last few items seen during iteration or during some other kind of processing.
'''
import random

n = input("Enter the number of iterations: \n")
n = int(n)

running_list = []

for i in range(n):
    running_list.append(random.randint(0,1000))

*_, t1, t2, t3 = running_list

list_3 = [t1,t2,t3]
print(running_list)
print(list_3)
```


## 05-15-2019

# EX 3/100

```markdown
''' With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between #1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program:      8       Then, the output should be:       {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}  """"

#Defines a dictionary to hold elements    
dict = {}

#User input saved to integer and then converted from string to type(int)
integer = input("Enter a integer: \n")
integer = int(integer)

#Populates dictionary with i and i^2
for i in range(integer):
    dict[(i+1)] = (1+i)*(i+1)

#prints    
print(dict)
```


# EX 4/100

``` markdown
""" Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. #Suppose the following input is supplied to the program:    34,67,55,33,12,98     Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""


#Creates string variable and saves input
string = input("Enter a list of number seperated by commas with no spaces \n")

#Splits string by comma delimination into list and then creates a tuple
l = string.split(',')
t = tuple(l)

print(t)
print(l)
```

# EX 5/100

``` markdown
""" Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods. """

#defines the class 
class string_output :
    
#defines the methods

    def getString(self):
        input_string = input("Enter a string: \n")
        return input_string

    def printString(self, s):
        print(s.upper())
    
#Creates object input_string of class string_output
string = string_output()

text = string.getString()
input_string.printString(text)
```

## 05-14-2019

# Python Exercise 1 / 100

```markdown
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

s = []

for i in range(2000, 3201):
    if i%7 == 0 and i%5 != 0:
        s.append(i)
    
print(s)
    
```

# Python Exercise 2 / 100

```markdown

#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#!8 -> 40320

n = 0
factorial = 1
f = []

n = input("Enter a number to apply the factorial \n")
n = int(n)

if n == 0:
    f = ['1']
else:    
    for i in range(1,n+1):
        factorial = factorial*i
        f.append(str(factorial))
    
    
print(",".join(f)) 
```

I chose to not use the factorial function and only briefly looked at the code when I found it. The tutorial I'm following must be using Python 2 as their solution code won't run on Jupitor and I gave up debugging. It returns the factorial but not a single line comma delimited sequence per the instructions.













