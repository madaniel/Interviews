import unittest
from src.find_duplicates import solution_1, solution_2, solution_3


class FindDuplicates(unittest.TestCase):

    # (input, expected)
    test_data = (
        ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
        ([1, 4, 3, 2, 7, 8, 2, 3, 3, 1], [1, 2, 3]),

    )

    def test_solution_1(self):
        for test in self.test_data:
            self.assertEqual(solution_1(test[0]), test[1])

    def test_solution_2(self):
        for test in self.test_data:
            self.assertEqual(solution_2(test[0]), test[1])

    def test_solution_3(self):
        for test in self.test_data:
            self.assertEqual(solution_3(test[0]), test[1])

if __name__ == '__main__':
    unittest.main()
