def is_sorted(integers):
    """
    Return True if list of integers is sorted in non-decreasing order and False if not.

    :param integers: a list of integers
    :precondition: all numbers in the list are integers
    :postcondition: parse through list and determine if elements are in non-increasing order
    :return: True if list is not ordered decreasingly, otherwise False.
    >>> is_sorted([1, 2, 3])
    True
    >>> is_sorted([3, 2, 1])
    False
    """

    sorted_list = sorted(integers)
    sort_status = False

    if len(integers) == 0:
        sort_status = False
    elif sorted_list == integers:
        sort_status = True
    elif sorted_list != integers:
        sort_status = False
    return sort_status


def main():
    print(is_sorted([1, 2, 3]))


if __name__ == "__main__":
    main()
