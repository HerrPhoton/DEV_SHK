import argparse as ap
import numpy as np
import random

parser = ap.ArgumentParser()
parser.add_argument('file_1', type = str)
parser.add_argument('file_2', type = str)
parser.add_argument('p', type = float)

args = parser.parse_args()

with open(args.file_1) as real:
    with open(args.file_2) as synth:

        to_lst = lambda line: list(map(int, line.split()))

        lst1 = to_lst(real.readline())
        lst2 = to_lst(synth.readline())
        lst = lst1 + lst2

        print('Real data:', lst1)
        print('Synthetic data:', lst2)
        print('Probability of Synthetic Data:', args.p, '\n')

        arr = np.array(lst).reshape(2, -1) 

#====================================================================================================================
#Method 1
 
        data = np.apply_along_axis(lambda colm: np.random.choice(colm, replace = False, p = [1 - args.p, args.p]), 0, arr)
        print('Shuffled arrays using the 1st method:', data)

#====================================================================================================================
#Method 2
    
        def take_data(colm):

            if random.random() > args.p:
                return colm[0]

            return colm[1]


        data = np.apply_along_axis(take_data, 0, arr)
        print('Shuffled arrays using the 2nd method:', data)