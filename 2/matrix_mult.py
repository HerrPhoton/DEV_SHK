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


def mult_matr(mtx1, mtx2):

    n1 = len(mtx1)
    m1 = len(mtx1[0])
    n2 = len(mtx2)
    m2 = len(mtx2[0])
    res = [[] for i in range(n1)]

    if (n2 != m1):
        return []          

    for i in range(n1):
        for j in range(m2):

            sum = 0

            for k in range(n2):
                sum += mtx1[i][k] * mtx2[k][j]

            res[i].append(sum)

    return res


with open(args.out, 'w') as out:

    res = mult_matr(matr1, matr2)

    for i in range(len(res)):
        out.write(" ".join(map(str, res[i])) + '\n')
