"""Testing functions
 quick sort, factorial, binary search"""
import math
import pytest
from recursive_factorial import my_factorial
from random import randint, sample
from quick_sort import quick_sort
from binary_search import binary_search


def lists_gen():
    """Generate 50 sorted quick sort function lists
    15 random integer values in each  from 0 to 1000
    """
    basic_list = [gen for gen in range(1000)]
    nested_lists = []
    for _ in range(50):
        interim_list = quick_sort(sample(basic_list, 15))
        nested_lists.append(interim_list)
    return nested_lists


@pytest.mark.parametrize("lists_generator", [lists_gen()])
def test_quick_sort(lists_generator):
    """Test of quick sort function

    The result of quick sort function
    for each of 1000 random generated lists
    should be equal to result of sorted() method
    """
    counter = 0
    while counter < 50:
        test = lists_generator[counter]
        assert quick_sort(test) == sorted(test), "equal should be"
        counter += 1


@pytest.mark.parametrize("num", [1, 11, 4, 5, 8])
def test_factorial(num):
    """Test of recursive factorial function

    The result of binary search function for each of (1, 11, 4, 5, 8)
    numbers, should be equal to result of math.factorial() method
    """
    assert my_factorial(num) == math.factorial(num), "equal should be"


@pytest.mark.parametrize("lists_generator", [lists_gen()])
def test_binary_search(lists_generator):
    """Test of binary search function

    The result of binary search index
    for each of 50 random generated lists
    should be equal to result of list.index() method
    """
    counter = 0
    while counter < 50:
        test = lists_generator[counter]
        test_val = randint(0, 14)
        assert binary_search(test[test_val], test) == test.index(test[test_val]), "equal should be"
        counter += 1
