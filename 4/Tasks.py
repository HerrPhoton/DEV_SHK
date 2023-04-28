import numpy as np

#=========================================================================================
#Task 1

lst = [1, 2, 2, 2, 5, 6, 0, 1, 0, 9, 0, 2]

print('Task 1:')
print('Initial values:', lst)

arr, freq = np.unique(lst, return_counts = True)

#Find the index of an element in the array of unique values and return the frequency of this element in the array by this index
lst.sort(key = lambda num: freq[np.where(arr == num)][0])

print('Answer:', lst, '\n')


#=========================================================================================
#Task 2

h = 3   
w = 5

print('Task 2:')
print('Height:', h)
print('Weight:', w)
print('Number of pixels:', w * h)

img = np.unique(np.random.randint(256, size = (h * w, 3)), axis = 0)
print('Number of unique colors:', len(img), '\n')

#=========================================================================================
#Task 3

def moving_avg(lst, win):
    
    lst.insert(0,0)
    sums = np.cumsum(np.array(lst))   
    
    return (sums[win:] - sums[:-win]) / win


lst = [1,2,3,4,5,6]
w = 2

print('Task 3:')
print('initial array:', lst)
print('Window size:', w)

print('Answer:', moving_avg(lst, w), '\n')

#=========================================================================================
#Task 4

a = np.random.randint(20, size = (10, 3))

print('Task 4:')
print('Initial values: \n', a, '\n')

a = a[a.all(1)] #Delete rows with null values

a.sort()
a = a[a[:, 2] < a[:,0] + a[:, 1]]

print('Answer: \n', a)
