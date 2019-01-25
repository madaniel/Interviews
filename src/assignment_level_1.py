"""
On the below, you have abstract class of a basic Stack.
Write additional class which inherit the abstract class with your implementation.
"""

from abc import ABCMeta, abstractmethod


class BasicStack(ABCMeta):

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

