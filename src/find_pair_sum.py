
"""
This functions should return all the numbers sums to a requested number 
"""


def solution_1_generator(data, target_number):
    """
    Using sort 
    Running time Complexity: O(n**2 log n)

    :param target_number: requested number for sum
    :param data: list of numbers to check 
    :return: list of numbers summed to target number
    """
    data.sort()

    right_index = len(data) - 1
    left_index = 0

    while left_index != right_index:

        current_sum = data[left_index] + data[right_index]

        # Check if the following numbers are summed as requested
        if current_sum == target_number:
            yield (data[left_index], data[right_index])

        # Move the right index for larger or equal sums then number
        if current_sum >= target_number:
            right_index -= 1

        # Move the left index for smaller sums then number
        if current_sum < target_number:
            left_index += 1


def solution_2_generator(data, target_number):
    """
    Without using sort 
    Running time Complexity: O(n)
    Space Complexity: O(n)

    :param target_number: requested number for sum
    :param data: list of positive numbers 
    :return: list of numbers summed to target number
    """
    read_numbers = set()

    for number in data:
        # If the complementary to target_number is in set - target_number found
        if (target_number - number) in read_numbers:
            yield (target_number - number, number)
        # Add current number to set
        read_numbers.add(number)


def solution_3_generator(data, target_number):
    """
    Without using sort 
    Running time Complexity: O(n)
    Space Complexity: O(1)

    :param target_number: requested number for sum
    :param data: list of positive numbers 
    :return: list of numbers summed to target number
    """

    for number in data:
        # Can't find two numbers if one is larger than target_number
        if number > target_number:
            continue

        # Setting the index to be zero based
        complementary_number = target_number - abs(number)
        complementary_index = abs(complementary_number) - 1
        number_index = abs(number) - 1

        # Can't find the index if it exceeds the array list length
        if complementary_index >= len(data):
            continue

        # Negative number => number already read once
        if data[complementary_index] < 0:
            yield (abs(complementary_number), abs(number))

        # Tag the read number
        data[number_index] = -abs(data[number_index])


def solution_1(data, target_number):
    return list(set(solution_1_generator(data, target_number)))


def solution_2(data, target_number):
    return list(set(solution_2_generator(data, target_number)))


def solution_3(data, target_number):
    return list(set(solution_3_generator(data, target_number)))
