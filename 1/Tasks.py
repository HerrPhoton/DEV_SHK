import random
import sys
import math
import os

def sumOfNums(num):

    print('Number:', num)

    sum = 0
    num = abs(num)

    while num != 0:
        sum += num % 10
        num //= 10

    print('Sum of number:', sum, '\n')

print('Task 1:')
sumOfNums(random.randint(100, 999))

print('Task 2:')
sumOfNums(random.randint(-sys.maxsize, sys.maxsize))

print('Task 3:')
radius = int(input('Enter the radius of the sphere: '))

S = 4 * math.pi * radius ** 2
V = 4/3 * math.pi * radius ** 3

print('S =', S)
print('V =', V, '\n')

print('Task 4:')
year = int(input('Enter year: '))

if year % 4 == 0:
    print('This year is a leap year', '\n')
else:
    print('This year is not a leap year', '\n')

print('Task 5:')
n = int(input('Enter N: '))

sieve = [False for i in range(0,n)]
sieve[0] = True
sieve[1] = True

primes = [0 for i in range(0,n)]
cnt = 0

for i in range(2,n):
    if sieve[i] == 0:

        primes[cnt] = i
        cnt += 1

        sqr = i * i 

        if sqr <= n:
            for j in range(sqr, n, i):
                sieve[j] = 1

primes = set(primes)
primes.remove(0)

print(primes, '\n')

print('Task 6:')
x = int(input('Enter the deposit amount: '))
y = int(input('Enter the number of years: '))

print(x * 1.1 ** y, '\n')

def printFiles(path):

    files = os.listdir(path)

    for i in range(0, len(files)):

        file = path + '\\' + files[i]

        if os.path.isfile(file):
            print(file)
        else:
            printFiles(file)

print('Task 7:')
path = input('Enter folder name: ')

printFiles(path)
