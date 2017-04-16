import unittest
from src.stack_min import StackMin


class StackMinTester(unittest.TestCase):

    def test_negative(self):
        # Verify no exceptions raised
        test_stack = StackMin()
        test_stack.stack_pop()
        test_stack.stack_peek()
        self.assertEqual(test_stack.min, None)

    def test_push_and_peek(self):
        test_stack = StackMin()
        test_numbers = [5, 1, 4, 2, 9]

        for item in test_numbers:
            test_stack.stack_push(item)
            self.assertEqual(test_stack.stack_peek(), item)

    def test_pop(self):
        test_stack = StackMin()
        test_numbers = [8, 3, 0, -1, -5, 4, 4]

        for item in test_numbers:
            test_stack.stack_push(item)

        for item in test_numbers[::-1]:
            self.assertEqual(test_stack.stack_pop(), item)

    def test_min(self):
        # Verify the min property updates correctly
        test_stack = StackMin()
        test_numbers = [5, 6, 3, 3, 9, -2, 3]
        min_expected = [5, 5, 3, 3, 3, -2, -2]

        for index, item in enumerate(test_numbers):
            test_stack.stack_push(item)
            self.assertEqual(test_stack.min, min_expected[index])

        for index, item in enumerate(test_numbers):
            self.assertEqual(test_stack.min, min_expected[len(min_expected)-1 - index])
            test_stack.stack_pop()


if __name__ == '__main__':
    unittest.main()
