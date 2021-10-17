from random import randint
from quick_sort import quick_sort


def binary_search(element, new_list):
    """Binary search algorithm"""
    if len(new_list) == 0:
        raise ValueError(f"{element} not in list")
    elif len(new_list) == 1:
        return new_list[0]
    list_index = [lin for lin in range(len(new_list))]
    while True:
        helf = len(new_list) // 2
        if element == new_list[helf]:
            return list_index[helf]  # return index
            # return new_list[helf]  # return element
        if helf == 1:
            if element == new_list[helf - 1]:
                return list_index[helf - 1]  # return index
                # return new_list[helf - 1]  # return element
            return list_index[helf + 1]  # return index
            # return new_list[helf + 1]  # return element
        elif element < new_list[helf]:
            new_list = new_list[0:helf]
            list_index = list_index[0:helf]
        elif element > new_list[helf]:
            new_list = new_list[helf + 1:len(new_list)]
            list_index = list_index[helf + 1:len(list_index)]

# a = [-1, 0, 5, 17, 29, 31, 42, 56, 78, 85, 91, 93, 94, 96, 100, "101"]
# b = binary_search(a[3], a)
# print(a, b, sep="\n")
