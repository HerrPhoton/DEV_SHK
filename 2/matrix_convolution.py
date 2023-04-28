import argparse

parser = argparse.ArgumentParser()
parser.add_argument('inp', type = str)
parser.add_argument('out', type = str)

args = parser.parse_args()

matr1 = []
matr2 = []

with open(args.inp, 'r') as inp:

    flag = False

    for line in inp:

        if (line == '\n'):
            flag = True
            continue

        if (flag == False):
            matr1.append(list(map(int, line.split())))
        else:
            matr2.append(list(map(int, line.split())))


def convolution(mtx1, mtx2):

    sum = 0
    n = len(mtx1) - len(mtx2) + 1
    m = len(mtx1[0]) - len(mtx2[0]) + 1

    res = [[] for i in range(n)]

    for i in range(n):
        for j in range(m):

            sum = 0

            for u in range(len(mtx2)):
                for v in range(len(mtx2[0])):

                    sum += mtx1[i + u][j + v] * mtx2[u][v]

            res[i].append(sum)

    return res


with open(args.out, 'w') as out:

    res = convolution(matr1, matr2)

    for i in range(len(res)):
        out.write(" ".join(map(str, res[i])) + '\n')