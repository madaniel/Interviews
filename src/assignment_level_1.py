"""

Step 1:

On the below, you have an abstract class of a basic Stack.
Write additional class which inherit the abstract class with your implementation.

Requirements:

- The stack should created with capacity > 0.
- The stack cannot exceed its own capacity.
- The stack should return True if push succeeded or False if it failed.


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
        Add new item after the last one in stack
        :return: None
        """
        pass

    @abstractmethod
    def pop(self):
        """
        Return and remove last item from stack
        :return: item
        """
        pass

    @abstractmethod
    def peak(self):
        """
        Return the last added item from stack
        :return: None
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


class BasicStack(MetaBasicStack):
    """
    Step 1 solution example
    """

    def __init__(self, capacity):
        assert capacity > 0
        self.capacity = capacity
        self.itemList = []

    def push(self, item):
        if not self.is_full():
            self.itemList.append(item)
            return True

        return False

    def pop(self):
        return self.itemList.pop()

    def peak(self):
        return self.itemList[0]

    def is_full(self):
        return len(self.itemList) == self.capacity

    def is_empty(self):
        return not self.itemList


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


if __name__ == '__main__':
    BasicStackTester.test_1()
    BasicStackTester.test_2()
    BasicStackTester.test_3()
    BasicStackTester.test_4()
    BasicStackTester.test_5()
    BasicStackTester.test_6()

