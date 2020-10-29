
from abc import ABCMeta, abstractmethod


class Process(object):

    """
    API only
    """

    def __init__(self, pid, priority):
        """
        :type pid: int
        :type priority: int
        """
        assert isinstance(priority, int)
        self.priority = priority
        self.pid = pid


class MetaProcessQueue(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def enqueue(self, process):
        """
        Add process to the queue
        :param process:
        :type: Process
        :return: None
        """
        raise NotImplemented

    @abstractmethod
    def dequeue(self):
        """
        Remove process from the queue
        :return: None
        """
        raise NotImplemented

    @abstractmethod
    def is_empty(self):
        """
        Returns True if queue is empty
        :return: True / False
        """
        raise NotImplemented

    @abstractmethod
    def size(self):
        """
        Returns size of the queue
        :return: int
        """
        raise NotImplemented

    @abstractmethod
    def sort(self):
        """
        Sort processes by priority
        First process to dequeue should be with the highest priority
        :return: None
        """
        raise NotImplemented

    @abstractmethod
    def remove_duplicates(self):
        """
        Remove process with the same pid
        :return: None
        """
        raise NotImplemented

    @abstractmethod
    def execute(self):
        """
        Trigger each process work() method, based on priority
        :return:
        """
        raise NotImplemented
