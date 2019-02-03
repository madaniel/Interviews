"""

Step 1:

On the below, you have an abstract class of a basic Stack.
Write additional class which inherit the abstract class with your implementation.

Requirements:

- The stack will accept only int numbers.
- The stack should created with capacity > 0.
- The stack should not exceed its own capacity.
- No need to consider complexity at this time.


Step 2:

Write tests to verify the functionality of the Stack.
Try to refer to both positive and negative scenarios.
Aim to achieve 100% coverage.


Step 3:

Add function get_minimum_fast() to Stack class.
The method should be able to get the minimum number at time-complexity of O(1).


Step 4:

Run the tests you've wrote for get_minimum_fast() and make sure they all pass.


"""

from abc import ABCMeta, abstractmethod


class MetaBasicStack(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def push(self, item):
        """
        Add new number after the last one in stack
        :return: True if succeeded or False if failed
        """
        pass

    @abstractmethod
    def pop(self):
        """
        Return and remove last number from stack
        :return: number if succeeded or False if failed
        """
        pass

    @abstractmethod
    def peak(self):
        """
        Return the last added number from stack
        :return: number
        """
        pass

    @abstractmethod
    def is_full(self):
        """
        Return True or False if the stack is full
        :return: True / False
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Return True or False if the stack is empty
        :return: True / False
        """
        pass

    @abstractmethod
    def get_size(self):
        """
        Return the count of the numbers in the stack
        :return: number or None
        """
        pass

    @abstractmethod
    def get_minimum(self):
        """
        Return the minimum value in Stack
        :return: number or None
        """
        pass

    @abstractmethod
    def get_second_minimum(self):
        """
        Return the next smallest number after the minimum
        :return: number or None
        """
        pass


class BasicStack(MetaBasicStack):
    """
    Step 1 + 3 solution example
    """

    def __init__(self, capacity):
        assert capacity > 0
        self.capacity = capacity
        self.itemList = []
        # For get_minimum_fast()
        self.minList = []

    def push(self, number):
        isinstance(number, int)

        if not self.is_full():
            self.itemList.append(number)

            # For get_minimum_fast()
            if not self.minList or number <= self.minList[-1]:
                self.minList.append(number)

            return True

        return False

    def pop(self):
        if self.is_empty():
            return False

        # For get_minimum_fast()
        if self.itemList[-1] == self.minList[-1]:
            self.minList.pop()

        return self.itemList.pop()

    def peak(self):
        return self.itemList[-1]

    def is_full(self):
        return self.get_size() == self.capacity

    def is_empty(self):
        return not self.itemList

    def get_size(self):
        return len(self.itemList)

    def get_minimum(self):
        if self.is_empty():
            return None

        min_number = None

        for number in self.itemList:

            if number < min_number or min_number is None:
                min_number = number

        return min_number

    def get_second_minimum(self):
        if self.get_size() < 2:
            return None

        first_min = None
        second_min = None

        for number in self.itemList:

            if number < first_min or first_min is None:
                second_min = first_min
                first_min = number

            elif number < second_min or second_min is None:
                second_min = number

        return second_min

    def get_minimum_fast(self):
        if not self.minList:
            return None

        return self.minList[-1]


class BasicStackTester(object):
    """
    Step 2 + 4 solution example
    """

    @staticmethod
    def test_1():
        # Basic usage
        test_stack = BasicStack(capacity=3)
        assert not test_stack.is_full()
        assert test_stack.is_empty()
        assert test_stack.push(1)
        assert not test_stack.is_empty()
        assert test_stack.push(2)
        assert test_stack.push(3)
        assert test_stack.is_full()

    @staticmethod
    def test_2():
        # pop() verification
        test_stack = BasicStack(capacity=3)
        assert test_stack.push(1)
        assert test_stack.pop() == 1
        assert test_stack.is_empty()
        assert not test_stack.pop()

    @staticmethod
    def test_3():
        # stack order (LIFO) verification
        test_stack = BasicStack(capacity=3)
        assert test_stack.push(1)
        assert test_stack.push(2)
        assert test_stack.pop() == 2
        assert test_stack.pop() == 1

    @staticmethod
    def test_4():
        # peak() verification
        test_stack = BasicStack(capacity=3)
        assert test_stack.push(1)
        assert test_stack.peak() == 1
        assert not test_stack.is_empty()
        assert test_stack.push(3)
        assert test_stack.peak() == 3
        assert test_stack.pop()
        assert test_stack.peak() == 1

    @staticmethod
    def test_5():
        # Requirement verification
        test_stack = BasicStack(capacity=3)
        assert test_stack.push(1)
        assert test_stack.push(2)
        assert test_stack.push(3)
        assert not test_stack.push(4)
        # Data retained
        assert test_stack.pop() == 3
        assert test_stack.pop() == 2
        assert test_stack.pop() == 1

    @staticmethod
    def test_6():
        # Requirement verification
        try:
            BasicStack(capacity=0)
        except AssertionError:
            pass
        else:
            assert False

    @staticmethod
    def test_7():
        # get_size verification
        test_stack = BasicStack(capacity=3)
        assert test_stack.get_size() == 0
        assert test_stack.push(3)
        assert test_stack.get_size() == 1
        assert test_stack.push(5)
        assert test_stack.get_size() == 2
        assert test_stack.push(9)
        assert test_stack.get_size() == 3
        assert test_stack.pop()
        assert test_stack.get_size() == 2
        assert test_stack.pop()
        assert test_stack.get_size() == 1
        assert test_stack.pop()
        assert test_stack.get_size() == 0

    @staticmethod
    def test_8():
        # get_minimum() verification
        test_stack = BasicStack(capacity=3)
        # No minimum when stack is empty
        assert not test_stack.get_minimum()
        assert test_stack.push(2)
        assert test_stack.get_minimum() == 2
        assert test_stack.push(3)
        assert test_stack.get_minimum() == 2
        assert test_stack.push(1)
        assert test_stack.get_minimum() == 1
        assert test_stack.pop()
        assert test_stack.get_minimum() == 2
        assert test_stack.pop()
        assert test_stack.get_minimum() == 2
        assert test_stack.pop()
        assert not test_stack.get_minimum()

    @staticmethod
    def test_9():
        # get_second_minimum() verification
        test_stack = BasicStack(capacity=3)
        # No second minimum when stack is empty
        assert not test_stack.get_second_minimum()
        assert test_stack.push(2)
        # No second minimum when there's only one number
        assert not test_stack.get_second_minimum()
        assert test_stack.push(3)
        assert test_stack.get_second_minimum() == 3
        assert test_stack.push(1)
        assert test_stack.get_second_minimum() == 2
        test_stack.pop()
        assert test_stack.get_second_minimum() == 3
        test_stack.pop()
        assert not test_stack.get_second_minimum()
        test_stack.pop()
        assert not test_stack.get_second_minimum()

    @staticmethod
    def test_10():
        # get_minimum_fast() verification
        test_stack = BasicStack(capacity=3)
        # No minimum when stack is empty
        assert not test_stack.get_minimum_fast()
        assert test_stack.push(2)
        assert test_stack.get_minimum_fast() == 2
        assert test_stack.push(3)
        assert test_stack.get_minimum_fast() == 2
        assert test_stack.push(1)
        assert test_stack.get_minimum_fast() == 1
        assert test_stack.pop()
        assert test_stack.get_minimum_fast() == 2
        assert test_stack.pop()
        assert test_stack.get_minimum_fast() == 2
        assert test_stack.pop()
        assert not test_stack.get_minimum_fast()


if __name__ == '__main__':
    BasicStackTester.test_1()
    BasicStackTester.test_2()
    BasicStackTester.test_3()
    BasicStackTester.test_4()
    BasicStackTester.test_5()
    BasicStackTester.test_6()
    BasicStackTester.test_7()
    BasicStackTester.test_8()
    BasicStackTester.test_9()
    BasicStackTester.test_10()
