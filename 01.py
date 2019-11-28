#!/usr/bin/python
# -*- coding: UTF-8 -*-

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "师姐你好"  # 字符串

print(counter)
print(miles)
print(name)

a, b, c = 1, 2, "john"

num = 5
if num == 3:
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:
    print('error')
else:
    print('roadman')

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)

# raw_input("按下 enter 键退出，其他任意键显示...\n")

# 字符串截取
s = 'abcdef'
print(s[1:5])

# 数组合并
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print(list+tinylist)

# 字典
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
print(dict)
print(dict[2])

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(tinydict['name'])

print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值

# 数据类型转换

e = 1.00001
f = 1
print(int(e))
print('--------------------',float(f))
# 函数
def demo(aa,bb):
    return aa+bb

print(demo(11,22))

_a = 1
while _a<10:
    _a +=1
    print(_a)

count = 0
while count < 5:
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")

###数组

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print('------', fruit)

fruits2 = ['banana', 'apple',  'mango']
for index in range(len(fruits2)):
   print('_____ 2:', fruits2[index])

_b = 'abcd'
print(_b.capitalize())
print(_b.center(8))

list11 = ['physics', 'chemistry', 1997, 2000,2000]
list22 = [1, 2, 3, 4, 5, 6, 7 ]
print(list11[0])
list11.append('Google')
print(list11)
del list11[0]
print(list11)
print(list11.count(2000))

# str = raw_input("请输入：")
# print("你输入的内容是: ", str)

# json
jsonList = [{'id':1,'name': 'john','code':6734, 'dept': 'sales'},{'id':2,'name': 'john','code':6734, 'dept': 'sales'}]
jsonListIndex = 0
for index in jsonList:
    index['cc'] = jsonListIndex
    # 向json数组中添加元素
    jsonListIndex = jsonListIndex+1
    # 删除json数组中的元素
    del index['code']
    print(index)
