arr = [7, 4, 3, 2, 5, 9, 6, 1, 2 ,9, 10, 5, 3]
arr1 = [1, 2, 3, 4, 5]

winSize = 3

ln = len(arr)

if winSize > ln:
    winSize = ln

queue = []

for i in range(ln - winSize + 1):
    
    queue.append(arr[i])
   
    while (len(queue) > 2 and queue[-2] < queue[-1]):
        queue.pop(-2)

    if (arr[i - winSize] == queue[0] and i >= winSize):
        print(queue[0], end = ' ')
        queue.pop(0)
    

print('\n')
        



