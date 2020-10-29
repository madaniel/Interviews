import numpy as np


# mat = [[3, 6, 7], [20, 20, 20], [10, 2, 3]]
path = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# trace = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def findSumIterator(mat, path, summ, x, y):
    if any([x > len(mat[0])-1, y > len(mat)-1]):
        return False

    if findSum(mat, path, summ, x, y):
        return True

    return findSumIterator(mat, path, summ, x+1, y) or findSumIterator(mat, path, summ, x, y+1)


def findSum(mat, path, summ, x, y):
    if any([summ < 0, x < 0, y < 0, x > len(mat[0]) - 1, y > len(mat) - 1, path[y][x]==1]):
        return False

    if summ == 0:
        print "Found"
        return True

    print "({},{}) mat[y][x]={} sum={}".format(y, x, mat[y][x], summ)
    path[y][x] = 1

    if x < len(mat[0])-1 and findSum(mat, path, summ - mat[y][x], x + 1, y):
        return True

    elif y < len(mat)-1 and findSum(mat, path, summ - mat[y][x], x, y + 1):
        return True

    elif y > 0 and findSum(mat, path, summ - mat[y][x], x, y - 1):
        return True

    elif x > 0 and findSum(mat, path, summ - mat[y][x], x - 1, y):
        return True

    else:
        path[y][x] = 0
        return False


#assert findSumIterator([[3, 6, 7], [20, 20, 20], [10, 2, 3]], path, 5, 0, 0) == True
#assert findSumIterator([[3, 6, 7], [20, 20, 20], [10, 6, 6]], path, 5, 0, 0) == False
#assert findSumIterator([[3, 6, 7], [4, 20, 20], [1, 6, 6]], path, 5, 0, 0) == True
#assert findSumIterator([[1, 1, 1], [6, 6, 1], [10, 6, 1]], path, 5, 0, 0) == True
#assert findSumIterator([[1, 6, 7], [2, 20, 20], [1, 2, 3]], path, 5, 0, 0) == True
#assert findSumIterator([[1, 1, 0], [10, 1, 10], [10, 1, 1]], path, 5, 0, 0) == True

print "\n"
print np.matrix(path)


