"""Recursive factorial implementation"""


def my_factorial(num):
    """Сalculating factorial of a number"""
    if num == 1:
        return num
    return num * my_factorial(num - 1)


# number = int(input())
# print(my_factorial(number))