
"""
This functions should return all the duplicates on array 
"""


def solution_1_generator(data):
    """
    Using sort 
    Running time Complexity: O(n**2 log(n))

    :param data: list of numbers to check 
    :return: list of duplicated numbers
    """
    data.sort()
    last = None

    for number in data:
        if number == last:
            yield number
        last = number


def solution_2_generator(data):
    """
    Running time Complexity: O(n)
    Space complexity: O(n)

    :param data: 
    :return: 
    """
    read_numbers = set()

    for number in data:
        if number in read_numbers:
            yield number

        read_numbers.add(number)


def solution_3_generator(data):
    """
    Running time Complexity: O(n)
    Space complexity: O(1)

    :param data: list of positive numbers 
    :return: list of duplicated numbers
    """
    for number in data:
        # Setting the index to be zero based
        data_index = abs(number) - 1

        # Negative number => number already read once
        if data[data_index] < 0:
            yield abs(number)
        else:
            # Tag index on array
            data[data_index] = -data[data_index]


def solution_1(data):
    return list(set(solution_1_generator(data)))


def solution_2(data):
    return list(set(solution_2_generator(data)))


def solution_3(data):
    return list(set(solution_3_generator(data)))





















