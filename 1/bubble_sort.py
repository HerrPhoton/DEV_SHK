import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('n', type = int)

args = parser.parse_args()

arr = [random.random() for i in range (0, args.n)]

print('\nArray of length', args.n)
print(arr, '\n')

for i in range(1, args.n):
    
    flag = False

    for j in range(0, args.n - i):
        if arr[j] > arr[j + 1]:

             temp = arr[j]
             arr[j] = arr[j + 1]
             arr[j + 1] = temp

             flag = True
     
    if flag == False:
        break

print('Sorted array of length', args.n)
print(arr)
            