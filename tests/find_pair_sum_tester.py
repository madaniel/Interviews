import unittest
from src.find_pair_sum import solution_1, solution_2, solution_3


class FindPairSum(unittest.TestCase):

    # (input, expected)
    test_data = (
        ([3, 4, 3, 4, 5, 7, 5], 10, [(3, 7), (5, 5)]),
        ([2, 6, 1, 9, 9, 5, 2, 9, 7], 4, [(2, 2)]),
        ([2, 6, 1, 9, 10, 5, 2, 10, 7, 3, 7, 1], 15, [(6, 9), (5, 10)]),

    )

    def test_solution_1(self):
        for test in self.test_data:
            self.assertEqual(solution_1(test[0], test[1]), test[2])

    def test_solution_2(self):
        for test in self.test_data:
            self.assertEqual(solution_2(test[0], test[1]), test[2])

    def test_solution_3(self):
        for test in self.test_data:
            self.assertEqual(solution_3(test[0], test[1]), test[2])

if __name__ == '__main__':
    unittest.main()
