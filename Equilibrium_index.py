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


class Equilibrium(unittest.TestCase):

    # (input, expected)
    test_data = (
        ([], [None]), ([1], [0]), ([1, -1, 0], [2], ([-7, 1, 5, 2, -4, 3, 0], [3, 6]))
    )

    @staticmethod
    def trivial_run(data):
        result = []
        for index in trivial(data):
            result.append(index)
        return result

    def test_trivial(self):
        for test in self.test_data:
            self.assertEqual(self.trivial_run(test[0]), test[1])

if __name__ == '__main__':
    unittest.main()








