# 1.Hello, World!
# print("Hello, World!")

# 2.Variables and Types
# change this code
# mystring = "hello"  # str
# myfloat = 10.0  # float
# myint = 20  # int
# testing code
# if mystring == "hello":
#     print("String: %s" % mystring)
# if isinstance(myfloat, float) and myfloat == 10.0:
#     print("Float: %f" % myfloat)
# if isinstance(myint, int) and myint == 20:
#     print("Integer: %d" % myint)

# 3.Lists
# numbers = [1, 2, 3]
# strings = ['hello', 'world']
# names = ["John", "Eric", "Jessica"]
# # write your code here
# second_name = names[1]
# this code should write out the filled arrays and the second name in the names list (Eric).
# print(numbers)
# print(strings)
# print("The second name on the names list is %s" % second_name)

# 4.Basic Operators
# x = object()
# y = object()
#
# # TODO: change this code
# x_list = [x] * 10
# y_list = [y] * 10
# big_list = x_list + y_list
#
# print("x_list contains %d objects" % len(x_list))
# print("y_list contains %d objects" % len(y_list))
# print("big_list contains %d objects" % len(big_list))
#
# # testing code
# if x_list.count(x) == 10 and y_list.count(y) == 10:
#     print("Almost there...")
# if big_list.count(x) == 10 and big_list.count(y) == 10:
#     print("Great!")

# 5.String Formatting
# data = ("John", "Doe", 53.44)
# format_string = "Hello"
#
# print(format_string, "%s %s. Your current balance is $%f" % data)

# 6.Basic String Operations
# s = "Strings are awesome!"

# 7.Conditions
# change this code
# number = 17
# second_number = 0
# first_array = [1, 0, 0]
# second_array = [1, 3]
#
# if number > 15:
#     print("1")
#
# if first_array:
#     print("2")
#
# if len(second_array) == 2:
#     print("3")
#
# if len(first_array) + len(second_array) == 5:
#     print("4")
#
# if first_array and first_array[0] == 1:
#     print("5")
#
# if not second_number:
#     print("6")

# 8.Loops
# numbers = [
#     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#     743, 527
# ]
#
# # your code goes here
# for i in numbers:
#     if i == 237:
#         break
#     if i % 2 == 0:
#         print(i)

# 9.Functions
# Modify this function to return a list of strings as defined above
# def list_benefits():
#     return ["More organized code", "More readable code",
#             "Easier code reuse", "Allowing programmers to share and connect code together"]
#
# # Modify this function to concatenate to each benefit - " is a benefit of functions!"
# def build_sentence(benefit):
#     return benefit + " is a benefit of functions!"
#
# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))
#
# name_the_benefits_of_functions()

# 9_1.Multiple Function Arguments
# edit the functions prototype and implementation
# def foo(a, b, c, *args, **kwargs):
#     return len(args) + len(kwargs)
#
# def bar(a, b, c, *args, **kwargs):
#     return kwargs['magicnumber'] == 7
#
# # test code
# if foo(1,2,3,4) == 1:
#     print("Good.")
# if foo(1,2,3,4,5) == 2:
#     print("Better.")
# if bar(1,2,3,magicnumber = 6) == False:
#     print("Great.")
# if bar(1,2,3,magicnumber = 7) == True:
#     print("Awesome!")

# 10.Docstrings
# def length(i, j):
#     """The length of two dots is: """
#     x, y = i
#     a, b = j
#     return ((x - a) ** 2 + (y - b) ** 2) ** 0.5
#
#
# dot_a, dot_b = (1, 2), (3, 4)
# print(f"{length.__doc__}{length(dot_a, dot_b)}")

# 11.Dictionaries
# phonebook = {
#     "John": 938477566,
#     "Jack": 938377264,
#     "Jill": 947662781
# }
# # your code goes here
# phonebook["Jake"] = 938273443
# del phonebook["Jill"]
#
# # testing code
# if "Jake" in phonebook:
#     print("Jake is listed in the phonebook.")
#
# if "Jill" not in phonebook:
#     print("Jill is not listed in the phonebook.")

# 12.Sets
# a = ["Jake", "John", "Eric"]
# b = ["John", "Jill"]
# c = {i for i in a if i not in b}
# print(c)

# 13.Imports
# from random import randint as ra
# print(ra(0, 10))

# 14.Modules and Packages
# import re
# a=" ".join(sorted(dir(re)))
# b = re.findall(r"\bfind\S+\b", a)
# print(b)



