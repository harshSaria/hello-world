# a = 3  # 3 is an object and a points to that memory location. It's not like what we know from java or cpp
# b = 3  # b will also point to the same memory location as the prev one
# print(id(3))
# print(id(a))
# print(id(b))
# all the above 3 will give same address

# a = 4
# a = 'string'
# print(id(a))
# print(id(4))
# print(id('string'))
# print(a)


# str = "harshsaria"
# str[0] = 'H'
# print(str[0::2])  # start: end: stepSize
# a = 'ha'
# b = 'ha'
# print(id(a))
# print(id(b))
# both will give the same output

# every thing in python is object
# mutable obj value can be changed
# immutable obj value cant be changed
# a = [1, 2, 3]  # mutable
# b = [1, 2, 3]  # mutable
# # b = a
# print(id(a))
# print(id(b))
# different address for a and b
# c = a[0]  # immutable
# d = a[0]  # immutable
# print(id(c))
# print(id(d))

# a = (1, 2, 3)
# b = (1, 2, 3)
# # b = a
# print(id(a))
# print(id(b))

# a = [1, 2, 3]  # mutable
# b = [1, 2, 3]  # mutable
# print(a is b)  # compares addresses
# c = a[0]  # immutable
# d = a[0]  # immutable
# print(c is d)

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b)  # false as address is different
# print(a == b)  # true as a and b are identical

# a = int(input("Enter an integer: "))
# b = int(input("Enter an integer: "))
# print("Sum of ", a, " and ", b, " is ", (a+b))
# print(f"Sum of {a} and {b} is {a+b}")

# str = "hello there"
# print("hello" in str)
# strr = "hell"
# print(str + strr)

# a = [1, 2, 3, 4, 5]
# a.append(6)
# print(a)
# print(a.count(3))
# a.insert(2,7)
# print(a)

# str = "this is a string"
# a = str.split(" ")
# print(a)
# a = str.split("i")
# print(a)
# a, b, c, d = "this is a string".split(" ")
# print(a, b, d, c)

# a = 3
# b = 4
# if a == b:
#     print("Equal")
# elif a != b:
#     print("not equal")
# else:
#     print("fool")

# terminologies
# 1) iterable = going again and again by order. Any object that can be iterated are called iterable.
# 2) iterator =
# a = [1, 2, 3, 4, 5]  # iterable
# a_inter = iter(a) # now it is iterator
# print(a_inter)
# print(next(a_inter))
# print(list(a_inter))
# print(next(a_inter))
# print(next(a_inter))
# print(next(a_inter))
# print(next(a_inter))

# my_list = [17, 24, 33, 41, 52]
# lii=[ ]
# for index in my_list:
#     lii.append(index)
# print(lii)
# down is the good way to implement upper one
# my_list = [17, 24, 33, 41, 52]
# result = [item for item in my_list]
# print(result)

# print(type(range(10)))
# a = range(10)
# my_iter = iter(a)
# print(next(my_iter))
# print(next(my_iter))

# a = range(10,20,2)
# my_iter = iter(a)
# print(next(my_iter))
# print(next(my_iter))

# my_list = [1, 2, 3, 4]
# for item in my_list:
#     print(item)

# for item in range(1, 101):
#     print(item)

my_dict = {
    "a": "apple",
    "b": "boy",
    "c": "china"
}
# for key in my_dict:
#     print(my_dict.get(key))
#
# print(type(my_dict.values()))
# for val in my_dict.values():
#     print(val)

# print(my_dict.keys())

# for key in my_dict:
#     print(my_dict[key])

# program : make a list of numbers. If we encounter an even num, skip the next number.
# my_list = [123, 1234, 2, 233, 342, 4, 5]
# for val in my_list:
#     if val % 2 == 0:
#         print(val)
#         my_list.index(val)+=1


# print(my_list.index(2))
# above idea was correct but grammar was wrong
# below is also the wrong grammar
# for index in range(len(my_list)):
#     if my_list[index] % 2 == 0:
#         print(my_list[index])
#         index += 1

# we cant make an inf loop using for. for in python is diff from that in cpp or java
# i = 0
# while i < len(my_list):
#     if my_list[i] % 2 == 0:
#         print(my_list[i])
#         i += 2
#         # break
#     else:
#         i += 1
# else:  # we can use else with loops but not when we break it
#     print("solution complete")

# i = 0
# while i < len(my_list):
#     if my_list[i] % 2 == 0:
#         print(my_list[i])
#         i += 2
#         # break
#     else:
#         i += 1
# else:  # we can use else with loops but not when we break it
#     print("solution complete", end = '. ')  # next print will be on the same line
#     print("Its really complete")

# unpacking
# my_list = [1, 2, 3, 4]
# a, b, c, d = my_list  # order matters here. will work even with dic and tuples. any iterable can be unpacked
# print(a, b, c, d)
# my_dict = {
#     'a':"apple",
#     'b':'banana',
#     'c':'china'
# }
# d, e, f = my_dict.values()
# print(d, e, f)
# d, e, f = my_dict
# print(d, e, f)
# q, w, e = range(3)
# print(q, w, e)

# zip - combines 2 iterables
# list_1 = [1, 3, 4]
# list_2 = [11, 12, 14]
# list_3 = (12, 12, 12)
# # i want to combine same index elements together
# print(zip(list_1, list_2, list_3))  # this will give zip object
# list_4 = list(zip(list_1, list_2, list_3))
# print(list_4)  # combinations are in form of a tuple
# # will work with any comb of iterables
# a, b, c = zip(list_1, list_2, list_3)  # unpacking zip
# print(a, b, c)

# functions
# def my_function():
#     print('my_function is called')
#
#
# my_function()
# my_function()
# def func():
#     pass  # means do nothing
#
#
# print(func())
# def func(test):
#     if test == 0:
#         return 0
#     else:
#         return f'this is {test}'
#
# # func(0)
# # func(13)
# print(func(0))
# print(func(2))
# def func(test):
#     return test, test + 1, test + 2
#
#
# print(func(12))  # prints as tuple
# a, b, c = func(12)
# print(a, b, c)
# def fun(test_1, test_2, test = 0):  # non default should follow default
#     return test_2, test_1, test
#
# print(1,2,3)
# def fun(test_1, test_2 = 0, test):  # will throw an error as non default followed default
#     return test_2, test_1, test
#
# print(1,2, 3)

# changes after file has been committed
# changed again
# changed again again
# here i have made a change again
# changes here
# changed here again
