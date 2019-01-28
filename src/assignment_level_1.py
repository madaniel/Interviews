"""

Step 1:

On the below, you have an abstract class of a basic Stack.
Write additional class which inherit the abstract class with your implementation.

Requirements:

- The stack will accept only int numbers.
- The stack should created with capacity > 0.
- The stack should not exceed its own capacity.


Step 2:

Write tests to verify the functionality of the Stack.
Try to refer to both positive and negative scenarios.
Aim to achieve 100% coverage.

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
    def get_minimum(self):
        """
        Return the minimum value in Stack
        :return: number or None
        """
        pass


class BasicStack(MetaBasicStack):
    """
    Step 1 solution example
    """

    def __init__(self, capacity):
        assert capacity > 0
        self.capacity = capacity
        self.itemList = []

    def push(self, number):
        isinstance(number, int)

        if not self.is_full():
            self.itemList.append(number)
            return True

        return False

    def pop(self):
        if self.itemList:
            return self.itemList.pop()

        return False

    def peak(self):
        return self.itemList[0]

    def is_full(self):
        return len(self.itemList) == self.capacity

    def is_empty(self):
        return not self.itemList

    def get_minimum(self):
        if self.itemList:
            return min(self.itemList)

        return None


class BasicStackTester(object):
    """
    Step 2 solution example
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
        test_stack.pop()
        assert test_stack.get_minimum() == 2
        test_stack.pop()
        assert test_stack.get_minimum() == 2
        test_stack.pop()
        assert not test_stack.get_minimum()


if __name__ == '__main__':
    BasicStackTester.test_1()
    BasicStackTester.test_2()
    BasicStackTester.test_3()
    BasicStackTester.test_4()
    BasicStackTester.test_5()
    BasicStackTester.test_6()
    BasicStackTester.test_7()

