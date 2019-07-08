# Python Cookbook by Beazley / Jones
# Chapter 1 - Data Structures & Algorithms

# 1.1 Unpacking a Sequence into Seperate Variables
# If the quantity is mismatched a ValueError is thrown
print('*********')
p = (4, 5)
x, y = p # Unpacking tuple
print('x = ' + str(x),'\ny = ' + str(y)+ '\n')

print('\n*********')
data = ['ACME', 50, 91.10, (2012, 12, 21), 'junk']
name, shares, price, (year, month, day), _= data # Unpacking list w/ tuple
price = 91.10
print(f'Name: {name}\nShares: {shares}\nPrice: $%.2f\nDate: {month}/{day}/{year}\n' % price) 

# 1.2 Unpacking Elements from Iterables of Arbitrary Length
print('\n*********')
grades = sorted([70, 77, 88, 99, 100, 50])
low, *middle, high = grades
print(f'Low Score: {low}\nHigh Score: {high}')

print('\n*********')
line = 'user_name:*:-2:-1:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(f'User Name: {uname}\nHome: {homedir}\nsh: {sh}')

# 1.3 Keeping the Last N Item
# Uses the Generator deque -> One time use per call
# popleft() on a deque is O(1) VS lists insert/removing first entry is O(N)
print('\n*********')
from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(f'Queue: {q}')

# 1.4 Finding the Large or Smallest N Items
# priority queue algorithm
print('\n*********')
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print('Largest 3: ', heapq.nlargest(3, nums))
print('Smallest 3:', heapq.nsmallest(3, nums))

print('\n*********')
# import heapq

portfolio = [
  {'name': 'IBM', 'shares': 100, 'price': 91.1},
  {'name': 'AAPL', 'shares': 50, 'price': 543.22},
  {'name': 'FB', 'shares': 200, 'price': 21.09},
  {'name': 'HPQ', 'shares': 35, 'price': 31.75}]

cheap = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
print(f'Cheap Stock: {cheap}')
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['price'])
print(f'Expensive Stock: {expensive}')