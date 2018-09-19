# 迭代
def iteration():
    for i in range(1, 101):
        if i % 7 == 0:
            print(i)


# iteration()


# Python中，迭代永远是取出元素本身，而非元素的索引。
# 索引迭代
def __enumerate(x):
    y = zip(range(1, len(x) + 1), x)
    for index, name in y:
        print(index, '-', name)


# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# __enumerate(L)


# 迭代dict的value
def __itervalues(x):
    __sum = 0.0
    for score in x.values():
        __sum = __sum + score
    print(__sum / len(x))


# d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
# __itervalues(d)

# 迭代dict的key和value
def iterKeyAndValues(d):
    sum_ = 0.0
    for name, score in d.items():
        print(name, ':', score)
        sum_ = sum_ + score
    print("average:", sum_ / len(d))


# d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
# iterKeyAndValues(d)

# 生成列表
# print([x * (x + 1) for x in range(1, 100, 2)])

# 复杂表达式
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)


# d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
# tds = [generate_tr(name,score) for name, score in d.items()]
# print ('<table border="1">')
# print ('<tr><th>Name</th><th>Score</th><tr>')
# print ('\n'.join(tds))
# print ('</table>')

# 条件过滤
def fun1(l):
    return [x.upper() for x in l if isinstance(x, str)]

# print(fun1(["wqe", "qwe", 123]))

# 多层表达式
# print([100 * n1 + 10 * n2 + n3 for n1 in range(1, 10) for n2 in range(0, 10) for n3 in range(0, 10) if n1 == n3])
