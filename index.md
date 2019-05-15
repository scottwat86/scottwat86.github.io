## Welcome to my GitHub Pages

Hello world! Lets learn some Python 3!


Thanks to Jeffrey Hu for the resource:

https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt

05-14-2019

# Python Exercise 1 / 100

```markdown
#Exercise 1/100
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
#EX 2/100
#Question:
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
'''

I chose to not use the factorial function and only briefly looked at the code when I found it. The tutorial I'm following must be using Python 2 as their solution code won't run on Jupitor and I gave up debugging. It returns the factorial but not a single line comma delimited sequence per the instructions.
