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

# Python Exercise  / 100

```markdown

'''


Just found a really great resource for self-studying. Bunches of thanks to Jake VanderPlas for all the hard work compiling these resources.
https://jakevdp.github.io/PythonDataScienceHandbook/
