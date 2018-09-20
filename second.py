import math
from functools import reduce


# 高阶函数
def add(x, y, f):
    return f(x) + f(y)


# print(add(25, 9, math.sqrt))


# python中map()函数
def fun1(s):
    return s[0].upper() + s[1:].lower()


# L = ['adam', 'LISA', 'barT']
# print(map(fun1, L))
# for x in map(fun1, L):
#     print(x)

# python中reduce()函数
def fun2(x, y):
    return x * y


# L = reduce(fun2, [2, 4, 5, 7, 12])
# print(L)


# python中filter()函数
def fun3(x):
    r = int(math.sqrt(x))
    return r * r == x


# L = []
# for x in filter(fun3, range(1, 101)):
#     L.append(x)
# print(L)

# python中自定义排序函数
def fun4(x):
    return x.upper()

# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=lambda x: x.upper()))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=fun4, reverse=False))

# python中返回函数
