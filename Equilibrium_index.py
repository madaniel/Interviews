import unittest

"""
The functions should return the index which the sum from its left equals to its right
"""


def trivial(data):
    if not data:
        yield None

    if len(data) == 1:
        yield 0

    for index, number in enumerate(data):
        left_sum = sum(data[:index + 1])
        right_sum = sum(data[index:])

        if left_sum == right_sum and index != 0:
            yield index


#class Equilibrium(unittest.TestCase):
data = [-7, 1, 5, 2, -4, 3, 0]
# data = [1, -1, 0]

if __name__ == '__main__':
    for result in trivial(data):
        print result



