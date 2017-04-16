"""
This class represents Stack with minimum property of O(1)
"""


class StackMin:

    def __init__(self):
        self.data = []
        self.min_list = []
        print "New stack created"

    def stack_pop(self):
        if self.is_empty:
            return "Stack is empty"

        if self.stack_peek() == self.min:
            self.min_list.pop()

        return self.data.pop()

    def stack_push(self, num):
        # Record the number if it's less than the last on stack
        if num <= self.min or not self.min:
            self.min_list.append(num)

        self.data.append(num)
        print "{} pushed to stack".format(num)

    def stack_peek(self):
        if self.data:
            return self.data[-1]
        else:
            return None

    @property
    def min(self):
        if self.min_list:
            return self.min_list[-1]
        else:
            return None

    @property
    def is_empty(self):
        if self.data:
            return False
        else:
            return True







