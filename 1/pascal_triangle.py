import argparse

parser = argparse.ArgumentParser()
parser.add_argument('n', type = int)

args = parser.parse_args()

arr = [[0] * args.n for i in range(args.n)]
strs = ['' for i in range(args.n)]

arr[0][0] = 1

for i in range(args.n):
    for j in range(i + 1):
        
        if (j == 0 or j == i):
            arr[i][j] = 1

        else:
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    for k in range(i + 1):     
        strs[i] += str(arr[i][k])

        if k < i:
            strs[i] += ' '


for i in range(args.n):
    print(strs[i].center(len(strs[args.n - 1])))
