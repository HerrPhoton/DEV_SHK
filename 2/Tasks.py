import sys
import random
import re

#============================================================================================================
print('Task 1: ')

str = input('Enter the string: ').lower().replace(' ', '')
str1 = ''.join(reversed(str));

if str == str1:
    print('This string is a polyndrom\n')
else:
    print('This string is not a polyndrom\n')

#============================================================================================================
print('Task 2: ')

words = input('Enter the string: ').split()

cnt = 0
word = ''

for x in words:
    if len(x) > cnt:
        cnt = len(x)
        word = x

print('The longest word is', word, '\n')

#============================================================================================================

print('Task 3: ')

lstLen = random.randint(0, 20)
lst = [random.randint(-1000, 1000) for i in range(lstLen)]

oddCnt = 0
evenCnt = 0

for i in range(lstLen):

    if lst[i] % 2 == 0:
        evenCnt += 1
    else:
        oddCnt += 1

print('The list', lst, '\nhas', evenCnt, 'even and', oddCnt, 'odd numbers\n')

#============================================================================================================

print('Task 4: ')

str = input('Enter some string: ').lower()

dct = {'скупой': 'жадный', 'кидать': 'бросать', 'очи': 'глаза'}
keys = dct.keys()

for key in keys:
    str = re.sub(key, dct[key], str)

print(str, '\n')

#============================================================================================================
print('task 5: ')


def fib(n):

    if n in (1, 2):
        return 1

    return fib(n - 1) + fib(n - 2)

n = int(input('enter n-th fibonacci number: '))
print(fib(n), '\n')

#============================================================================================================
print('Task 6: ')

file = input('Enter the path to the file: ')

strsCnt = 0
wordsCnt = 0
lettrsCnt = 0

reg = re.compile('[^a-zA-Z]')

with open(file, 'r') as file:

    for line in file:
        strsCnt += 1

        wordsInLine = line.split()
        wordsCnt += len(wordsInLine)

        lettrsCnt += len(reg.sub('', line))

print('The file has', strsCnt, 'lines', wordsCnt, 'words and',  lettrsCnt, 'letters\n')

#============================================================================================================
print('Task 7: ')

def geom_Prog(b1 = 2, q = 2, n = 1):
    
    #while (True):
    while (n < 100):
        print(b1 * q ** (n-1))
        n += 1

geom_Prog()