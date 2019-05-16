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


# Python Exercises

Thanks to Jeffrey Hu for the resource:
https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt

__05-14-2019__

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
# !8 -> 40320

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


__05-15-2019__

# EX 3/100

```markdown
#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between #1 and n (both included). and then the program should print the dictionary.
#Suppose the following input is supplied to the program: 8       Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

#Defines int var and a dictionary to hold elements    
integer = 0
dict = {}

#User input for int var and converts to type(int)
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
#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:

t = []
l = ()
string = ""

string = input("Enter a list of number seperated by commas with no spaces \n")

l = string.split(',')
t = tuple(l)

print(t)
print(l)
```
