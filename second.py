import math


# 高阶函数
def add(x, y, f):
    return f(x) + f(y)


print(add(25, 9, math.sqrt))


#test