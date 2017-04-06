
"""
The functions should return the indexes which the sum from its left equals to its right is equals
"""


def solution_1_generator(data):
    """
    Using sum function for each index on iteration
    
    :param data: list of numbers to check 
    :return: list of indexes found 
    """
    if len(data) == 0:
        yield None
        return

    if len(data) == 1:
        yield 0
        return

    for index, number in enumerate(data):
        left_sum = sum(data[:index + 1])
        right_sum = sum(data[index:])

        if left_sum == right_sum:
            yield index


def solution_2_generator(data):
    """
    Without using sum function
    
    :param data: list of numbers to check
    :return: list of indexes found
    """
    if not data:
        yield None
        return

    if len(data) == 1:
        yield 0
        return

    # Sum all the numbers on the array
    total_sum = 0
    for number in data:
        total_sum += number

    left_sum = 0
    right_sum = total_sum

    for index, number in enumerate(data):
        # Decrement right sum
        right_sum -= number

        if left_sum == right_sum:
            yield index

        # Increment left sum
        left_sum += number


def solution_1(data):
    return list(solution_1_generator(data))


def solution_2(data):
    return list(solution_2_generator(data))






