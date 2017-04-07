import unittest
from src.equilibrium import solution_1, solution_2


class Equilibrium(unittest.TestCase):

    # (input, expected)
    test_data = (
        ([], [None]), ([1], [0]), ([1, -1, 0], [2]), ([-7, 1, 5, 2, -4, 3, 0], [3, 6]),
        ([-14, 2, 10, 4, -8, 6, 0, 14, -2, -10, -4, 8, -6], [3, 6, 10])
    )

    def test_solution_1(self):
        for test in self.test_data:
            self.assertEqual(solution_1(test[0]), test[1])

    def test_solution_2(self):
        for test in self.test_data:
            self.assertEqual(solution_2(test[0]), test[1])

if __name__ == '__main__':
    unittest.main()
