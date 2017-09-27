# -*- coding: utf-8 -*-
#上面一行语句的作用是设置文件的编码

#第一个python程序，永远的Hello,world!
#在标准输出设备上打印Hello,world!
# print("Hello,world!")
#字符串用单双引号都可以
# print('Hello,大神')
# 在3.0以前print不是一个真正的函数 因此在那里使用print时可以不用写括号
# 但在3.0以后print是一个真正的函数，调用是必须写括号

# python中标识符的命名规则与C语言类似
# 可包含数字，字母，下划线
# 不能以数字开头
# 下面这些变量的命名都是合法的
# a = 1
# a2 = 2
# a_b = 3
# _a = 4

# 大多数编程语言中表示八进制的整数时以0开头 
# 而python中的八进制以0o开头 还有0b,0x 分别为二进制与十六进制整数的前缀
# print(0b11)
# print(0o11)
# print(0x11)

# 获取用户的输入 input函数
# input函数会等待用户输入一行字符串 用户按下回车时结束
# line = input()
# print(line)
# input可以接收一个字符串 作为提示
# name = input('Enter your name: ')
# print('Hello '+name) #字符串可以用+连接
# 在3.0以前input函数的功能由raw_input函数实现

# print可以接受多个参数 默认以空格分隔输出
# print('hello','Tom')
# print('i','love','you')

# python中以模块组成程序文件 相当于java中的包
# 导入数学模块
# import math
# 可以通过模块.函数名来调用模块中的函数
# print(math.ceil(1.5))
# print(math.floor(1.5))
# print(math.sqrt(9))

# 导入模块中的指定成员
# from math import sin
# print(sin(3.14/2))

# 导入模块中的所有成员
# from math import *
# print(sqrt(5))

# python本身支持复数 复数单位用j或J表示
# 虚部即使为1也不能省略
# print(1+1j)
# print(1+2j+(1+3j))

# 复数范围内的数学模块 cmath
# import cmath
# print(cmath.sqrt(-1))

# 字符串 start========================================================================================
# 字符串 单双引号均可作为字符串的定界符
# 单引号括起来的字符串
# print('Hello world')
# print('he said:"I love her"')
# 双引号括起来的字符串
# print("Hello")
# print("let's go")
# 使用转义序列
# print('let\'s go!')
# print("You say:\"forget it\"")
# 三引号(单双引号都可以)括起来的字符串 非常适用于表达大段的文本 
# 如果不希望在一行的最后面产生换行 请在后面加上\ 表示连续的文本
# s = '''Jack:"Do you love me?"
# Rose:"No,I love Jerry"
# Jack:"It doesn't matter.Let's go to play!"\
# '''
# print(s)

# 原始字符串 有时候不希望字符串中的\转义字符 这时可以在字符串前面加上r
# print(r'C:\nhome\movie')
# print(r'abc\\n')

# python3以前字符串中的字符采用8位ASCII编码 如果要使用unicode字符串则需要加u
# us = u'你好abc'
# print(us)
# python3以后所有的字符串都采用unicode字符 所有不再需要加u
# us = '大家hello'
# print(us)

# 拼接字符串 可以使用+
# s1 = 'Let her'
# s2 = ' go'
# s3 = s1+s2
# print(s3)

# 字符串与数字相乘表示重复字符串
# s = 'a'
# print(s*10)

# str与repr 将值转换为字符串
# str 转换为字符串
# repr 转换为合法的python表达式字符串 因此会给字符串带引号
# a = 23
# a = 'abc'
# print(str(a))
# print(repr(a))

# 不能直接将字符串与数字相加
# print('123'+4) #TypeError: must be str, not int

# python中的任何东西都是对象 可以使用type函数返回一个对象的类
# strClass = type('abc')
# print(strClass) #<class 'str'>
# print(strClass == str) #True
# print(strClass is str) #True
# 因此任何字符串对象 都是str类的实例 isinstance函数可以判断一个对象是否为某个类型的实例
# print(isinstance('abc',str)) #True

# 内置函数 我们前面直接使用的str,repr的函数被称为python的内置函数
# python内置了60多个函数 参见 https://docs.python.org/3.6/library/functions.html?highlight=built

# ord返回一个Unicode字符的代码点 与chr互为逆操作
# print(ord('A'))
# print(ord('德'))
# chr返回一个Unicode代码点所代表的字符
# print(chr(97))
# print(chr(24503))

# 字符串是字符串构成的序列 序列在python中是许多数据类型的公共特性 如：列表，元组，字典
# 可以像所有数组那样对索引字符串中的字符
# s = 'abcde'
# print(s[0])
# print(s[-1]) #支持负数索引

# 序列可以索引 并且支持切片操作 所以字符串也支持切片
# s = 'abcdef'
# print(s[0:3])
# print(s[0:]) #可复制字符串 
# print(s[:]) #与上面的相同
#指定步长
# print(s[::2]) #ace 
# print(s[-1:-3:-1]) #fe

# 字符串是不可变对象 因此不能通过索引的方式改变字符串
# s = 'abc'
# s[0] = 0

# python字符串常见操作

#内置函数len可返回序列的长度 
# 1)字符串的长度
# print(len('abc')) #2
# print(len('德德')) #3

# 2)检查一个字符串是否包含指定的字符串
# 检查一个对象是否在序列中可以使用in操作符
# 因此可以使用in检查一个字符串是否出现在另一个字符串中
# s = 'python is wonderful'
# print('is' in s) #True
# print('iss' in s) #False
# not in与in意思相反

# 3)查找子串
# 3.1)查找子串第一次出现的索引
# s = 'thinking'
# print(s.find('in')) #2
# 如果没有找到则返回-1
# print(s.find('inn'))
# 第二个参数可以指定搜索的起始位置
# print(s.find('in',3)) #5
# 第三个参数指定搜索的结束位置(不包括)
# print(s.find('in',1,5))
# 3.2)查找子串最后一次出现的索引
# print(s.rfind('in')) #5
# print(s.rfind('in',0,5)) #2

# 4)子串出现的次数 没有则返回0
# str.count(sub[, start[, end]])
# s = 'aaabbaa'
# print(s.count('aa')) #2
# print(s.count('aa',3)) #1
# print(s.count('aa',0,2)) #1

# 5)大小写转换
# s = 'aB'
# print(s.lower())
# print(s.upper())

# 6)判断字符串是否以指定的字符串开头或结尾
# str.startswith(prefix[, start[, end]])
# str.endswith(suffix[, start[, end]])
# s = 'abc'
# print(s.startswith('a'))
# print(s.startswith('A'))
# print(s.endswith('c'))
# print(s.endswith('C'))

# 7)替换字符串中的子串为指定的字符串 返回替换后的字符串
# str.replace(old, new[, count])
# s = 'i love you,but you love him'
# print(s.replace('love','LOVE'))
# print(s.replace('love','LOVE',1))

# 7.2)maketrans与translate
# 静态方法maketrans用于构建一个ascii字符的转换表
# table = str.maketrans('cs','kz') #将c->k s->z
#translate方法根据提供的转换来转换原字符串中的字符
# s = 'core test'.translate(table)
# print(s) #kore tezt
# 8)分割字符串 返回一个列表
# str.split(sep=None, maxsplit=-1)
# s = '1 2  3\t4\n5'
#默认用空白字符串分割
# print(s.split()) 
# print('1,2,3'.split(',')) #['1', '2', '3']
# print('1,2,,3'.split(',')) #['1', '2', '', '3']
# print('1,2,3,'.split(',')) #['1', '2', '3', '']
# print(',1,2,3'.split(',')) #['', 1', '2', '3']
# print('1<>2<>3'.split('<>')) #['1', '2', '3']

# 9)用当前字符串拼接多个字符串
# 以下三个均输出'1,2,3'
# print(','.join(['1','2','3']))
# print(','.join(('1','2','3')))
# print(','.join('123'))

# 10)去除两端指定的字符 默认为空白字符
# str.strip([chars])
# print('  abc  '.strip())
# print('**abc**'.strip('*'))
# print('www.example.com'.strip('cmowz.')) #example
#类似的方法还有lstrip,rstrip

# 11)判断一个字符串内容是否为纯数字
# str.isnumeric()
# print('123'.isnumeric()) #True
# print('-123'.isnumeric()) #False
# print('12.3'.isnumeric()) #False
# print('-12.3'.isnumeric()) #False
# print('0b11'.isnumeric()) #False
# print('0o11'.isnumeric()) #False
# print('0x41'.isnumeric()) #False

# 12)返回字符串中的所有行组成额列表
# s = 'let her go\nDon not call me that\n'
# print(s.splitlines()) #['let her go', 'Don not call me that']

# 反转字符串并返回
# print('abc'[::-1])

# 13)字符串格式化
# str.format(*args, **kwargs)
# 详情参见 https://docs.python.org/3.6/library/string.html#formatstrings
#{}为占位符
# print('Jack loves {}'.format('Rose')) #Jack loves Rose
# print('{}+{}={}'.format(1,2,3)) #1+2=3
# print('{name} is {desc}'.format(name="Tom",desc="shiny")) #Tom is shiny
# print('name={0[name]},age={0[age]}'.format({'name':'Jack','age':23})) #name=Jack,age=23

# class Person(object):
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
# p = Person('Jack',23)
# print('name={p.name},age={p.age}'.format(p=p)) #name=Jack,age=23

# print('{0[0]},{0[1]}'.format(['hello','world']))
#f表示浮动数格式
# print('{:f}'.format(1.2346)) #1.234500
# # 指定精度
# print('{:.3f}'.format(1.2346)) #1.235
# # 指定宽度
# print('{:10f}'.format(1.2346)) #  1.234600
# # 同时指定宽度与精度
# print('{:10.2f}'.format(1.2346)) #      1.23
# # 左对齐
# print('{:<10f}'.format(1.2346)) #1.234600
# # 显示符号
# print('{:<+10f}'.format(1.2346)) #+1.234600
# # 补足宽度
# print('{:010f}'.format(1.2346)) #001.234600
# 参数指定宽度
# s = 'abc'
# print('{0:>{width}}'.format('abc',width=len(s)*2))

# 按不同的进制输出整数
# print('int:{0:d} hex:{0:x} oct:{0:o} bin:{0:b}'.format(12))

# 使用逗号作为千分隔符
# print('{:,}'.format(123456789234))

#百分数
# print('{:.2%}'.format(5/10)) #50.00%

# 格式化日期时间
# from datetime import datetime
# d = datetime.now()
# print('{:%Y-%m-%d %H:%M:%S}'.format(d))

# 14)老式的字符串格式
# 格式说明符与C语言printf一致
# 语法 格式化字符串 % 参数
# s = 'Hello %s!' % 'python'
# print(s)
# s = 'name=%s,age=%d' % ('Jack',23)
# print(s)
# print('price=%.2f' % 234.8789)
# print('%10.5s' % 'Guido van Rossum')
# 使用字典作为参数
# print('%(name)s scored %(score)d' % zidandf{'name':'Jack','score':89})


# 15)模板字符串
# string模块提供了模板字符串功能
# from string import Template
# t = Template('Hello $who')
# s = t.substitute(who='Tom')
# print(s)

# t = Template('$a and $b')
# # s = t.substitute(a='safe',b='fast')
# d = {'a':'safe','b':'fast'}
# s = t.substitute(d)
# print(s)

# 如果替换额是字符串一部分 则必须用花括号括起来
# t = Template('eat ${f}s')
# s = t.substitute(f='apple')
# print(s)

# 可以使用$$插入美元符号
# t = Template('$$ {}')
# s = t.substitute()
# print(s) #$ {}

# 如果缺少值则报错
# t = Template('$who likes $what')
# # s = t.substitute(who='Tom') #KeyError: 'what'
# print(s) 
# # safe_substitute不会报错 而是把不匹配的当作字符串
# s = t.safe_substitute(who='Tom') 
# # print(s)#Tom likes $what



# 字符串 end========================================================================================

# 数值型 numeric
# 整数类型 int
# 整数对象是int类的实例
# inta = 12
# intb = 0b11
# intc = 0o11
# intd = 0x41
# inte = int() #默认返回0
# intf = int(13)
# intg = int('13',8) #第二个参数指定进制 此时第一个参数必须为字符串
# print(inta,intb,intc,intd,inte,intf,intg) #12 3 9 65 0 13 11
# 因此int可以实现字符串与整数的互相转换

# 浮点型 float
# f1 = 1.5
# print(f1)
# print(isinstance(f1,float)) #True

# 布尔类型 只有两个值True，False
# 它是bool类的实例
# a = True
# print(a)
# print(isinstance(a,bool)) #True
# 将任何转换为真值
# print(bool('')) #False
# print(bool(0)) #False
# print(bool(None)) #False
# print(bool([])) #False
# print(bool((0,))) #True

#序列 
#序列是python中最基本的数据结构 它是有序元素的集合
#python中的内置序列有：字符串，列表，元组，range, buffer对象
#序列的通用操作：索引 分片 加法 乘法 成员资格 长度 最值

# 1)索引 序列中的元素可以通过索引访问
# seq1 = 'abc'
# seq2 = (1,2,3)
# seq3 = ['a','b','c']
# print(seq1[0])
# print(seq2[0])
# print(seq3[0])

# 至于序列中的元素是否可以通过索引修改 则取决于序列是否可变
# 字符串与元组是不可变的
# seq1[0] = 'A' #TypeError: 'str' object does not support item assignment
# seq2[0] = '4' #TypeError: 'tuple' object does not support item assignment
# seq3[0] = 10
# print(seq3)

# 2)分片 分片操作序列中一段连续的元素或者说是子序列
# seq = [1,2,3,4,5]
# 分片操作至少需要提供两个参数：起始索引(包含) 结束索引(不包含)
# print(seq[1:3]) #[2,3]
# print(seq[1:len(seq)]) #[2, 3, 4, 5]
# 如果省略结束索引 则默认为末尾
# print(seq[1:]) #等同于seq[1:len(seq)]
# 如果省略起始索引则默认为0
# print(seq[0:3]) #[1, 2, 3]
# 同时省略 则会返回序列的复本
# seq_copy = seq[:]
# print(seq_copy) #[1, 2, 3, 4, 5]
# seq_copy[0] = 10
# print(seq_copy) #[10, 2, 3, 4, 5]
# print(seq) #[1, 2, 3, 4, 5]
#索引可以为负数 -1索引倒数第一个 以此类推
# print(seq[-3:-1]) #[3, 4]
# print(seq[-3:]) #[3, 4, 5]
# print(seq[0:1]) #[1]
# 如果起始索引指向的位置不在结束索引的左边则返回空序列
# print(seq[0:0]) #[]
# print(seq[1:0]) #[]
#指定分片的步长(python2.3+) 默认分片的步长为1
# print(seq[::2]) #[1, 3, 5]
# 步长可以为负数 此时起始索引指向的位置必须在结束索引的右边 否则返回空序列
# print(seq[::-1]) #[5, 4, 3, 2, 1]
# print(seq[-1:-3:-1]) #[5, 4]

# 3)加 使用+可以将两个同类型的序列连接为一个序列
# seq1 = [1,2,3]
# seq2 = [3,4,5]
# print(seq1+seq2) #[1, 2, 3, 3, 4, 5]

# 4)乘法 用一个正整数n乘以一个序列会生成一个将当前序列重复n次的序列
# seq1 = 'abc'
# seq2 = (1,2,3)
# seq3 = [1,3,5]
# print(seq1*3)
# print(seq2*3)
# print(seq3*3)
# 利用乘法可以方便初始化指定长度的序列
# 例如生成一个长度为10的序列 默认值均为0
# seq = [0]*10
# print(seq)
# 如果想表示一个指定长度的列表中还没有任何值 可以用None填充 
# None是python中一个特殊的内建值 表示什么也没有
# seq = [None]*10
# print(seq)

# 5)成员资格 检查序列是否包含指定的元素 返回bool值
# 使用 element in sequence 这样的语法可以检查指定的元素是否则序列中
# print(1 in [1,2,3]) #True
# print(10 in [1,2,3]) #False
# 字符串序列的成员是字符 所有可以检查某个字符是否在字符串中
# print('a' in 'abc')
# 为了方便 自python2.3起可以检查字符串是否在字符串中
# print('ab' in 'abc')

# 6)len min max
# seq1 = 'aAdb'
# seq2 = (1,2,23,0)
# seq3 = [13,11,22]
# print(seq1,len(seq1),min(seq1),max(seq1))
# print(seq2,len(seq2),min(seq2),max(seq2))
# print(seq3,len(seq3),min(seq3),max(seq3))

# 7)s.index(x[, i[, j]]) 指定元素第一次出现的索引
# seq = 'abca'
# print(seq.index('a')) #0
# 如果元素不存在会报异常
# print(seq.index('x')) #ValueError: substring not found

# 8)s.count(x) 返回指定元素在序列中出现的次数
# print('abca'.count('a')) #2
# print('abca'.count('x')) #0

# 列表 list
# 列表也是一种序列 它不同于字符串与元组 它是可变的
# 列表对象是list类的实例
# 可以将任何序列传递给list来构造列表
# L = list('abc')
# L2 = list((1,2,3))
# print(L)
# print(L2)
# 列表直接量是写在中括号中并有逗号分隔元素
# L = [1,2,3]
# print(L)
# 两个列表变量赋值 会使它们指向同一个列表
# t = [1,2,3]
# t2 = t #t2与t指向同一个列表
# t2[0] = 100 
# print(t) #[100, 2, 3]
# print(t2) #[100, 2, 3]
# 列表操作
# L = [1,2,3]
# 1)通过索引修改元素
# L[0] = 11
# print(L) #[11, 2, 3]
# 索引不能超出范围
# L[len(L)] = 4 #IndexError: list assignment index out of range
# L[100] = 1000 
# 2)删除列表元素
# del L[0]
# print(L) #[2, 3]
# 3)分片赋值 这是一个很强大的特性 可以实现元素的插入，删除，修改
# L[1:] = [4,5]
# print(L) #[1, 4, 5]
#也可以使用于原分片不等长的列表来赋值
# L[1:] = [7,8,9,10]
# print(L) #[1, 7, 8, 9, 10]
#通过给长度为1的分片赋值来修改某个元素
# L[1:2] = [4] 
# print(L) #[1, 2, 3]
# 通过给一个空的分片赋值来插入元素
# L[1:1] = [8,9,10]
# print(L) #[1, 8, 9, 10, 2, 3]
# 尾部插入
# L[len(L):] = [4]
# print(L) #[1, 2, 3, 4]
# 将一个分片赋值为空列表 可以删除元素
# L[1:] = []
# print(L) #
# 也可使用del语句来删除分片
# del L[1:]
# print(L) #[1]
# 结合步长可以更灵活地进行分片赋值
# L[-2:] = [5,6]
# print(L) #[1, 5, 6]
# L[::2] = [8,9]
# print(L) #[8, 2, 9]
# del L[::2]
# print(L) #[2]
# 可变序列的通用操作 由于list是可变序列 所以也适用于列表
# L = [1,2,3,4,5]
# 1)分片赋值 这个已经讲过了
# 2)append 追加元素
# L.append(6)
# print(L) #[1, 2, 3, 4, 5, 6]
# 3)*= 重复列表中的元素
# L *= 2
# print(L) #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# 4)insert 在指定索引出插入元素
# L.insert(0,11)
# print(L) #[11, 1, 2, 3, 4, 5]
# L.insert(len(L),6) #相当于L.append(6)
# print(L) #[1, 2, 3, 4, 5, 6]
# 5)pop 删除指定索引处的元素 并返回 默认删除最后一个
# e = L.pop(1)
# print(e) #2
# print(L) #[1, 3, 4, 5]
# 6)remove 删除第一次出现的指定元素
# L.remove(5)
# print(L)
# 如果删除的元素不存在则会报错
# L.remove(6) #ValueError: list.remove(x): x not in list
# print(L)
# 7)reverse 原地反转列表
# L.reverse()
# print(L) #[5, 4, 3, 2, 1]
# 8)clear 清空列表
# L.clear()
# print(L) #[]
# 9)extend 将一个序列中的可迭代对象中的元素添加到末尾 也可以使用 += 完成
# L.extend('abc')
# print(L) #[1, 2, 3, 4, 5, 'a', 'b', 'c']
# 等价于
# L += 'abc'
# print(L)
# 10)copy 返回列表的一个浅拷贝
# L2 = L.copy()
# print(L2)
# print(L == L2) #True
# print(L is L2) #False

# 列表独有的方法
# 1)sort(*, key=None, reverse=False)
# L = list('baxA')
# L.sort()
# print(L) #['A', 'a', 'b', 'x']
# L.sort(key=str.lower)
# print(L) #['a', 'A', 'b', 'x']
# L.sort(reverse=True)
# print(L) #['x', 'b', 'a', 'A']

# 用列表实现栈(stack)操作
# stack = [3,4,5]
# stack.append(6)
# stack.append(7)
# print(stack)
# print(stack.pop())
# print(stack)

# 队列操作 双端队列
# from collections import deque
# queue = deque(['Jack','Rose','Tom'])
# # print(type(queue))
# # print(dir(queue))
# print(queue)
# # 入队操作
# queue.append('Linda')
# print(queue)
# # 出队操作
# print(queue.popleft())
# print(queue)
# # 查看队首元素
# print(queue[0])
# # 队列大小
# print(len(queue))

# 列表推导式
# L = list(map(lambda x: x*x,range(10)))
# print(L)
# L2 = [x*x for x in range(10)]
# print(L2)
# 在列表推导式中使用if语句
# L = [x*x for x in range(10) if x % 2 == 0]
# print(L)
# 多个for语句
# L = [(x,y) for x in [1,2,3] for y in [1,2,3] if x != y]
# print(L)

# vec = [[1,2,3], [4,5,6], [7,8,9]]
# L = [n for v in vec for n in v]
# print(L)

# from math import pi
# print(pi)
# L = [str(round(pi,i)) for i in range(9)]
# print(L)

# matrix = [
# 	[1, 2, 3, 4],
# 	[5, 6, 7, 8],
# 	[9, 10, 11, 12],
# ]
# # 嵌套的列表推导式
# # 转置矩阵
# L = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(L)
# 内置的zip函数可以巧妙地完成
# print(list(zip(*matrix)))

# 元组 
# 元组是不可变序列 所以它具有序列的通过操作
# 创建元组 逗号分隔元素 通常用圆括号括起来
# t1 = (1,2,3)
# t2 = 1,2,3
# t3 = () #空元组
# print(t1)
# print(t2)
# print(t3)
# 如果创建只包含一个元素德元组 那么为了不与表达式混淆必须后面写逗号
# t1 = (1) #等价于t1 = 1
# t2 = (1,)
# t3 = 1,
# print(t1)
# print(t2)
# print(t3)
# 元组由于是不可变的 所以不能改变元组的元素
# t = (1,[2])
# print(t)
# t[1] = [2,3] #TypeError: 'tuple' object does not support item assignment
# print(t)
# t[1].append(3)
# print(t) #(1, [2, 3])
# 元组对象所属的类型为tuple
# t = 1,
# print(isinstance(t,tuple))
# print(type(t))
# tuple函数可以把传入的序列转换为元组
# t = tuple([1,2,3])
# t2 = tuple('abc')
# t3 = (1,2,3)
# t4 = tuple(t3)
# print(t)
# print(t2)
# print(t3 is t4) #True 说明当传给tuple的参数就是元组时 则直接返回这个元组
# 既然元组的没有序列强大 那为何还要使用它呢
# 1)可作为字典的键 键必须是不可变的
# 2)许多内建函数的参数或返回值是元组

# 字典 dict
# 列表时通过下标索引值 但有时这不是很方便与直观
# 我们希望用名字来索引值 这就是映射 字典是python内建的具有映射功能的内建类型
# 创建字典
# 在大括号中键值对之间以逗号分隔，键值之间以冒号分隔
# d = {'name':'Tom','age':23}
# print(d)
# print(d['name'])

# 访问不存在的键会抛异常
# print(d['gender']) #KeyError: 'gender'

# 字典中的键应该是唯一的 如果出现重复的键 则后面的值会覆盖前面的值
# d = {"name":'Tom',"name":'Jack'}
# print(d) #{'name': 'Jack'}

# 字典的键不能是可变的 所以列表等可变的对象不能作为字典的键 这时候元组就可以派上用场 来构造复杂的键
# d = {[1,2]:'tom'} #TypeError: unhashable type: 'list'
# prnit(d)
# d = {} #空字典
# print(d)

# 列表时dict类型的实例
# print(isinstance(d,dict))
# print(type(d)) #<class 'dict'>

# 可以通过dict函数构造字典
# L = [('Tom','2384'),('Jack','2839'),('Rose','1399')]

# 通过键值对组成的序列构建字典
# d = dict(L)
# print(d)

# 通过关键字参数构建字典
# d = dict(name='Jack',age=23)
# print(d)
# d = dict(zip(['one','two','three'],[1,2,3]))
# print(d)

# 字典操作
# d = {'name':'Tom','age':23}
# len 返回字典中键值对的个数
# print(len(d))

# 通过键访问值 如果键不存在则raise a KeyError
# print(d['name'])

# 通过键修改值
# d['name'] = 'Rose'
# print(d)

# 通过键删除键值对 如果键不存在则raise a KeyError
# del d['name']
# print(d)

# 检测键是否则字典中
# print('name' in d)
# print('gender' in d)

# 检测键是否不在字典中
# print('name' not in ds

# 清空字典
# d.clear()
# print(d)

# 返回字典的浅拷贝
# d2 = d.copy()
# print(d2)

# 创建一个字典 键由序列给出 默认值都为None或给定的默认值
# classmethod fromkeys(seq[, value])
# d = dict.fromkeys('abc')
# print(d)
# d = dict.fromkeys('abc',1)
# print(d)

# 返回字典中键对应的值 如果存在则返回默认值 默认值默认为None
# get(key[, default])
# Return the value for key if key is in the dictionary, else default. 
# If default is not given, it defaults to None, so that this method never raises a KeyError.
# d = {'name':'Jack','age':23}
# print(d.get('name'))
# print(d.get('gender'))
# print(d.get('score',100))

# 返回字典中键值对的视图
# items()
# Return a new view of the dictionary’s items ((key, value) pairs)
# 通常由于遍历字典
# for k, v in dict(name='Jack',age=23).items():
# 	print(k,v)

# 返回字典中键的视图
# keys()
# Return a new view of the dictionary’s keys
# for k in {'a':1,'b':2}.keys():
# 	print(k)
#直接遍历字典 遍历的也是键
# for k in {'a':1,'b':2}:
	# print(k)

# 返回值的视图
# values()
# Return a new view of the dictionary’s values
# for v in d.values():
# 	print(v)

# 移除并返回字典中键对应的值 如果键不存在但给出的默认值则返回默认值 如果没有默认值则raise a KeyError
# pop(key[, default])
# d = {'name':'tom','age':23}
# print(d.pop('name'))
# print(d)
# print(d.pop('gender','男'))
# print(d)
# print(d.pop('gender'))

# 随机移除并返回键值对怎成的元组
# popitem()
# Remove and return an arbitrary (key, value) pair from the dictionary
# print(d.popitem())
# print(d)

# 如果键在字典中则返回对应的值 如果不在则插入键值对并返回值
# setdefault(key[, default])
# If key is in the dictionary, return its value. 
# If not, insert key with a value of default and return default. default defaults to None.
# print(d.setdefault('name'))
# print(d.setdefault('gender'))
# print(d.setdefault('score',100))

# 用另外一个字典更新当前字典
# update([other])
# Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None
# d = {'host':'localhost','port':3306,'user':'root','password':''}
# d2 = {'port':8000,'password':'root123'}
# d.update(d2)
# print(d)
# d.update([('port',8000),('password','root123')])
# print(d)

# 字典的拷贝
# d = {'name':'Tom','age':23,'fruits':['apple','banana','orange']}
# 浅拷贝
# d2 = d.copy() 
# 深拷贝
# from copy import deepcopy
# d2 = deepcopy(d)
# d2['name'] = 'Jack'
# d2['fruits'].remove('apple')
# print(d) 
# print(d2) 

# 字典推导式
# d = {x:x*x for x in range(1,10)}
# print(d)

# 集合 set 不包含重复元素
# 创建集合 通过set函数 set函数接受一个序列
# s = set('abcacc')
# print(s) #{'b', 'c', 'a'}
# print(type(s)) #<class 'set'>

# 集合字面量 有逗号分隔 用花括号括起来
# s = {'apple','orange','apple','banana'}
# print(s) #{'apple', 'orange', 'banana'}

# 创建空集合 不能使用{} 它是一个空字典 此时必须使用set()
# s = set()
# print(s)

# s1 = {'a','b','c','d'}
# s2 = {'c','d','e','f'}
# 并集
# print(s1|s2) #{'a', 'c', 'e', 'b', 'd', 'f'}
# print(s1.union(s2))
# 差集
# print(s1 - s2) #{'a', 'b'}
# print(s1.difference(s2))
# 交集
# print(s1&s2) #{'c', 'd'}
# print(s1.intersection(s2))
# 对称差
# print(s1^s2) #{'b', 'a', 'e', 'f'}
# print(s1.symmetric_difference(s2))
# 添加元素
# s1.add(1)
# print(s1)
# 集合通常不能包含集合
# s1.add(s2) #TypeError: unhashable type: 'set'
# s1.add(frozenset(s2))
# print(s1)
# 移除元素
# s1.remove('a')
# print(s1)

# 集合推导式
# s = {c for c in 'akdfabadfkl'}
# print(s) #{'a', 'k', 'd', 'b', 'f', 'l'}



# 全面地掌握print函数
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# print(1,2,3,sep=',')
# print(1,2,3,end=';')

# 常用遍历技术
# 遍历字典
# dic = {'name':'Tom','age':23,'gender':'male'}
# for k, v in dic.items():
# 	print(k,'=',v)

# 同时遍历序列的索引和值
# for i, v in enumerate(['da','ama','mida','hoff']):
# 	print(i,v)

# 同时遍历多个序列
# questions = ('name','gender','age')
# answers = ['Tom','male',23]
# for q, a in zip(questions,answers):
# 	print("What's your {0}? It is {1}".format(q,a))

# 反向迭代序列
# seq = ['tom','jack','rose']
# print(seq)
# for n in reversed(seq):
# 	print(n)

# 按排序顺序遍历
# fruits = ['banana','apple','pear','mango','orange']
# for f in sorted(fruits):
# 	print(f)

# 两个相同类型的序列可以比较
# print('abc' < 'A') #False
# print('abc' < 'abcd') #True
# print([111,22,3] < [3,4,5]) #False
# print((1,2,3) == (1.0,2.0,3.0)) #True

# 赋值魔法
# 多个值一次性赋给多个变量 这叫做序列解包(sequence unpacking)
# a,b,c = 1,2,3
# print(a,b,c)
# 只要右边是一个序列就可以
# a,b = [1,2]
# print(a)
# print(b)
# 可以利用序列解包交换两个变量的值
# a,b = 1,2
# a,b = b,a
# print(a,b)
#将多余的值打包到一个列表后赋给最后一个变量
# a,b,*c = 1,2,3,4,5
# print(a,b,c,sep=",") #1,2,[3, 4, 5]

# 布尔类型 bool
# 下面的值被解释为False
# 0  0.0 空字符串 空的列表，元组，字典 None
# bool可以将任何传入的值转换为真值 其它都为True
# 所以在python中任何都可以作为真值 设置不需要用bool函数转换
# print(bool(0))
# print(bool(0.0))
# print(bool(''))
# print(bool([]))
# print(bool(()))
# print(bool({}))
# print(bool(None))

# print(True==1)
# print(True+True)
# print(False+1)

# 比较运算符的连写
# 在许多语言中如果 直接写1<2<3这样的包含多个比较运算符的表达式会出错
# 但python可以
# print(1<2<3) #True

# 控制语句
# age = int(input('Enter you age: '))
# if age >= 18:
# 	print('成年人')
# else:
# 	print('未成年')

# elif 是 else if的缩写
# num = int(input('Enter an integer: '))
# if num > 0:
# 	print('positive')
# elif num < 0:
# 	print('negative')
# else:
# 	print('zero')

# 比较运算符
# 比较运算符中需要特别关注的是 == ，!= 与 is，is not的区别
# ==用来比较两个对象的值是否相等
# is要来比较两个变量是否指向同一个对象
# a = b = [1,2,3]
# c = [1,2,3]
# print(a==b) #True
# print(a is b) #True
# print(a is c) #False
# 注意不要讲is用于数值，字符串等不可变对象
# in，not in 也算比较运算符 x in y 判断x是否为容器y的元素

# 布尔运算符 and or not
# print(True and False)
# print(True or False)
# print(not False)
# 短路逻辑
# x and y 如果x为假则返回x的值 如果x为真则返回y的值
# print(4 and 3) #3
# print(0 and 1) #0
# x or y 如果x为真则返回x的值 否则返回y的值
# name = input('you name: ') or 'xxx'
# print('Hello',name)

# 断言
# 如果想确保某个条件必须为真 在为假是让程序报错 则可以使用断言
# age = int(input('Enter your age: '))
# 条件为假是会raise a AssertionError
# assert 1 <= age <= 100
# 断言后面可以写解释断言的字符串
# assert 1 <= age <= 100; 'age must between 1 and 100'
# print(age)

# 循环

# while 循环
# name = ''
# while name.strip() == '':
# 	name = input('Enter your name: ')
# print('Hello',name)

# for 循环
# python中的for循环专门用来迭代可迭代对象

# for s in 'abc':
# 	print(s)

# for n in [1,2,3]:
# 	print(n)

# for n in (1,2,3):
# 	print(n)

# for k in dict(name='Tom',age=23):
# 	print(k)

# 有时候迭代一个范围内的数字是很常见的操作
# 内置的range函数返回一个指定范围内的数字的迭代器 python2.3以前返回的是列表
# range返回迭代器的好处是 在真正需要值是才会计算值 可节省内存

# for i in range(5): #[0,5)范围的整数
# 	print(i)

# for i in range(1,5): #[1,5)
# 	print(i)

# for i in range(0,11,2): #[0,10]之间的偶数
# 	print(i)

# 并行遍历多个序列
# seq1 = (1,2,3)
# seq2 = ['one','two','three']
# # print(list(zip(seq1,seq2)))
# for a,b in zip(seq1,seq2):
# 	print(a,'=',b)

# 如果需要在遍历序列元素是同时获得索引
# seq = 'abcdef'
# for index,value in zip(range(len(seq)), seq):
# 	print(index,value)
# 内置的enumerate可方便地实现上面的需求
# seq = 'python'
# for i,v in enumerate(seq):
# 	print(i,v)

# 可在循环后面添加一个else语句 当循环正常结束时会执行这个else语句 如果循环是由break退出则不会执行
# 例如寻找100以内的质数
# for n in range(2,101):
# 	for k in range(2,n):
# 		if n % k == 0:
# 			break
# 		k += 1
# 	else:
# 		print(n,end=',')

# 可迭代对象都可以通过for循环遍历 那么如何判断一个对象是否为可迭代的呢
# from collections import Iterable
# print(isinstance('abc',Iterable))
# print(isinstance((),Iterable))
# print(isinstance([1],Iterable))
# print(isinstance({},Iterable))
# print(isinstance(range(2),Iterable))

# 通过关键字方式给函数传参 而不必考虑顺序
# def f(a,b):
# 	print(a,b)
# f(1,2)
# f(a=2,b=1)

# 函数参数的默认值是在定义函数时计算的
# i = 1
# def f(arg=i):
# 	print(arg)
# i = 2
# f() #1

# 当函数参数的默认值为可变对象时 需要注意下面的现象
# def f(a, L=[]):
# 	L.append(a)
# 	return L
# print(f(1))	#[1]
# print(f(2))	#[1, 2]
# print(f(3))	#[1, 2, 3]

# 如果不想在多次调用函数时共享参数默认值 可以如下定义
# def f(a, L=None):
# 	if L is None:
# 		L = []
# 	L.append(a)
# 	return L
# print(f(1)) #[1]
# print(f(2)) #[2]
# print(f(3)) #[3]

 # Function Annotations 函数注解
# def f(ham: str, eggs: str = 'eggs') :
# 	print("Annotations:", f.__annotations__)
# 	print("Arguments:", ham, eggs)
# 	return ham + ' and ' + eggs
# print(f('spam'))

# def f(ham: str, eggs: str = 'eggs') -> str:
# 	print("Annotations:", f.__annotations__)
# 	print("Arguments:", ham, eggs)
# 	return ham + ' and ' + eggs
# print(f('spam'))

# 列表推导式 

# 生成1~10的平方构成的列表
# L = [x*x for x in range(1,11)]
# print(L) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 可以增加if语句对元素进行过滤
# 生成[1,10]中能被3整除的数的平方
# L = [x*x for x in range(1,11) if x % 3 == 0]
# print(L) #[9, 36, 81]

# 可以有多for语句
# L = [(x, y) for x in range(3) for y in range(3)] 
# print(L) #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 作为对比 下面的循环生成与上面相同的列表
# L = []
# for x in range(3):
# 	for y in range(3):
# 		L.append((x, y))
# print(L)

# pass语句 是空语句 用于做占位符
# 例如当函数体尚未实现时可以先写为
# def f():
# 	pass
# 还未实现的类
# class A():
# 	pass

# del 删除
# 在前面已经看到del可以删除字典或列表中的元素
# del可以删除变量
# x = 1
# print(x)
# del x 
# #此时已不存在变量x
# print(x)  #NameError: name 'x' is not defined

# del 只能删除对象的引用 无法删除对象本身
# x = [1,2,3]
# y = x
# y[0] = 'a'
# print(x)
# del x #只是删除了对列表的一个引用
# print(y)

# exec 内置函数exec可以执行一段python代码
# exec(object[, globals[, locals]])

# pcs = 'print("Hello python")'
# exec(pcs)

# 使用简单形式的exec 可能存在风险 它可以污染命名空间
# from math import sqrt
# print(sqrt(9))
# exec('sqrt = 1') #改变了sqrt
# print(sqrt(9)) #TypeError: 'int' object is not callable

# 为了避免上面的问题 可以提供一个字典作为命名空间
# from math import sqrt
# print(sqrt(9))
# NS = {}
# exec('sqrt = 1', NS)
# print(sqrt(9)) 
# print(NS['sqrt']) #1

# eval 计算python表达式并返回结果
# eval(expression, globals=None, locals=None)
# NS = {
# 	'a' : 6174,
# 	'b' : 2,
# }
# print(eval('a**b',NS)) #38118276

# 函数 函数是一段代码的封装

# def fibs(n):
# 	L = []
# 	a,b = 1,1
# 	while n > 0:
# 		L.append(a)
# 		a,b = b,a+b
# 		n -= 1
# 	return L
# count = int(input('How many fibonacci numbers do you want?\n'))
# f1 = fibs(count)
# print(f1)

# 内建的callable函数可以判断一个对象是否可调用
# def add(a,b):
# 	return a+b
# print(callable(add))
# 类都是可调用的
# print(callable(str))

# docstring 函数文档字符串
# 写在函数体开头的字符串 会作为函数的文档存储 可以通过函数的__doc__属性访问
# def square(x):
# 	'''Calculate the square of the number x
# 	'''
# 	return x*x
# print(square.__doc__)
# help(square)

# python中的任何函数都是由返回值的
# 如果return语句后面没有值或者没有return语句则返回None 类似于js中返回undefined
# def f(a):
# 	if a > 0:
# 		return
# print(f(1)) #None
# print(f(0)) #None

# 函数参数采用值传递
# def f(name):
# 	name = 'Rose'
# 	print(name)
# name = 'Jack'
# f(name) #Rose
# print(name) #Jack

# 可变数据作为参数传递时 传递的是引用 所有可以通过引用改变指向的数据
# L = [1,2,3]
# def f(a):
# 	print(id(a))
# 	a.append(100)
# f(L)
# # id函数返回对象的唯一标识 可理解为地址 
# print(id(L)) #与函数中打印的值相同 说明引用的是同一对象
# print(L)

# 存取名字的小程序 start
# db = {}
# def init(db):
# 	db['first'] = {}
# 	db['middle'] = {}
# 	db['last'] = {}
# def lookup(db, label, name):
# 	return db[label].get(name, [])
# def save(db, full_name):
# 	names = full_name.split()
# 	if len(names) == 2:
# 		names.insert(1, '')
# 	labels = 'first', 'middle', 'last'
# 	for label, name in zip(labels, names):
# 		db[label].setdefault(name, []).append(full_name)
# def delete(db, full_name):
# 	names = full_name.split()
# 	if len(names) == 2:
# 		names.insert(1, '')
# 	labels = 'first', 'middle', 'last'
# 	for label, name in zip(labels, names):
# 		L = db[label].get(name, None)
# 		if L:
# 			while full_name in L:
# 				L.remove(full_name)

# init(db)
# print(lookup(db, 'middle', 'Lie'))
# save(db, 'Jack Lie Bob')
# save(db, 'Jack Red Mike')
# save(db, 'Rose Lie Smith')
# save(db, 'Tim Green Smith')
# print(lookup(db, 'first', 'Jack'))
# print(lookup(db, 'first', 'Jackson'))
# print(lookup(db, 'middle', 'Lie'))
# print(lookup(db, 'middle', 'Liee'))
# print(lookup(db, 'last', 'Smith'))
# print(lookup(db, 'last', 'Smitheen'))
# print(db)
# delete(db, 'Jack Lie Bob')
# print(db)
# 存取名字的小程序 end

# 可以忘记函数的参数
# def greet(greeting, name,):
# 	print(greeting, name)
# greet('Hello','Tom')
# # 通过关键字传递参数
# greet(greeting='cheer up!', name='Jack',)
# greet(name='Jack', greeting='cheer up!',)
# greet('Great', name = 'Adam')
# # 关键字参数不能为与位置参数之前
# greet(name = 'Adam', 'Great',) #SyntaxError: positional argument follows keyword argument

# 关键字参数最厉害的地方在于可以给参数提供默认值
# def greet(greeting='Hello', name='world',):
# 	print(greeting, name,)
# greet()
# greet('Good bye')
# greet(name='Tom')
# greet('wonderful','universe')

# # 混合使用位置参数与关键字参数
# def greet(name, greeting='Hello', punctuation='!'):
# 	print(greeting, name+punctuation)

# greet('Tom')
# greet(name='Jack')
# greet('Rose', 'Hi', '!!')
# greet('Linda', greeting='Bye',)
# greet('Linda', punctuation='...',)
# greet(greeting='Hi', name='Snow')

# 非关键字可变长参数
# def pnt(*params): #将所有的参数收集到元组中
# 	print(params)
# 	print(*params) #这里的*表示将元组拆开
# pnt()
# pnt('a')
# pnt('a','b')
# # 此时不能使用关键字参数
# pnt(name='Tom') #TypeError: pnt() got an unexpected keyword argument 'name'

# def add(*nums):
# 	return sum(nums)
# print(add(1,2,3))

# 关键字可变长参数
# def f(**kws): #会将所有的关键字参数收集到一个字典中
# 	print(kws)
# f()
# f(name='Tom')
# f(name='Tom',age=23)
# f(1) #TypeError: f() takes 0 positional arguments but 1 was given

# 联合使用可变长非关键字参数与可变长关键字参数
# def f(*args, **kws):
# 	print(args)
# 	print(kws)
# 	print('='*30)
# f()
# f(1)
# f(name='Jack')
# f(1,name='Rose')

# def f(a,b,*c):
# 	print(a)
# 	print(b)
# 	print(c)
# 	print('='*30)
# f(1,2)
# f(a=2,b=1)
# f(1,2,3,4)
# f(a=1,b=2,3,4) #SyntaxError: positional argument follows keyword argument

# def f(a,b,**c):
# 	print(a)
# 	print(b)
# 	print(c)
# 	print('='*30)
# f(1,2)
# f(a=2,b=1)
# f(1,2,c=3,d=4)
# f(a=2,b=1,c=3,d=4)

# def f(a,b,c=3,*d):
# 	print(a)
# 	print(b)
# 	print(c)
# 	print(d)
# 	print('='*30)
# f(1,2)
# f(1,2,33)
# f(a=2,b=1)
# # f(a=2,b=1,33) #SyntaxError: positional argument follows keyword argument
# f(1,2,33,4)

# def f(a,b,c=3,*d,**e):
# 	print(a)
# 	print(b)
# 	print(c)
# 	print(d)
# 	print(e)
# 	print('='*30)
# f(1,2)
# f(1,2,33)
# f(1,2,33,4,5)
# f(1,2,33,4,5,name='Tom')

# 作用域
# 变量可以看做是对值的引用 类似字典的键引用值
# x = 1
# 内建的vars函数可以返回对象的__dict__属性
# scope = vars()
# 不带参数的vars等同于locals()
# scope = locals()
# print(scope)
# print(scope['x'])

# 函数会创建一个自己的作用域 所以函数的参数及函数体中的变量不会影响全局作用域中的变量
# x = 1
# def f(x):
# 	x =2
# f(x)
# print(x) #1

# x = 1
# # 但函数在自己的作用域中找不到访问的变量时 会到父级作用域中查找
# def f():
# 	print(x)
# f() #1

# x = 1
# def f():
# 	global x
# 	print(x)
# 	x = 2 
# f()
# print(x)

# 访问同名的全局变量
# x = 1
# def f(x):
# 	print(x,globals()['x'])
# f(0)

# 循环计算阶乘
# def my_factorial(n):
# 	result = 1
# 	for i in range(2,n+1):
# 		result *= i
# 	return result

# for i in range(0,10):
# 	print('{:d}!={:d}'.format(i,my_factorial(i)))

# 递归计算阶乘
# def my_cur_factorial(n):
# 	if n == 0:
# 		return 1
# 	else:
# 		return n * my_cur_factorial(n-1)

# for i in range(0,10):
# 	print('{:d}!={:d}'.format(i,my_cur_factorial(i)))

# 循环计算幂
# def my_pow(x,n):
# 	r = x
# 	for i in range(1,n):
# 		r *= x
# 	return r

# for i in range(2,10):
# 	print('{:d} -> {:d}'.format(i,my_pow(i,i)))

# # 递归计算幂
# def my_cur_pow(x,n):
# 	if n == 0:
# 		return 1
# 	else:
# 		return x*my_cur_pow(x,n-1)

# for i in range(2,10):
# 	print('{:d} -> {:d}'.format(i,my_cur_pow(i,i)))


# 二分查找
# def binSearch(seq,value,start=0,end=None):
# 	if end is None:
# 		end = len(seq)-1
# 	while start <= end:
# 		middle = (start+end)//2
# 		v = seq[middle]
# 		if v == value:
# 			return middle
# 		if v > value:
# 			end = middle-1
# 		else:
# 			start = middle+1
# 	return -1

# L = [1,2,3,4,5,6]
# print(binSearch(L,100))

# from collections import Iterable,Iterator
# def f(n):
# 	return n*n
# r = map(f,[1,2,3])
# print(isinstance(r,Iterable)) #True
# print(isinstance(r,Iterator)) #True
# print(list(r))

# L = list(range(1,11))
# def f(n):
# 	return n % 2 == 0
# # r = filter(f,L) #只留下偶数
# r = filter(lambda n:n % 2 == 0,L) #使用lambda创建匿名函数
# print(r)
# print(list(r))

# 多态体验
# import random
# x = random.choice(['abc',['a','b','a','c']])
# # 不论x是字符串还是列表 只要有count方法就可以刻
# print(x.count('a'))

# 类
# class Person(object):

# 	def setName(self,name):
# 		self.name = name

# 	def getName(self):
# 		return self.name

# 	def greet(self):
# 		print("Hello,I'm {}".format(self.name))

# p1 = Person()
# p1.setName('Tom')
# print(p1.getName())
# p1.greet()
# 可以给对象添加属性
# p1.age = 18
# print(p1.age)
# 可以通过类调用方法 此时必须显示的传入对象
# Person.greet(p1)
# f = p1.greet
# f() #有self参数
# f = Person.greet
# f() #TypeError: greet() missing 1 required positional argument: 'self'

# Python并不直接支持私有化 但可以利用一些小技巧
# 在属性或方法的前面加上两个下划线 这样在类外就不能直接访问了
# 实际上还是可以访问的 只是python把它们的名字改成了加上_类名原名
# class Person(object):

# 	def setName(self,name):
# 		self.__name = name

# 	def getName(self):
# 		return self.__name

# 	def greet(self):
# 		print("Hello,I'm {}".format(self.__name))

# 	def __hello(self):
# 		print('private hello method')


# p = Person()
# p.setName('Tom')
# print(dir(p))
# print(p.getName()) #Tom
# print(p.name) #AttributeError: 'Person' object has no attribute 'name'
# print(p._Person__name) #Tom
# p.hello() #AttributeError: 'Person' object has no attribute 'hello'
# p._Person__hello()



# 定义类实际上就是执行类的代码块
# 所以类中可以放置普通的语句
# class Person(object):
# 	print('Defining class Person')
# 	numbers = 0

# 	def init(self):
# 		Person.numbers += 1

# print(Person.numbers)
# p1 = Person()
# p1.init()
# print(Person.numbers)
# p2 = Person()
# p2.init()
# print(Person.numbers)
# # 通过对象可以访问到类的属性 假定当前对象没有同名的实例属性
# print(p2.numbers)
# #此时p2拥有自己的number2属性
# p2.numbers = 100
# print(Person.numbers) #2
# print(p2.numbers) #100

# 继承
# class Animal(object):
# 	def eat(self):
# 		print('Animal is eating')

# class Bird(Animal):
# 	def eat(self):
# 		print('Bird is eating')

# print(dir(Animal))
# print(dir(Bird))

# print(issubclass(Bird,Animal)) #True
# print(Bird.__bases__) #基类组成的元组

# a = Animal()
# b = Bird()
# a.eat()
# b.eat()
# print(isinstance(b,Bird))
# print(isinstance(b,Animal)) #True

# python支持多继承
# class Calculator(object):
# 	def calc(self):
# 		print('calc')
# 	def f(self):
# 		print("f in Calculator")

# class Talker(object):
# 	def talk(self):
# 		print('talk')
# 	def f(self):
# 		print("f in Talker")

# class TalkingCalculator(Talker,Calculator):
# 	pass

# print(TalkingCalculator.__bases__)
# tc = TalkingCalculator()
# tc.calc()
# tc.talk()
# tc.f()

# hasattr 检查对象是否具有某个属性
# print(hasattr(tc,'talk'))
#getattr获取对象的某个属性
# 检查是否具有某个指定的方法
# print(callable(getattr(tc,'talk')))
# print(dir(tc))

# 看看一个除零异常
# print(1/0) #ZeroDivisionError: division by zero

# 所有异常类的根类是Exception
# raise 语句引发异常
# raise Exception #会自动创建一个Exception类的实例
# 提供出错信息
# raise Exception('xxx')

# 自定义异常
# class AgeException(Exception):
# 	pass

# age = 150
# if age < 1 or age > 120:
# 	raise AgeException('Invalid age')

# a = float(input('Enter first number: '))
# b = float(input('Enter second number: '))
# try:
# 	c = a / b
# 	print('{:f}/{:f}={:f}'.format(a,b,c))
# except ZeroDivisionError:
# 	print('除数不能为0')

# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# # 注意先写子类异常 再写父类异常
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
        # print("B")

# 无参数的raise语句 将异常继续上抛
# def f():
# 	try:
# 		a = 1/0
# 	except ZeroDivisionError:
# 		print('除数不能为0')
# 		raise
# 	print('f end')
# f()

# 多个except
# a = 1
# b = '2'
# try:
# 	c = a / b
# 	print('{:f}/{:f}={:f}'.format(a,b,c))
# except ZeroDivisionError:
# 	print('除数不能为0')
# except TypeError:
# 	print('不合法的类型')


# 一个except 捕获多个异常
# a = 1
# b = 0
# b = '2'
# try:
# 	c = a / b
# 	print('{:f}/{:f}={:f}'.format(a,b,c))
# except (ZeroDivisionError,TypeError):
# 	print('出错了')

# 获取异常对象
# a = 1
# b = 0
# b = '2'
# try:
# 	c = a / b
# 	print('{:f}/{:f}={:f}'.format(a,b,c))
# except (ZeroDivisionError,TypeError) as e:
# 	print(e)

# 真正的全捕获
# a = 1
# b = 0
# b = '2'
# try:
# 	c = a / b
# 	print('{:f}/{:f}={:f}'.format(a,b,c))
# except:
# 	print('出错了')

# 给except配个else
# 当没有异常发生时执行else
# try:
# 	a = 1/0
# except Exception as e:
# 	print(e)
# else:
# 	print('ok')

# finally 总会执行
# try:
# 	a = 1/2
# finally:
# 	print('finally')

# 组合使用
# try:
# 	a = 1/0
# except:
# 	print('error')
# finally:
# 	print('finally')

# try的else字句
# import sys
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# 获取异常对象及参数
# try:
# 	raise Exception('spam', 'eggs')
# except Exception as inst:
# 	print(type(inst))    # the exception instance
# 	print(inst.args)     # arguments stored in .args
# 	print(inst)          # __str__ allows args to be printed directly,                     # but may be overridden in exception subclasses
# 	x, y = inst.args     # unpack args
# 	print('x =', x)
# 	print('y =', y)
# 	inst.a = 'abc'
# 	print(inst.a)


# 魔法方法

# __init__ 构造方法
# class Person(object):
# 	def __init__(self,name):
# 		self.name = name
# 		print('调用了构造方法',name)

# p1 = Person('Tom')
# p2 = Person('Jack')
# print(p1.name)
# print(p2.name)

# 子类的初始化 子类初始化是一定要先初始化父类 否则可能没有正确地初始化
# class Person(object):
# 	def __init__(self,name):
# 		self.name = name
# 		print('调用了Person的构造方法,name={0}'.format(name))

# class Student(Person):
# 	def __init__(self,name,sid):
# 		# Person.__init__(self,name) #老式方法 缺点：硬书写父类的名字 多继承时可能会多次调用父类的构造方法
# 		super(Student,self).__init__(name)
# 		self.sid = sid
# 		print('调用了Student的构造方法,name={0},sid={1}'.format(name,sid))

# s1 = Student('Jack','2342')
# print(s1.name,s1.sid)

# 序列相关的魔术方法
# __len__(self)	如果实现了__len__方法 则可以使用len函数求对象的长度
# __setitem__(self,key,value)	通过索引或键设置时调用
# __getitem__(self,key) 通过索引或键访问时调用
# __delitem__(self,key) 通过索引或键删除时调用

# 自定义的算式序列
# def checkIndex(index):
# 	if not isinstance(index, int):
# 		raise TypeError('索引必须是整数')
# 	if index < 0:
# 		raise ValueError('索引不能为负数')

# class ArithmeticSequence(object):
# 	def __init__(self,start=0,step=1):
# 		self.start = start
# 		self.step = step
# 		self.changed = {} #用户修改的值的字典

# 	def __getitem__(self,key):
# 		checkIndex(key)
# 		if key in self.changed:
# 			return self.changed[key]
# 		else:
# 			return self.start+key*self.step

# 	def __setitem__(self,key,value):
# 		checkIndex(key)
# 		self.changed[key] = value

# seq = ArithmeticSequence()
# seq[2] = 22
# print(seq[0])
# print(seq[1])
# print(seq[2])


# 同一通过继承内置类型 并重写一些方法 来定制更适合自己的类型
# 下面是一个带有访问计数的list
# class CounterList(list):
# 	def __init__(self,*args):
# 		super(CounterList,self).__init__(*args)
# 		self.counter = 0
# 	def __getitem__(self,key):
# 		self.counter += 1
# 		return super(CounterList,self).__getitem__(key)

# clist = CounterList(range(10))
# print(clist)
# clist.pop()
# clist.pop(1)
# print(clist)
# del clist[2:4]
# a = clist[2]
# print(clist)
# print(clist.counter)

# property 属性
# class Rectange(object):
# 	def __init__(self,width=0,height=0):
# 		self._w = width
# 		self._h = height
# 	def getSize(self):
# 		return self._w,self._h
# 	def setSize(self,size):
# 		self._w,self._h = size
# 	def delSize(self):
# 		del self._w
# 		del self._h

# 	size = property(getSize,setSize,delSize,'size of the rectangle')

# rect = Rectange()
# print(rect.size)
# rect.size = (1,2)
# print(rect.size)
# del rect.size
# print(rect.size) #AttributeError: 'Rectange' object has no attribute '_w'


# @property 装饰器

# class Rectange(object):
# 	def __init__(self,width=0,height=0):
# 		self._w = width
# 		self._h = height
# 	@property
# 	def size(self):
# 		return self._w,self._h
# 	@size.setter
# 	def size(self,value):
# 		self._w,self._h = value
# 	@size.deleter
# 	def size(self):
# 		del self._w
# 		del self._h

# rect = Rectange()
# print(rect.size)
# rect.size = (1,2)
# print(rect.size)
# del rect.size
# print(rect.size) #AttributeError: 'Rectange' object has no attribute '_w'

# staticmethod,classmethod 静态方法与类方法
# class MyClass(object):
# 	@staticmethod
# 	def smeth():
# 		print('This is a static method')
# 	@classmethod
# 	def cmeth(cls):
# 		print(cls)
# 		print('This is a class method')

# obj = MyClass()
# MyClass.smeth()
# MyClass.cmeth()
# obj.smeth()
# obj.cmeth()

# __getattr__(self,name)	#访问不存在的属性是自动调用
# __setattr__(self,name,value) #设置属性时自动调用
# __delattr__(self,name) #删除属性时自动调用
# class MyClass(object):
# 	def __init__(self,a):
# 		# self.a = a #会调用__setattr__
# 		self.__dict__['a'] = a
# 	def __getattr__(self,name):
# 		print('getattr,name={0}'.format(name))
# 		return self.__dict__[name]
# 	def __setattr__(self,name,value):
# 		print('setattr,name={0},value={1}'.format(name,value))
# 		self.__dict__[name] = value
# 	def __delattr__(self,name):
# 		print('delattr,name={0}'.format(name))
# 		del self.__dict__[name]
# obj = MyClass(1)
# print(obj.a)
# obj.b = 2
# print(obj.b)
# del obj.b
# print(obj.b)

# class Rectange(object):
# 	def __init__(self,w=0,h=0):
# 		self.__dict__['w'] = w
# 		self.__dict__['h'] = h
# 	def __setattr__(self,name,value):
# 		if name == 'size':
# 			self.__dict__['w'],self.__dict__['h'] = value
# 		else:
# 			self.__dict__[name] = value
# 	def __getattr__(self,name):
# 		if name == 'size':
# 			return self.__dict__['w'],self.__dict__['h']
# 		else:
# 			return self.__dict__[name]

# rect = Rectange()
# print(rect.size)
# rect.size = 1,2
# print(rect.size)


# 可迭代对象
# __iter__(self) 实现该方法的对象是可迭代的 此方法返回迭代器实例
# 迭代器必须实现__next__ 方法以返回下一个元素 如果没有元素则应该raise StopIteration

# class FibIter(object):
# 	def __init__(self,max):
# 		self.max = max
# 		self.a = 0
# 		self.b = 1
# 	def __next__(self):
# 		self.a,self.b = self.b,self.a+self.b
# 		if self.a <= self.max:
# 			return self.a
# 		else:
# 			raise StopIteration
# class Fibs(object):
# 	def __init__(self,max):
# 		self.max = max
# 	def __iter__(self):
# 		return FibIter(self.max)

# fib = Fibs(1000)
# for f in fib:
# 	print(f)

# 内置的iter用于返回对象的迭代器
# it = iter(fib)
# while True:
# 	try:
# 		f = next(it) #内置函数next返回迭代器的下一个元素
# 		print(f)
# 	except StopIteration:
# 		break

# 生成器 有yield语句的函数 它实际上是一个可以暂停执行的函数
# def fib(max):
# 	a, b = 0, 1
# 	while True:
# 		a,b = b,a+b
# 		if a > max:
# 			break
# 		else:
# 			yield a

# for f in fib(100):
# 	print(f)

# 递归生成器
# 展开嵌套列表的生成器
# def flattern(nested):
# 	for sublist in nested:
# 		if isinstance(sublist,str):
# 			yield sublist
# 		else:
# 			try:
# 				for e in flattern(sublist):
# 					yield e
# 			except:
# 				yield sublist

# for e in flattern(['abc',2,3,[4,5],[[6,7],8]]):
# 	print(e)

# 注意生成器函数与生成器迭代器的区别
# print(flattern) #<function flattern at 0x00000000003E3E18>
# print(flattern([])) #<generator object flattern at 0x00000000021EB200>

# 生成器的send方法
# def consumer():
# 	print('Consumer')
# 	s = ''
# 	while True:
# 		r = yield s
# 		if r:
# 			print('Consuming {0}'.format(r))
# 			s = '200 OK'
# 		else:
# 			s = 'not ok'

# def produce(c):
# 	r = c.send(None)
# 	print(r)
# 	n = 0
# 	while n < 5:
# 		n += 1
# 		print('Producing {0}'.format(n))
# 		r = c.send(n)
# 		print('Producer receives {0}'.format(r))
# 	c.close()
# c = consumer()
# produce(c)

# 我的八皇后问题解决方案
# def check(board,row,col,level):
# 	for i in range(row+1):
# 		for j in range(level):
# 			if i < row or j < col:
# 				if board[i][j] ==1 and (i == row or j == col or abs(i-row) == abs(j-col)):
# 					return False
# 	return True
# def isAllQueuePresent(board):
# 	count = 0
# 	for row in board:
# 		count += row.count(1)
# 	return count == len(board)

# def queue(board,row=0,col=0):
# 	for i in range(2):
# 		board[row][col] = i
# 		if i == 0 or (i == 1 and check(board,row,col,len(board))):
# 			if col < len(board)-1:
# 				queue(board,row,col+1)
# 			elif row < len(board)-1:
# 				queue(board,row+1,0)
# 			elif isAllQueuePresent(board):
# 				global count
# 				count += 1
# 				printBoard(board)
# def getBoard(level):
# 	return [[0]*level for i in range(level)]
# def printBoard(board):
# 	print(str(count)+'*'*30)
# 	for row in board:
# 		print(row)

# level = 8
# count = 0
# board = getBoard(level)
# queue(board)



# 更简洁的解决八皇后问题方案
# def conflicts(state,nextX):
# 	'''检查下一行皇后的位置与当前所有皇后是否冲突

# 	state是表示当前各行皇后水平位置的元素 
# 	例如state为(0,2)表示第一行与第二行皇后分别位于第0列与第2列
# 	'''
# 	nextY = len(state)
# 	for i in range(len(state)):
# 		x = state[i]
# 		if abs(x-nextX) in (0,nextY-i):
# 			return True
# 	return False

# def queue(num=8,state=()):
# 	for x in range(num):
# 		if not conflicts(state,x):
# 			if len(state) == num-1:
# 				yield (x,)
# 			else:
# 				for result in queue(num,state+(x,)):
# 					yield (x,)+result

# def printSolution(solution):
# 	for x in solution:
# 		print(' . '*x+' X '+' . '*(len(solution)-1-x))

# for index,solution in enumerate(queue(4)):
# 	print(str(index+1)+'*'*30)
# 	printSolution(solution)


# 模块
# 即使你用import语句重复导入一个模块 python也只会导入一次 否则会重复
# import m01
# import m01

# python内置的标准库提供了一些模块 我们可以直接导入并使用
# import math
# print(math.pi)

# python是如何知道从哪里导入模块呢？
# 首先内置模块中找 其次在当前目录找  最后在sys.path中列出路径中寻找
# import sys
# print(sys.path)
# # sys.path是一个列表 我们可以在程序执行是动态地改变 但这是一次性的 也可以配置PYTHONPATH环境变量
# sys.path.append('D:/mods')
# print(sys.path)

# 任何python文件都可以作为一个模块导入
# 如果要导入的python文件位于当前目录 则可直接导入 
# 否则需要在sys.path中指定需要导入的文件的路径
# import mymath
# print(mymath.PI)

# import sys
# sys.path.append("D:/")
# import mymath
# print(mymath.PI)

# 通过sys.argv可以获取命令函数参数
# import sys
# sys.argv是一个列表 第一个元素是python文件名
# print(sys.argv)

# 如果一个python文件被执行那么它的__name__属性值为'__main__' 如果作为模块导入则为模块名
# 可以利用这一点在模块中添加测试代码 当模块被单独执行是会允许这些测试代码 而作为模块被导入是则不会
# import m01
# m01.hello('Tom')

# pprint模块的pprint打印函数提供更加友好的输出
# import pprint,sys
# pprint.pprint(sys.path)

# 包含模块的目录成为包 如果要加一个自定义的目录作为包 则必须在目录下创建一个名为__init__.py的文件
# import pk01.m01
# print(pk01.m01.E)

# from pk01 import m01
# print(m01.E)

# 模块非常多 我们不可能完全了解每一模块
# 遇到新的模块 如何了解他里面的内容
# 使用dir函数列出模块中的成员
# import copy,pprint
# dir返回一个列表
# print(dir(copy))
# 为了去掉以双划线开头的属性 使用列表推导式过滤
# pprint.pprint([m for m in dir(copy) if m == '__all__' or not m.startswith('_')])

# __init__文件中设置的__all__变量是一个列表列出了该包下可以用*号导入的模块
# import pk01
# print(pk01.__all__)

# 如果__all__没有设置 则使用*号不会导入任何包下的模块
# from pk01 import *
# print(m01.E)
# print(m02.pwd)

# from pk01 import m02
# print(m02.pwd)

# 用help获得帮助
# import copy
# # help(copy)
# help(copy.copy)
# help(copy.copy.__doc__)

# 如果不了解一个函数的用法 那么最快的方式是查看该函数的__doc__ 即文档字符串
# print(range.__doc__)
# 当然不是所有的模块都有良好的文档字符串 
# 各种库的说明请参见 https://docs.python.org/3.6/library/index.html

# 查看源代码
# import copy
# 模块的__file__属性可返回模块文件所在的路径
# print(copy.__file__)

# time 时间模块
# import time
# print(dir(time))
# print(time.__doc__)


# time模块表示时间的两种方式
# 方式一：距Epoch的秒数
# time函数返回当前时间距Epoch的秒数 返回的是一个float类型的数字
# print(time.time())
# 不同的系统定义的Epoch可能不同 可用gmtime(0)查看
# print(time.gmtime(0))
# 方式二: 用含有9个元素的元组表示各时间分量 
# localtime将给定的距Epoch的秒数转换为本地时间元组 默认为当前时间
# print(time.localtime())
# gmtime将给定的距Epoch的秒数转换为标准时区的时间元组 默认为当前时间
# print(time.gmtime())

# 时间元组的类型为<class 'time.struct_time'>
# print(type(time.localtime())) 
# print(type(time.gmtime())) 

# 访问时间分量
# print(time.localtime())
# print(time.localtime().tm_year) #年
# print(time.localtime().tm_mon) #月
# print(time.localtime().tm_mday) #日
# print(time.localtime().tm_hour) #时
# print(time.localtime().tm_min) #分
# print(time.localtime().tm_sec) #秒
# print(time.localtime().tm_wday) #星期 0~6 0表示星期一
# print(time.localtime().tm_yday) #一年中的天数
# print(time.localtime().tm_isdst) #是否为夏令时

# time.asctime([t]) 将时间元组转换为本地时间字符串 格式为Sun Jun 20 23:21:05 1993
# 如果未提供参数 则使用localtime()的返回值
# print(time.asctime())

# time.ctime([secs]) 将距离Epoch的秒数转换为本地时间字符串 格式与asctime相同
# 默认使用time()的返回值
# print(time.ctime())

# time.mktime(t) localtime的逆操作
# print(time.time())
# print(time.mktime(time.localtime()))
# print(time.mktime((2017,8,12,0,0,0,-1,-1,-1))) #-1表示让python自己计算

# time.strftime(format[, t]) 将时间元组转换转换为指定格式的字符串
# print(time.strftime('%Y-%m-%d %H:%M:%S %p %w %A %B %z',time.localtime()))

# time.strptime(string[, format]) strftime的逆操作
# ts = '2017-08-12 09:56:23'
# t = time.strptime(ts,'%Y-%m-%d %H:%M:%S')
# print(t)

# 将时间戳转换为字符串
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# 将字符串转为时间戳
# print(time.mktime(time.strptime('2017-08-12 09:56:23','%Y-%m-%d %H:%M:%S')))

# clock() -- return CPU time since process start as a float
# print(time.clock())

# sleep delay for a number of seconds given as a float
# print(time.time())
# time.sleep(1.5)
# print(time.time())

# random 随机数模块
# import random,pprint
# pprint.pprint([m for m in dir(random) if not m.startswith('_')])
# print(random.__doc__)

# random() 返回[0,1)之间的随机实数
# print(random.random())

# randint
# Return random integer in range [a, b], including both end points.
# print(random.randint(1,10))

# randrange 
# Choose a random item from range(start, stop[, step])
# 返回range(start,stop,step)中的一个整数
# print(random.randrange(1,5))

# uniform 返回指定范围的随机实数
# Get a random number in the range [a, b) or [a, b] depending on rounding
# print(random.uniform(0,360))

# choice
# Choose a random element from a non-empty sequence.
# print(random.choice('abcdef'))

# random.sample(population, k)
# Return a k length list of unique elements chosen from the population sequence or se
# print(random.sample(range(10),3))
# 如果给定的序列含有重复元素 则认为它是不同的
# print(random.sample('aaabbbccc',2))

# shuffle
# random.shuffle(x[, random])
# Shuffle the sequence x in place.
# L = [1,2,3,4]
# print(L)
# random.shuffle(L)
# print(L)

# import random
# import time
# 返回指定时间范围内的随机时间
# date1 = (2013,1,1,0,0,0,-1,-1,-1)
# date2 = (2017,12,32,0,0,0,-1,-1,-1)
# sec1 = time.mktime(date1)
# sec2 = time.mktime(date2)
# sec =  random.uniform(sec1,sec2)
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(sec)))

# 掷骰子游戏
# dices = int(input('骰子数: '))
# sides = int(input('每个骰子的面数: '))
# L = []
# for i in range(dices):
# 	L.append(random.randrange(sides)+1)
# result = sum(L)
# print(L)
# print(result)

# 随机运势
# import fileinput, random
# fortunes = list(fileinput.input(files=('d:/dictionary.txt')))
# print(random.choice(fortunes))

# import pprint
# import random
# # 发牌
# values = list(range(1,11))+'Jack Queen King'.split(' ')
# suits = ['heart','spade','club','diamond']
# deck = ['{value} of {suit}'.format(value=v,suit=s) for v in values for s in suits]
# random.shuffle(deck)
# while deck:
# 	input()
# 	print(deck.pop())

# shelve 模块 以字典形式存储数据到文件
# shelve以键值对的方式存储数据 键必须为字符串 值可以是各种对象
# import shelve
# print(shelve.__doc__)
# db = None
# try:
# 	db = shelve.open('d:/she.txt')
# 	# db支持字典的操作 所有操作起来像字典
# 	db['name'] = 'Jack'
# 	if 'name' in db:
# 		print('my name is',db['name'])
# 	db['nums'] = [1,2,3]
# 	print(db['nums'])

# 	db['nums'].append(4) #并没有改变存储在文件的nums对应的值
# 	print(db['nums'])

# 	# 正确改变数据的方式
# 	temp = db['nums']
# 	temp.append(100)
# 	db['nums'] = temp
# 	print(db['nums'])
# except Exception as e:
# 	print(e)
# finally:
# 	if db:
# 		db.close()


# import re
# print(re.__doc__)
# print(re.split(r'\*','ab*23**de'))
# print(re.split(r'oo','foobar'))
# print(re.split(r'o(o)','foobar'))

# 替换
# print(re.sub(r'\d','*','kmd1234'))
# print(re.sub(r'\*([^\*]+)\*',r'<em>\1</em>','Hello,*Tom*'))

# 对字符串中为正则表达式中特殊字符的字符进行转义
# print(re.escape('abc.ok?kmd*'))

# match = re.search(r'^www\.(.+)\.com$','www.python.com')
# print(match.groups())
# print(match.group(),match.span())
# print(match.group(1),match.span(1))

# 一个模板系统
# import fileinput,re
# 匹配中括号里的字段
# pat = re.compile(r'\[(.+?)\]')
# # 我们将变量收集到这里
# scope = {}

# # 用于re.sub中
# def replacement(match):
# 	code = match.group(1)
# 	try:
# 		# 如果字段可以求值 则返回它
# 		return str(eval(code,scope))
# 	except:
# 		# 否则执行相同作用域内的赋值语句
# 		exec(code,scope)
# 		#返回空字符串
# 		return ''

# lines = []
# for line in fileinput.input(files=('d:/temp.txt')):
# 	lines.append(line)
# text = ''.join(lines)
# print(pat.sub(replacement,text))

# datetime 模块 操作时间日期 推荐使用该模块 比time好用
# import datetime,pprint
# pprint.pprint(dir(datetime))
# print(datetime.__doc__)
# print('='*80)

# pprint.pprint(dir(datetime.datetime))
# print(datetime.datetime.__doc__)

# print(datetime.datetime.now())
# print(datetime.datetime.now().timestamp()) #时间戳
# print(datetime.datetime.utcnow())
# print(datetime.datetime(2013,9,1))
# # 获取时间分量
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)
# print(datetime.datetime.now().hour)
# print(datetime.datetime.now().minute)
# print(datetime.datetime.now().second)
# print(datetime.datetime.now().weekday())
# # 格式化为字符串
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %p %w'))
# print(datetime.datetime(2017,8,1).isoformat())
# # 从字符串构建datetime
# print(datetime.datetime.strptime('2017-08-01 23:22:10','%Y-%m-%d %H:%M:%S').isoformat())
# print(datetime.datetime.now()+datetime.timedelta(days=1)) #增加分量
# # 时区转换
# print(datetime.datetime.utcnow().astimezone(datetime.timezone(datetime.timedelta(hours=8))))

# 读写文件
# 默认打开模式为'r' 如果不给read指定读取的字节数则会读取所有内容
# read方法在遇到文件末尾是返回空字符串
# with open('d:/abc.txt') as f:
# 	print(f.read())

# 一行一行地读取
# with open('d:/abc.txt') as f:
# 	while True:
# 		line = f.readline()
# 		if line == '':
# 			break
# 		else:
# 			print(line,end='')

# 用for循环读取
# with open('d:/abc.txt') as f:
# 	for line in f:
# 		print(line,end='')

# 如果不使用with 则必须在try-finally
# try:
# 	f = open('d:/abc.txt')
# 	for line in f:
# 		print(line,end='')
# finally:
# 	f.close()


# 将文件的所有行多一个列表 可以使用list(f) 或 readlines
# with open('d:/abc.txt') as f:
# 	# print(f.readlines())
# 	print(list(f))

# 二进制模式读取的是字节
# with open('d:/abc.txt','rb') as f:
	# print(f.read()) #返回字节数据

# 写文本文件
# with open('d:/x01.txt','w') as f:
# 	count = f.write('he你好') #返回写出的字符数量
# 	print(count)

# 写二进制文件
# with open('d:/x02.txt','wb') as f:
# 	count = f.write('he你好'.encode('gbk')) #返回写出的字节数量
# 	print(count)

# f.tell()返回文件指针当前位置
# f.seek(offset, from_what) 移动文件指针 参考位置 0文件开头 默认值 1当前位置 3末尾
# 文本模式下 只能seek(0) 或seek(f.tell())
# with open('d:/abc.txt') as f:
# 	print(f.tell())
# 	print(f.readline())
# 	print(f.tell())
# 	f.seek(0)
# 	print(f.tell())
# 	print(f.readline())


# 使用json方式序列化与反序列化数据
# json模块直接支持python的基本数据类型 对象类型需要额外的工作
# import json
# print(json.__doc__)
# json序列化
# 返回数据的json字符串表示
# d = {'name':'Jack','age':23,'books':['abc','defg']}
# json_str = json.dumps(d)
# print(json_str)
# with open('d:/x03.txt','w') as f:
	# 写入到文件
	# json.dump(d,f)

# json反序列化
# json_str = '{"name": "Jack", "age": 23, "books": ["abc", "defg"]}'
# d = json.loads(json_str) 
# print(d)
# 从文件读取
# with open('d:/x03.txt') as f:
# 	d = json.load(f)
# 	print(d)

# 对象序列化
# class Student(object):
#     def __init__(self,name,gender,score):
#         self.name = name
#         self.gender = gender
#         self.score = score
# def student2Dict(st):
#     return {'name':st.name,'gender':st.gender,'score':st.score}
# st = Student('Tom','男',98)
# s = json.dumps(st,default=student2Dict)
# # s = json.dumps(st,default=lambda x:x.__dict__)
# def dict2Student(d):
#     return Student(d['name'],d['gender'],d['score'])
# st2 = json.loads(s,object_hook=dict2Student)
# print(st2)
# print(st2.name)

# while True:
# 	try:
# 		num = int(input('Please enter a integer: '))
# 		print(num)
# 		break
# 	except ValueError:
# 		print('不能转换为整数，请重新输入')


# GUI wxPython

# First things, first. Import the wxPython package.
# import wx
# # Next, create an application object.
# app = wx.App()
# # Then a frame.
# frm = wx.Frame(None, title="Hello World")
# # Show it.
# frm.Show()
# # Start the event loop.
# app.MainLoop()


# import wx
# app = wx.App()
# frm = wx.Frame(None,title='Simple Frame')
# open_btn = wx.Button(frm,label='open')
# save_btn = wx.Button(frm,label='save')
# frm.Show()
# app.MainLoop()

# import wx
# app = wx.App()
# frm = wx.Frame(None,title='Simple Frame',size=(520,440))
# open_btn = wx.Button(frm,label='open',size=(100,50),pos=(300,0))
# save_btn = wx.Button(frm,label='save',size=(100,50),pos=(400,0))
# fn_tc = wx.TextCtrl(frm,size=(300,50),pos=(0,0))
# content_tc = wx.TextCtrl(frm,size=(500,350),pos=(0,50),style=wx.TE_MULTILINE|wx.HSCROLL)
# frm.Show()
# app.MainLoop()


# 搞布局
# import wx
# app = wx.App()
# frm = wx.Frame(None,title='Simple Frame',size=(500,300))
# pnl = wx.Panel(frm)

# open_btn = wx.Button(pnl,label='open')
# save_btn = wx.Button(pnl,label='save')
# fn_tc = wx.TextCtrl(pnl)
# content_tc = wx.TextCtrl(pnl,style=wx.TE_MULTILINE|wx.HSCROLL)

# hbox = wx.BoxSizer()
# hbox.Add(fn_tc,proportion=1,flag=wx.EXPAND)
# hbox.Add(open_btn,proportion=0,flag=wx.LEFT,border=5)
# hbox.Add(save_btn,proportion=0,flag=wx.LEFT,border=5)

# vbox = wx.BoxSizer(wx.VERTICAL)
# vbox.Add(hbox,proportion=1,flag=wx.EXPAND | wx.ALL,border=5)
# vbox.Add(content_tc,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,border=5)

# pnl.SetSizer(vbox)

# frm.Show()
# app.MainLoop()



# 事件处理
# import wx
# app = wx.App()
# frm = wx.Frame(None,title='Simple Frame',size=(500,300))
# pnl = wx.Panel(frm)

# open_btn = wx.Button(pnl,label='open')
# save_btn = wx.Button(pnl,label='save')
# fn_tc = wx.TextCtrl(pnl)
# content_tc = wx.TextCtrl(pnl,style=wx.TE_MULTILINE|wx.HSCROLL)

# hbox = wx.BoxSizer()
# hbox.Add(fn_tc,proportion=1,flag=wx.EXPAND)
# hbox.Add(open_btn,proportion=0,flag=wx.LEFT,border=5)
# hbox.Add(save_btn,proportion=0,flag=wx.LEFT,border=5)

# vbox = wx.BoxSizer(wx.VERTICAL)
# vbox.Add(hbox,proportion=1,flag=wx.EXPAND | wx.ALL,border=5)
# vbox.Add(content_tc,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,border=5)

# pnl.SetSizer(vbox)

# def loadFile(event):
# 	filename = fn_tc.GetValue().strip()
# 	if filename:
# 		content_tc.SetValue(open(filename).read())
# 	else:
# 		 wx.MessageBox("文件名不能为空")

# open_btn.Bind(wx.EVT_BUTTON,loadFile)

# def saveFile(event):
# 	content = content_tc.GetValue().rstrip()
# 	if content:
# 		filename = fn_tc.GetValue().strip()
# 		if filename:
# 			with open(filename,'a+') as f:
# 				f.write(content)
# save_btn.Bind(wx.EVT_BUTTON,saveFile)

# frm.Show()
# app.MainLoop()


"""
Hello World, but with more meat.
"""


# import wx

# class HelloFrame(wx.Frame):
#     """
#     A Frame that says Hello World
#     """

#     def __init__(self, *args, **kw):
#         # ensure the parent's __init__ is called
#         super(HelloFrame, self).__init__(*args, **kw)

#         # create a panel in the frame
#         pnl = wx.Panel(self)

#         # and put some text with a larger bold font on it
#         st = wx.StaticText(pnl, label="Hello World!", pos=(25,25))
#         font = st.GetFont()
#         font.PointSize += 10
#         font = font.Bold()
#         st.SetFont(font)

#         # create a menu bar
#         self.makeMenuBar()

#         # and a status bar
#         self.CreateStatusBar()
#         self.SetStatusText("Welcome to wxPython!")


#     def makeMenuBar(self):
#         """
#         A menu bar is composed of menus, which are composed of menu items.
#         This method builds a set of menus and binds handlers to be called
#         when the menu item is selected.
#         """

#         # Make a file menu with Hello and Exit items
#         fileMenu = wx.Menu()
#         # The "\t..." syntax defines an accelerator key that also triggers
#         # the same event
#         helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
#                 "Help string shown in status bar for this menu item")
#         fileMenu.AppendSeparator()
#         # When using a stock ID we don't need to specify the menu item's
#         # label
#         exitItem = fileMenu.Append(wx.ID_EXIT)

#         # Now a help menu for the about item
#         helpMenu = wx.Menu()
#         aboutItem = helpMenu.Append(wx.ID_ABOUT)

#         # Make the menu bar and add the two menus to it. The '&' defines
#         # that the next letter is the "mnemonic" for the menu item. On the
#         # platforms that support it those letters are underlined and can be
#         # triggered from the keyboard.
#         menuBar = wx.MenuBar()
#         menuBar.Append(fileMenu, "&File")
#         menuBar.Append(helpMenu, "&Help")

#         # Give the menu bar to the frame
#         self.SetMenuBar(menuBar)

#         # Finally, associate a handler function with the EVT_MENU event for
#         # each of the menu items. That means that when that menu item is
#         # activated then the associated handler function will be called.
#         self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
#         self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
#         self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


#     def OnExit(self, event):
#         """Close the frame, terminating the application."""
#         self.Close(True)


#     def OnHello(self, event):
#         """Say hello to the user."""
#         wx.MessageBox("Hello again from wxPython")


#     def OnAbout(self, event):
#         """Display an About Dialog"""
#         wx.MessageBox("This is a wxPython Hello World sample",
#                       "About Hello World 2",
#                       wx.OK|wx.ICON_INFORMATION)


# if __name__ == '__main__':
#     # When this module is run (not imported) then create the app, the
#     # frame, show it, and start the event loop.
#     app = wx.App()
#     frm = HelloFrame(None, title='Hello World 2')
#     frm.Show()
#     app.MainLoop()


# tkinter GUI python自带的GUI库
# import tkinter as tk

# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=root.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()


# from tkinter import *
# root = Tk()

# gui-01 最简单的GUI hello world
# label = Label(root,text='Hello tkinter')
# label.pack()

# gui-02 带图片的Label
# logo = PhotoImage(file='images/python_logo_small.gif')
# w1 = Label(root,image=logo).pack(side='right')
# s = 'At present, only GIF and PPM/PGM formats are supported'
# w2 = Label(root,justify=LEFT,padx=10,text=s).pack(side='left')

# gui-03 跳转Label中图片与文字的位置
# logo = PhotoImage(file='images/python_logo_small.gif')
# s = 'At present, only GIF and PPM/PGM formats are supported'
# # w = Label(root,image=logo,text=s,compound=CENTER).pack(side='left')
# w = Label(root,image=logo,text=s,compound=LEFT,padx=20,justify=LEFT).pack(side='left')

# gui-04 设置Label的文字，颜色，背景色
# Label(root, 
# 		 text="Red Text in Times Font",
# 		 fg = "red",
# 		 font = "Times").pack()
# Label(root, 
# 		 text="Green Text in Helvetica Font",
# 		 fg = "light green",
# 		 bg = "dark green",
# 		 font = "Helvetica 16 bold italic").pack()
# Label(root, 
# 		 text="Blue Text in Verdana bold",
# 		 fg = "blue",
# 		 bg = "yellow",
# 		 font = "Verdana 10 bold").pack()

# gui-04 动态设置Label文字
# counter = 0 
# def counter_label(label):
#   def count():
#     global counter
#     counter += 1
#     label.config(text=str(counter))
#     label.after(1000, count)
#   count()
 
 
# root.title("Counting Seconds")
# label = Label(root, fg="green")
# label.pack()
# counter_label(label)
# button = Button(root, text='Stop', width=25, command=root.destroy)
# button.pack()

# gui-05 Button
# class App(Frame):
# 	def __init__(self,master=None):
# 		super().__init__(master)
# 		self.pack()
# 		self.button = Button(self,text='Quit',fg='red',command=quit)
# 		self.button.pack(side=LEFT)
# 		self.slogan = Button(self,text='Hello',command=self.print_slogan)
# 		self.slogan.pack(side=LEFT)
# 	def print_slogan(self):
# 		print('life is short,you need python')
# app = App(root)

# gui-05 不使用继承 实现上例
# class App(object):
# 	def __init__(self,master=None):
# 		frame = Frame(master)
# 		frame.pack()
# 		self.button = Button(frame,text='Quit',fg='red',command=quit)
# 		self.button.pack(side=LEFT)
# 		self.slogan = Button(frame,text='Hello',command=self.print_slogan)
# 		self.slogan.pack(side=LEFT)
# 	def print_slogan(self):
# 		print('life is short,you need python')
# app = App(root)

# gui-06 动态设置label文字 指定按下stop按钮
# counter = 0
# def count_label(label):
# 	def count():
# 		global counter
# 		counter += 1
# 		label.config(text=str(counter))
# 		label.after(1000,count)
# 	count()
# label = Label(root,fg='dark green')
# label.pack()
# button = Button(root,text='stop',command=root.destroy)
# button.pack()
# count_label(label)

# gui-07 radio button
# v = IntVar()
# Label(root,
# 	text='Choose a programming language:',
# 	justify = LEFT,
# 	padx = 20
# 	).pack()
# Radiobutton(root,
# 	text='Python',
# 	padx=20,
# 	variable=v,
# 	value=1).pack(anchor=W)
# Radiobutton(root,
# 	text='Java',
# 	padx=20,
# 	variable=v,
# 	value=2).pack(anchor=W)

# gui-08 通过循环创建多个radio button
# v = IntVar()
# v.set(1)  # initializing the choice, i.e. Python

# languages = [
#     ("Python",1),
#     ("Perl",2),
#     ("Java",3),
#     ("C++",4),
#     ("C",5)
# ]

# def ShowChoice():
#     print(v.get())

# Label(root, 
#       text="""Choose your favourite 
# programming language:""",
#       justify = LEFT,
#       padx = 20).pack()

# for e in languages:
# 	Radiobutton(root,
# 		text=e[0],
# 		padx=20,
# 		variable=v,
# 		command=ShowChoice,
# 		value=e[1]).pack(anchor=W)

# gui-09 条状的radio button
# Label(root,
# 	text = 'Choose your favorite programming language:',
# 	justify = LEFT,
# 	padx = 40
# 	).pack()

# v = IntVar()
# v.set(1)

# textValues = [
# 	('Python',1),
# 	('C++',2),
# 	('Java',3),
# 	('C',4),
# ]

# for txtVal in textValues:
# 	Radiobutton(root,
# 		text = txtVal[0],
# 		value = txtVal[1],
# 		variable = v,
# 		indicatoron = 0,
# 		width = 20,
# 		padx = 20
# 		).pack()

# gui-10 checkbox
# var1 = IntVar()
# Checkbutton(root, text='male', variable=var1).grid(row=0, sticky=W)
# var2 = IntVar()
# Checkbutton(root, text='female', variable=var2).grid(row=1, sticky=W)

# gui-11 checkbox
# var1 = IntVar()
# var2 = IntVar()
# def var_states():
# 	print('male: {}\nfemale: {}'.format(var1.get(), var2.get()))
# Label(root, text='Your sex:').grid(row=0, sticky=W)
# Checkbutton(root, text='male', variable=var1).grid(row=1, sticky=W)
# Checkbutton(root, text='female', variable=var2).grid(row=2, sticky=W)
# Button(root, text='Quit', command=root.quit).grid(row=3, sticky=W, pady=4)
# Button(root, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)

# gui-12 checkbox
# class Checkbar(Frame):
# 	def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
# 		Frame.__init__(self, parent)
# 		self.vars = []
# 		for pick in picks:
# 			var = IntVar()
# 			chk = Checkbutton(self, text=pick, variable=var)
# 			chk.pack(side=side, anchor=anchor, expand=YES)
# 			self.vars.append(var)
# 	def state(self):
# 		return map((lambda var : var.get()), self.vars)

# lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
# tgl = Checkbar(root, ['English', 'German'])
# lng.pack(side=TOP, fill=X)
# tgl.pack(side=LEFT)
# lng.config(relief=GROOVE, bd=2)

# def allstates():
# 	print(list(lng.state()), list(tgl.state()))

# Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
# Button(root, text='Peek', command=allstates).pack(side=RIGHT)

# gui-12 entry 输入控件
# Label(root, text='First Name').grid(row=0)
# Label(root, text='Last Name').grid(row=1)
# e1 = Entry(root)
# e1.grid(row=0, column=1)
# Entry(root).grid(row=1, column=1)

# gui-13 获取输入框的值
# Label(root, text='First Name').grid(row=0)
# Label(root, text='Last Name').grid(row=1)

# e1 = Entry(root)
# e1.grid(row=0, column=1)
# e1.insert(0,'Mendel') #插入值

# e2 = Entry(root)
# e2.grid(row=1, column=1)

# def show_entry_fields():
# 	print('First Name: {}\nLast Name: {}'.format(e1.get(), e2.get()))

# def clear_entry_fields():
# 	e1.delete(0)
# 	e2.delete(0,END)

# Button(root, text='Quit', command=root.quit).grid(row=3, column=0, sticky=W, pady=4)
# Button(root, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
# Button(root, text='Clear', command=clear_entry_fields).grid(row=3, column=2, sticky=W, pady=4)

# gui-14 通过循环创建多个控件
# fields = 'Last Name', 'First Name', 'Job', 'Country'

# def fetch(entries):
# 	for entry in entries:
# 		field = entry[0]
# 		text = entry[1].get()
# 		print('{}: {}'.format(field, text))

# def makeform(root, fields):
# 	entries = []
# 	for field in fields:
# 		row = Frame(root)
# 		lab = Label(row, width=15, text=field, anchor='w')
# 		ent = Entry(row)
# 		row.pack(side=TOP, fill=X, padx=5, pady=5)
# 		lab.pack(side=LEFT)
# 		ent.pack(side=RIGHT, expand=YES, fill=X)
# 		entries.append((field, ent))
# 	return entries

# ents = makeform(root, fields)
# root.bind('<Return>', (lambda event, e=ents: fetch(e)))
# b1 = Button(root, text='Show', command=(lambda e=ents: fetch(e)))
# b1.pack(side=LEFT, padx=5, pady=5)
# b2 = Button(root, text='Quit', command=root.quit)
# b2.pack(side=LEFT, padx=5, pady=5)

# gui-15 简易计算器
# def calc(event):
# 	res.configure(text=str(eval(entry.get())))

# Label(root, text='结果为:').pack()

# res = Label(root)
# res.pack()

# entry = Entry(root)
# entry.pack()
# entry.bind('<Return>',calc)

# gui-16 canvas
# canvas_width = 80
# canvas_height = 40
# canvas = Canvas(root, width=canvas_width, height=canvas_height)
# canvas.pack()
# y = int(canvas_height/2)
# canvas.create_line(0, y, canvas_width, y, fill='green')

# gui-17 canvas
# canvas = Canvas(root, width=200, height=100, bg='red', bd=0)
# canvas.pack()
# canvas.create_rectangle(50,20,150,80, fill='#0f0')
# canvas.create_rectangle(65,35,135,65, fill='#ff0')
# canvas.create_line(0,0,50,20, fill='#476042', width=3)
# canvas.create_line(150,20,200,0, fill='#476042', width=3)
# canvas.create_line(0,100,50,80, fill='#476042', width=3)
# canvas.create_line(150,80,200,100, fill='#476042', width=3)

# gui-18 canvas text
# canvas_width = 200
# canvas_height = 100

# ratios = (0.2, 0.35)
# colors = ('#ff0', '#0f0')

# boxs = []
# for r in ratios:
# 	boxs.append((canvas_width*r, canvas_height*r, 
# 		canvas_width*(1-r), canvas_height*(1-r)) )

# canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='#f00')
# canvas.pack()

# for i,box in enumerate(boxs):
# 	canvas.create_rectangle(box[0],box[1],box[2],box[3], fill=colors[i])

# canvas.create_line(0,0, boxs[0][0], boxs[0][1], fill='#0f0', width=3)
# canvas.create_line(0,canvas_height, boxs[0][0], boxs[0][3], fill='#0f0', width=3)
# canvas.create_line(boxs[0][2],boxs[0][1], canvas_width, 0, fill='#0f0', width=3)
# canvas.create_line(boxs[0][2],boxs[0][3], canvas_width, canvas_height, fill='#0f0', width=3)

# canvas.create_text(canvas_width/2, canvas_height/2, text='Python')

# gui-19 canvas oval
# canvas = Canvas(root, width=200, height=100, bg='#f00')
# canvas.pack()
# # canvas.create_oval(50,20,150,80, fill='#0f0')
# canvas.create_oval(50,20,150,80, outline='#0f0', width=3)

# gui-20 canvas mouse paint
# canvas_width = 500
# canvas_height = 100
# def paint(event):
# 	x1, y1 = event.x-1, event.y-1
# 	x2, y2 = event.x+1, event.y+1
# 	canvas.create_oval(x1,y1,x2,y2, fill='#000')

# canvas = Canvas(root, width=canvas_width, height=canvas_height)
# canvas.bind('<B1-Motion>', paint)

# message = Label(root, text='Press and Drag the mouse to draw')

# root.title('Painting using Ovals')
# canvas.pack(expand=YES, fill=BOTH)
# message.pack(side=BOTTOM)

# gui-21 canvas
# canvas_width = 200
# canvas_height = 200
# canvas = Canvas(root, width=canvas_width, height=canvas_height)
# canvas.pack()
# points = [0,0, canvas_width,canvas_height/2, 0,canvas_height]
# canvas.create_polygon(points, outline='#00f', width=3, fill='#ff0')

# gui-22 canvas paint star
# canvas_width = 400
# canvas_height =400
# python_green = "#476042"
# p = 20
# t = 5
# def paint_star(canvas,x,y,p,t, outline=python_green, fill='#ff0', width=1):
# 	points = []
# 	for i in (1,-1):
# 		points.extend((x, y+i*p))
# 		points.extend((x+i*t, y+i*t))
# 		points.extend((x+i*p, y))
# 		points.extend((x+i*t, y-i*t))
# 	canvas.create_polygon(points, outline=outline, width=3, fill=fill)

# canvas = Canvas(root, width=canvas_width, height=canvas_height)
# canvas.pack()
# nsteps = 10
# dist = canvas_width/nsteps
# for i in range(1,nsteps):
# 	paint_star(canvas, i*dist, i*dist, p, t)
# 	paint_star(canvas, i*dist, canvas_height-i*dist, p, t)

# gui-23 Bitmaps
# canvas_width = 300
# canvas_height = 80
# canvas = Canvas(root,width=canvas_width,height=canvas_height)
# canvas.pack()

# bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", 
# "hourglass", "info", "questhead", "question", "warning"]
# nsteps = len(bitmaps)
# step_x = int(canvas_width/nsteps)
# for i in range(0,nsteps):
# 	canvas.create_bitmap(i*step_x+step_x/2,50,bitmap=bitmaps[i])

# gui-24 The Canvas method create_image(x0,y0, options ...) is used to draw an image on a canvas. create_image doesn't accept an image directly. It uses an object which is created by the PhotoImage() method. 
# The PhotoImage class can only read GIF and PGM/PPM images from files
# canvas = Canvas(root,width=300,height=300)
# canvas.pack()
# img = PhotoImage(file="../images/timg.gif")
# canvas.create_image(10,10,anchor=NW,image=img)

# gui-25 画方格
# canvas_width = 200
# canvas_height = 100
# def checkered(canvas,line_distance):
# 	for x in range(line_distance,canvas_width,line_distance):
# 		canvas.create_line(x,0,x,canvas_height,fill='#000')
# 	for y in range(line_distance,canvas_height,line_distance):
# 		canvas.create_line(0,y,canvas_width,y,fill='#000')

# canvas = Canvas(root,width=canvas_width,height=canvas_height)
# canvas.pack()
# checkered(canvas,10)

# gui-26 slider
# s1 = Scale(root,from_=0,to=24)
# s1.pack()
# s2 = Scale(root,from_=0,to=200,orient=HORIZONTAL)
# s2.pack()

# gui-27 获取slider的值
# s1 = Scale(root,from_=0,to=24)
# s1.pack()
# s2 = Scale(root,from_=0,to=200,orient=HORIZONTAL)
# s2.pack()
# def show_values():
# 	print(s1.get(),s2.get())
# 	print(type(s1.get()))
# Button(root,text='View value',command=show_values).pack()


# gui-28 位slider设置初值
# s1 = Scale(root,from_=0,to=24)
# s1.set(10)
# s1.pack()

# s2 = Scale(root,from_=0,to=200,orient=HORIZONTAL)
# s2.set(100)
# s2.pack()

# def show_values():
# 	print(s1.get(),s2.get())
# 	print(type(s1.get()))
# Button(root,text='View value',command=show_values).pack()

# gui-29 位slider设置初值，刻度间隔，长度
# s1 = Scale(root,from_=0,to=24,tickinterval=8)
# s1.set(10)
# s1.pack()

# s2 = Scale(root,from_=0,to=200,tickinterval=10,length=600,orient=HORIZONTAL)
# s2.set(100)
# s2.pack()

# def show_values():
# 	print(s1.get(),s2.get())
# 	print(type(s1.get()))
# Button(root,text='View value',command=show_values).pack()

# gui-30 Text
# A text widget is used for multi-line text area. The Tkinter text widget is very 
# powerful and flexible and can be used for a wide range of tasks. 
# Though one of the main purposes is to provide simple multi-line areas, 
# as they are often used in forms, 
# text widgets can also be used as simple text editors or even web browsers. 
# T = Text(root,height=2,width=30) #注意height以行为单位
# T.pack()
# T.insert(END, 'Just a text widget\nThere are two lines')

# gui-31 带滚动条的Text
# t = Text(root,height=4,width=40)
# s = Scrollbar(root)
# t.pack(side=LEFT,fill=Y)
# s.pack(side=RIGHT,fill=Y)
# t.config(yscrollcommand=s.set)
# s.config(command=t.yview)
# quote='''HAMLET: To be, or not to be--that is the question:
# Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune
# Or to take arms against a sea of troubles
# And by opposing end them. To die, to sleep--
# No more--and by a sleep to say we end
# The heartache, and the thousand natural shocks
# That flesh is heir to. 'Tis a consummation
# Devoutly to be wished.'''
# t.insert(END,quote)

# gui-32 带两个滚动条的Text
# t = Text(root,height=4,width=40,wrap=NONE)
# s = Scrollbar(root)
# s2 = Scrollbar(root,orient=HORIZONTAL)
# s.pack(side=RIGHT,fill=Y)
# s2.pack(side=BOTTOM,fill=X)
# t.pack(side=LEFT,fill=BOTH,expand=1)
# t.config(yscrollcommand=s.set)
# t.config(xscrollcommand=s2.set)
# s.config(command=t.yview)
# s2.config(command=t.xview)
# quote='''HAMLET: To be, or not to be--that is the question:
# Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune
# Or to take arms against a sea of troubles
# And by opposing end them. To die, to sleep--
# No more--and by a sleep to say we end
# The heartache, and the thousand natural shocks
# That flesh is heir to. 'Tis a consummation
# Devoutly to be wished.'''
# t.insert(END,quote)

# gui-33
# text1 = Text(root, height=20, width=30)
# photo=PhotoImage(file='../images/shakespare.gif')
# text1.insert(END,'\n')
# text1.image_create(END, image=photo)

# text1.pack(side=LEFT)

# text2 = Text(root, height=20, width=50)
# scroll = Scrollbar(root, command=text2.yview)
# text2.configure(yscrollcommand=scroll.set)
# text2.tag_configure('big', font=('Verdana', 20, 'bold'))
# text2.tag_configure('color', foreground='#476042', 
# 						font=('Tempus Sans ITC', 12, 'bold'))

# text2.insert(END,'\nWilliam Shakespeare\n', 'big')
# quote = """
# To be, or not to be that is the question:
# Whether 'tis Nobler in the mind to suffer
# The Slings and Arrows of outrageous Fortune,
# Or to take Arms against a Sea of troubles,
# """
# text2.insert(END, quote, 'color')

# # text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
# def cb(e):
# 	text2.insert(END, "Not now, maybe later!")
# 	print(e)
# text2.tag_bind('follow', '<1>', cb)
# text2.insert(END, 'follow-up\n', 'follow')
# text2.pack(side=LEFT)
# scroll.pack(side=RIGHT, fill=Y)

# gui-34 dialog
# from tkinter.messagebox import * #旧版的模块名为tkMessageBox 
# def answer():
# 	r = showerror('Answer','Sorry, no answer available')
# 	print(r)
# 	print(type(r))

# def callback():
# 	if askyesno('Verify','Really quit?'):
# 		r = showwarning('Yes','Not yet implemented')
# 	else:
# 		r = showinfo('No','Quit has been cancelled')

# Button(text='Quit',command=callback).pack(fill=X)
# Button(text='Answer',command=answer).pack(fill='x')

# gui-35 文件对话框
# import tkinter.filedialog
# def callback():
# 	path = tkinter.filedialog.askopenfilename()
# 	print(path)
# def callback2():
# 	pass
# 	path = tkinter.filedialog.asksaveasfilename()
# 	print(path)
# Button(text='File open',command=callback).pack(fill=X)
# Button(text='File save',command=callback2).pack(fill=X)

# gui-36 颜色对话框
# import tkinter.colorchooser
# def callback():
# 	color = tkinter.colorchooser.askcolor()
# 	print(color)
# Button(text='Choose color',command=callback).pack()

# gui-37 layout 布局
# Label(root,text='Red Sun',bg='red',fg='white').pack()
# Label(root,text='Green grass',bg='green',fg='white').pack()
# Label(root,text='Blue sky',bg='blue',fg='white').pack()


# gui-38 fill
# Label(root,text='Red Sun',bg='red',fg='white').pack(fill=X)
# Label(root,text='Green grass',bg='green',fg='white').pack(fill=X)
# Label(root,text='Blue sky',bg='blue',fg='white').pack(fill=X)

# gui-39 外边距 padx,pady
# Label(root,text='Red Sun',bg='red',fg='white').pack(fill=X,padx=10)
# Label(root,text='Green grass',bg='green',fg='white').pack(fill=X,padx=20)
# Label(root,text='Blue sky',bg='blue',fg='white').pack(fill=X,pady=20)

# gui-40 内边距 ipadx,ipady
# Label(root,text='Red Sun',bg='red',fg='white').pack()
# Label(root,text='Green grass',bg='green',fg='white').pack(ipadx=10)
# Label(root,text='Blue sky',bg='blue',fg='white').pack(ipady=10)

# gui-41 side
# Label(root,text='Red',bg='red',fg='white').pack(padx=5,pady=10,side=LEFT)
# Label(root,text='Green',bg='green',fg='white').pack(padx=5,pady=10,side=LEFT)
# Label(root,text='Blue',bg='blue',fg='white').pack(padx=5,pady=10,side=LEFT)

# gui-42 place布局
# import random
# # width x height + x_offset + y_offset:
# root.geometry('170x205+30+30')

# languages = ['python','Perl','C++','Java','Tcl/Tk']
# labels = range(5)
# for i in range(5):
# 	ct = [random.randrange(256) for x in range(3)]
# 	brightness = int(round(0.299*ct[0]+0.587*ct[1]+0.114*ct[2]))
# 	ct_hex = '{:02x}{:02x}{:02x}'.format(*ct)
# 	bg_color = '#'+''.join(ct_hex)
# 	l = Label(root,text=languages[i],fg='White' if brightness < 120 else 'black',
# 		bg=bg_color)
# 	l.place(x=25,y=30+i*30,width=120,height=25)

# gui-43 gird布局
# colors = ['red','orange','yellow','green','blue','white']
# for i in range(len(colors)):
# 	Label(root,text=colors[i],relief=RIDGE,width=15).grid(row=i,column=0)
# 	Entry(root,bg=colors[i],relief=SUNKEN,width=10).grid(row=i,column=1)

# gui-44 菜单
# import tkinter.filedialog
# import tkinter.messagebox

# def newFile():
# 	print("new File")
# def openFile():
# 	path = tkinter.filedialog.askopenfilename()
# 	print(path)
# def about():
# 	print(tkinter.messagebox.showinfo('about','by xxx'))

# menu = Menu(root)
# root.config(menu=menu)

# filemenu = Menu(menu)
# menu.add_cascade(label='File',menu=filemenu)
# filemenu.add_command(label='New',command=newFile)
# filemenu.add_command(label='Open...',command=openFile)
# filemenu.add_separator()
# filemenu.add_command(label='Exit',command=root.quit)

# helpmenu = Menu(menu)
# menu.add_cascade(label='help',menu=helpmenu)
# helpmenu.add_command(label='about',command=about)

# gui-45 事件
# def cb1(e):
# 	print('Button-1')

# def cb2(e):
# 	print('Double-1')

# button = Button(root, text='Click me')
# button.bind('<Button-1>', cb1)
# button.bind('<Double-1>', cb2)
# button.pack()

# gui-46 motion event
# top=root.winfo_toplevel()
# print(top is root)
# top.rowconfigure(0, weight=1)
# top.columnconfigure(0, weight=1)

# def cb1(e):
# 	print(e.__dict__)
# 	print('Mouse position: x={}, y={}'.format(e.x, e.y))

# str1 = 'To be or not to be. That is a question.'
# msg = Message(root, text=str1, bg='lightgreen')
# msg.bind('<Motion>', cb1)
# msg.grid(row=0, column=0, sticky=N+S+W)

# root.mainloop()


# import tkinter as tk
# import pprint

# root = tk.Tk()
# btn = tk.Button(root,text='button')
# def list_config():
	# 打印控件的属性
# 	# print(btn.keys())
# 	# pprint.pprint(btn.config())
# 	pprint.pprint(btn.config('bg'))
# btn['command'] = list_config
# btn.pack()
# root.mainloop()




# python为数据库操作规定了同一的接口 不同的数据库只需实现该接口 即可用python操作该数据库
# import pymysql
# print(pymysql.__doc__)
# python DB API规定 数据库模块必须提供下面三个全局变量
# print(pymysql.apilevel) #实现的api版本
# print(pymysql.threadsafety) #线程安全等级 取值0~3的整数
# print(pymysql.paramstyle) #sql语句的参数格式

# 使用connect函数创建与数据库的连接
# print(pymysql.connect.__doc__)
# connect接受一些指定数据库信息的参数：host,user,password,database,charset等
# connect函数返回一个连接对象 通过该对象的方法 cursor,commit,rollback,
# close等可获取游标，提交或回滚，关闭连接
# try:
# 	conn = pymysql.connect(host='localhost',user='root',password='',
# 		database='db01',charset='utf8')
# 	# print(conn.cursor.__doc__)
# 	cursor = conn.cursor(pymysql.cursors.DictCursor)

	# 查询
	# cursor.execute('select id,name,gender,salary from emp')
	# rows = cursor.fetchall()
	# for row in rows:
	# 	print(row['id'],row['name'],float(row['salary']))

	# cursor.execute('insert into emp(name,gender,salary) values("%s","%s",%f)' % ('x01','女',2300))
	# conn.commit()
	# print(cursor.rowcount)
	# print(cursor.lastrowid)

	# cursor.execute('update emp set salary=%f where id=10' % 3500.5)
	# print(cursor.rowcount)
	# conn.commit()

	# cursor.execute('delete from emp where id=%d' % 10)
	# print(cursor.rowcount)
	# conn.commit()

# finally:
# 	cursor.close()
# 	conn.close()


# import urllib.request
# with urllib.request.urlopen('http://www.python.org') as file:
# 	data = file.read()
# 	print(data.decode('utf-8'))

# import urllib.request
# with urllib.request.urlopen('http://python.org/') as response:
#    data = response.read()
#    html = data.decode('utf-8')
#    print(html)

# 如果想把返回的数据临时保存到文件 可以调用urlretrieve方法
# import urllib.request
# # local_filename, headers = urllib.request.urlretrieve('http://python.org/')
# # 如果提供第二个参数则会保存到指定位置
# local_filename, headers = urllib.request.urlretrieve('http://python.org/','d:/pyp.txt')
# print(local_filename)
# print(headers) #类型为<class 'http.client.HTTPMessage'>
# html = open(local_filename) #之后可以进行文件操作

# post方式提交请求参数
# import urllib.request
# import urllib.parse
# url = 'http://localhost/test/t01.php'
# values = {'name' : 'Michael Foord',
#           'location' : '中国 Northampton',
#           'language' : 'Python' }

# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8') # data should be bytes
# req = urllib.request.Request(url, data) #如果不传递参数则为get请求 否则为post
# with urllib.request.urlopen(req) as response:
#    the_page = response.read()
#    html = the_page.decode('utf-8')
#    print(html)

# get方式提交参数
# import urllib.request
# import urllib.parse
# url = 'http://localhost/test/t01.php'
# url_params = {'name':'Jack','location':'陕西','language':'老陕'}
# query_string = urllib.parse.urlencode(url_params)
# print(query_string)
# url = url+'?'+query_string
# with urllib.request.urlopen(url) as response:
# 	data = response.read()
# 	print(data.decode('utf-8'))

# 添加消息头
# import urllib.request
# import urllib.parse
# url = 'http://localhost/test/t01.php'
# headers = {
# 	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
# }
# params = {
# 	'name' : 'Ro啦',
# 	'location' : 'heaven',
# 	'language' : '斯柯达啦'
# }
# params = urllib.parse.urlencode(params)
# params = params.encode('utf-8')
# req = urllib.request.Request(url,params,headers)
# with urllib.request.urlopen(req) as response:
# 	print(response.headers)
# 	data = response.read()
# 	data_str = data.decode('utf-8')
# 	print(data_str)

# URLError 
# import urllib.request
# import urllib.error
# bad_url = 'http://localhost/xxx'
# req = urllib.request.Request(bad_url)
# try:
# 	res = urllib.request.urlopen(req)
# except urllib.error.URLError as e:
# 	print(e)

# HTTPError是 URLError的子类
# import urllib.request
# import urllib.error
# bad_url = 'http://localhost/xxx'
# req = urllib.request.Request(bad_url)
# try:
# 	res = urllib.request.urlopen(req)
# except urllib.error.HTTPError as e:
# 	print(e.code) #状态码
# 	print(e.read().decode('utf-8')) #错误页


# 查看所有状态码及其描述
# import http.server
# import pprint
# pprint.pprint(http.server.BaseHTTPRequestHandler.responses)

# 错误处理 获取响应头信息
# from urllib.request import Request, urlopen
# from urllib.error import URLError
# req = Request('http://localhost/test')
# try:
#     response = urlopen(req)
# except URLError as e:
#     if hasattr(e, 'reason'):
#         print('We failed to reach a server.')
#         print('Reason: ', e.reason)
#     elif hasattr(e, 'code'):
#         print('The server couldn\'t fulfill the request.')
#         print('Error code: ', e.code)
# else:
# 	data = response.read()
# 	data_str = data.decode('utf-8')
# 	print(data_str)
# 	print(response.geturl())
# 	print(response.headers)
# 	print(response.info())
# 	print(response.info()['Content-Type'])
# 	response.close()


# url解析
# import urllib.parse
# url = 'http://www.cwi.nl:80/%7Eguido/Python.html;abc?id=1001#1'
# o = urllib.parse.urlparse(url)
# print(o)
# print(o.scheme)
# print(o.netloc)
# print(o.geturl())


# import os
# import os.path
# import pprint
# pprint.pprint(dir(os))
# print(os.__doc__)
# print(os.curdir)
# print(os.sep)
# print(repr(os.linesep))
# print(os.pathsep)
# print(os.getcwd())
# os.system('calc')
# stat = os.stat('d:/abc.txt')
# print(stat)
# print(stat.st_size)
# import datetime
# print(datetime.datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S'))
# print(os.path.abspath('.'))
# print(os.path.basename('d:/python-demo/demo02/d01.py'))
# print(os.path.dirname('d:/python-demo/demo02/d01.py'))
# print(os.path.exists('d:/abc.txt'))
# print(os.path.exists('d:/abx.txt'))
# print(os.path.getctime('d:/abc.txt'))
# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getctime('d:/abc.txt'))))
# print(os.path.getmtime('d:/abc.txt'))
# print(os.path.isdir('d:/'))
# print(os.path.isdir('d:/abc.txt'))
# print(os.path.join('d:','abc.txt'))
# print(os.path.join('d:/','abc.txt'))
# print(os.path.split('d:/abc/ab.txt'))
# print(os.path.split('d:/abc/ab'))
# print(os.path.split('d:/abc/ab/'))
# pprint.pprint(os.listdir('d:/'))

# 递归地遍历一个文件夹
# def cursiveScan(path):
# 	if os.path.isdir(path):
# 		L = os.listdir(path)
# 		for p in L:
# 			for f in cursiveScan(os.path.join(path,p)):
# 				yield f
# 	else:
# 		yield path

# diriter = cursiveScan('d:/githome')

# for f in diriter:
# 	print(f)

# 递归删除文件夹
# def cursiveDelete(path):
# 	if os.path.isdir(path):
# 		L = [os.path.join(path,x) for x in os.listdir(path)]
# 		for f in L:
# 			cursiveDelete(f)
# 		os.rmdir(path)
# 	else:
# 		os.remove(path)

# cursiveDelete('d:/x')

# for f in os.walk('d:/githome',topdown=False):
# 	print(f)

# t = (1,[2,3])
# print(t)

# shutil 高级文件操作模块
# import shutil
# import pprint
# pprint.pprint(dir(shutil))
# print(shutil.__doc__)
# print(shutil.copyfile.__doc__)
# print(shutil.copyfile('d:/abc.txt','d:/xxxxxxxxxxxxxxxxxxx.txt'))
# print(shutil.copyfile('d:/abc.txt','d:/yyy/')) #第二个参数不能诶目录
# print(shutil.move('d:/abc.txt','d:/abcc.txt'))

# import glob
# import pprint
# pprint.pprint(dir(glob))
# print(glob.__doc__)
# # print(glob.glob('*.py'))
# print(glob.glob('*'))

# import re
# pat = re.compile(r'\d+')
# text = 'a1b23 614s'
# for match in pat.finditer(text):
# 	print(match.group())
# 	print(match.start())
# 	print(match.end())
# 	print(match.span())

# import math
# import pprint
# pprint.pprint(dir(math))
# print(math.__doc__)
# print(math.sin(math.pi/6))

# import random
# import pprint
# # pprint.pprint(dir(random))
# # print(random.__doc__)
# print(random.random())
# print(random.choice(['Jack','Rose','Tim']))
# L = list(range(10))
# random.shuffle(L)
# print(L)
# print(random.sample(range(10),3))


# 统计模块
# import statistics
# print(statistics.mean([1,2,3,4])) #算术平均值
# 调和平均值
#he harmonic mean of three values a, b and c will be equivalent to 3/(1/a + 1/b + 1/c).
# print(statistics.harmonic_mean([1,2,3,4])) 
# 中值
# print(statistics.median([1,2,3,4]))
# print(statistics.median([1,2,3]))
# 众数 mode
# print(statistics.mode([1, 1, 2, 3, 3, 3, 3, 4]))
# 众数不存在时抛statistics.StatisticsError:
# print(statistics.mode([1, 2, 3]))
# 方差
# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.variance(data))
# import math
# print(math.sqrt(statistics.variance(data)))
# print(statistics.pvariance(data))
# print(statistics.pstdev(data))

# import urllib.request
# import re
# with urllib.request.urlopen('http://www.baidu.com') as response:
# 	data = response.read()
# 	data_str = data.decode('utf-8')
# 	pat = re.compile(r'\b\S*百度\S*\b')
# 	for m in pat.finditer(data_str):
# 		print(m.group())
# 		print(m.span())

# 根据出生日期计算你活了多少天
# import datetime
# birth = datetime.date(1994,12,8)
# now = datetime.date.today()
# print(now-birth)
# print(22*365)


# 数据压缩与解压模块 : zlib, gzip, bz2, lzma, zipfile and tarfile
# import zlib
# data = 'dakfdjfkadfa你好dafaaaaaaaadakfdjfkadfa你好dafaaaaaaaadakfdjfkadfa你好dafaaaaaaaa'.encode('utf-8')
# print(len(data))
# compressed_data = zlib.compress(data) #第二个参数课可以指定压缩解绑 0~9 默认为-1
# print(len(compressed_data))
# decompressed_data = zlib.decompress(compressed_data)
# print(decompressed_data.decode('utf-8'))

# 性能测试
# from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b,a', 'a=1; b=2').timeit())


# from string import Template
# import os.path
# import time

# class BatchRename(Template):
# 	delimiter = '%'


# photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
# date = time.strftime('%Y%m%d')
# fmt = input('Enter the format(%n:number,%t:date,%f:format):')
# brt = BatchRename(fmt)
# for i,filename in enumerate(photofiles):
# 	name,ext = os.path.splitext(filename)
# 	newFilename = brt.substitute(n=i,t=date,f=ext)
# 	print('{} -> {}'.format(filename,newFilename))


# import struct

# with open('m01.zip','rb') as f:
# 	data = f.read()

# start = 0
# # show the first 2 file header
# for i in range(2):
# 	start += 14
# 	#H：2字节无符号整数 I：4字节无符号整数 <:小端
# 	fields = struct.unpack('<IIIHH',data[start:start+16])
# 	crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

# 	start += 16
# 	filename = data[start:start+filenamesize]
# 	start += filenamesize
# 	extra = data[start:start+extra_size]
# 	print(filename,hex(crc32),comp_size,uncomp_size)
# 	start += extra_size + comp_size


# import threading, zipfile

# class AsyncZip(threading.Thread):
# 	def __init__(self,infile,outfile):
# 		super().__init__()
# 		self.infile = infile
# 		self.outfile = outfile

# 	def run(self):
# 		f = zipfile.ZipFile(self.outfile,'w',zipfile.ZIP_DEFLATED)
# 		f.write(self.infile)
# 		f.close()
# 		print('Finished background zip of: ',self.infile)

# background = AsyncZip('t01.txt','t01.zip')
# background.start()
# print('The main program continues to run in foreground')
# background.join()
# print('Main program waited until background was done')


# 日志 模块
# 默认输出到sys.stderr 级别为warning 
# import logging
# logging.debug('Debugging information')
# logging.info('Informational mesasge')
# logging.warning('Warning:config file %s not found','server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')

# 输出日志到文件
#默认以追加模式写 覆盖写请设置参数filemode='w'
# logging.basicConfig(filename='example.log',level=logging.DEBUG) 
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')

# 动态设置日志级别
# level = input('Enter log level: ')
# numeric_level = getattr(logging,level.upper())
# if isinstance(numeric_level,int):
# 	logging.basicConfig(filename='example.log',level=numeric_level,filemode='w')
# logging.debug('Debugging information')
# logging.info('Informational mesasge')
# logging.warning('Warning:config file %s not found','server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')

# 设置日志输出的格式
# fmt = '%(asctime)s %(filename)s %(funcName)s %(levelname)s:%(message)s'
# logging.basicConfig(filename='example.log',level=logging.INFO,filemode='w',format=fmt)
# # 自定义日期格式
# datefmt='%m/%d/%Y %I:%M:%S %p'
# logging.basicConfig(filename='example.log',level=logging.INFO,filemode='w',format=fmt,datefmt=datefmt)
# logging.debug('Debugging information')
# logging.info('Informational mesasge')
# logging.warning('Warning:config file %s not found','server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')

# 通常是创建一个指定名称的日志处理器
# logger = logging.getLogger(__name__)
# 配置logger的方法
# logger.setLevel(logging.INFO)
# 添加处理器
# logger.addHandler()
# 添加过滤器
# logger.addFilter()

# print(type(logger))
# logger.info('info log')
# logger.warning('warning log')


# import logging

# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)

# sh = logging.StreamHandler()
# sh.setLevel(logging.DEBUG)

# fh = logging.FileHandler('fh01.txt',mode='w',encoding='utf-8')
# fh.setLevel(logging.WARNING)

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# sh.setFormatter(formatter)
# fh.setFormatter(formatter)

# logger.addHandler(sh)
# logger.addHandler(fh)

# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')


# import logging
# import logging.config
# # 从文件配置日志器
# logging.config.fileConfig('logging.config')

# # create logger
# logger = logging.getLogger('simpleExample')

# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')

# 虚引用
# import weakref, gc
# class A:
#     def __init__(self, value):
#         self.value = value
#     def __repr__(self):
#         return str(self.value)
# a = A(10)                   # create a reference
# d = weakref.WeakValueDictionary()
# d['primary'] = a            # does not create a reference
# print(d['primary'])              # fetch the object if it is still alive
# del a                       # remove the one reference
# gc.collect()                # run garbage collection right away
# print(d['primary'])              # entry was automatically removed


# from array import array
# # 第一个参数H表示以2字节无符号整数存储
# a = array('H',[400,10,700,222])
# print(type(a))
# print(a)
# print(a[1:3])

# import bisect
# scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
# bisect.insort(scores, (300, 'ruby'))
# print(scores)

# 精确的浮动数计算
# from decimal import *

# d1 = Decimal('0.7')
# d2 = Decimal('1.05')
# d3 = d1 * d2
# print(d3)
# print(str(d3))
# print(round(d3,2))
# print(round(0.7*1.05,2))

# print(Decimal('1.0') % Decimal('0.1'))
# print(1.0 % 0.1)

# print(sum([Decimal('0.1')]*10) == 1)
# print(sum([0.1]*10) == 1)

# getcontext().prec = 36
# print(Decimal('1') / Decimal('7'))
# python基础教程 学习进度 at page 271

# sys模块
# sys模块用于访问与python解释器紧密相关的函数，变量，对象等
# import sys
# print(sys.__doc__)

# sys.path  搜寻模块的目录列表 第一项为当前目录
# print(sys.path)

# sys.argv  命令行参数列表 第一项为文件名
# print(sys.argv)

# sys.modules 映射当前已加载的模块的模块名到模块的字典
# print(sys.modules)
# for name,module in sys.modules.items():
# 	print(name,'->',module)

# sys.platform 系统平台信息
# print(sys.platform)
# sys.version python解释器版本
# print(sys.version)

# sys.exit([arg]) 退出当前程序 
# print(sys.exit.__doc__)
# while True:
# 	s = input('Enter instruction: ')
# 	if s == 'exit':
# 		sys.exit()
# 	else:
# 		print('Hello',s)

# 类文件流对象
# sys.stdin
# sys.stdout
# sys.stderr
# print(sys.stdin)
# print(sys.stdout)
# print(sys.stderr)
# print('write text to stderr',file=sys.stderr)


# os模块
# import os
# print(os.__doc__)

# os.environ 系统环境变量的映射
# print(os.environ)
# print(os.environ['path'])
# print(os.environ['classpath'])

 # - all functions from posix or nt, e.g. unlink, stat, etc.
 # - os.path is either posixpath or ntpath
 # - os.name is either 'posix' or 'nt'
 # - os.curdir is a string representing the current directory (always '.'
 # - os.pardir is a string representing the parent directory (always '..'
 # - os.sep is the (or a most common) pathname separator ('/' or '\\')
 # - os.extsep is the extension separator (always '.')
 # - os.altsep is the alternate pathname separator (None or '/')
 # - os.pathsep is the component separator used in $PATH etc
 # - os.linesep is the line separator in text files ('\r' or '\n' or '\r\
 # - os.defpath is the default search path for executables
 # - os.devnull is the file path of the null device ('/dev/null', etc.)

# print(os.name)
# os.sep 目录分割符
# print(os.sep) 
# os.linesep 行分割符
# print(repr(os.linesep))
# os.pathsep 路径分割符
# print(os.pathsep)

# os.system(command)
# 启动windows自带的计算器程序
# os.system('calc')

# 使用浏览器打开指定网站的方法
# import webbrowser
# webbrowser.open('http://www.baidu.com/')


# topdown为True则为广度优先遍历 为False为深度优先
# import os
# from os.path import join, getsize
# for root, dirs, files in os.walk('d:\\python-demo\\demo02',topdown=True ):
#     # print(root, "consumes", end=" ")
#     # print(sum(getsize(join(root, name)) for name in files), end=" ")
#     # print("bytes in", len(files), "non-directory files")
#     print(root)
#     print(dirs)
#     print(files)
#     print('*'*30)

# fileinput 模块
# import fileinput
# print(fileinput.__doc__)
# This iterates over the lines of all files listed in sys.argv[1:],
# defaulting to sys.stdin if the list is empty.  If a filename is '-' it
# for line in fileinput.input():
# 	print('lineno:{}, filelineno:{}'.format(fileinput.lineno(),fileinput.filelineno()))
# 	print(line,end='')

# 为文件添加行号 格式为 原文本行 #行号
# for line in fileinput.input(inplace=True):
# 	line = line.rstrip()
# 	num = fileinput.filelineno()
# 	print('{:s} #{:d}'.format(line,num))


# heapq 模块 实现堆的数据结构
# import heapq
# import random
# print(heapq.__doc__)
# heap = []            # creates an empty heap
# heappush(heap, item) # pushes a new item on the heap
# item = heappop(heap) # pops the smallest item from the heap
# item = heap[0]       # smallest item on the heap without popping it
# heapify(x)           # transforms list into a heap, in-place, in linear time
# item = heapreplace(heap, item) # pops and returns smallest item, and adds
#                                # new item; the heap size is unchanged

# heap = []
# L = list(range(10))
# random.shuffle(L)
# print(L)
# for x in L:
# 	heapq.heappush(heap,x)
# print(heap)

# 使用堆对序列排序
# from heapq import *
# def heapsort(iterable):
# 	h = []
# 	for value in iterable:
# 		heappush(h, value)
# 	return [heappop(h) for i in range(len(h))]
# import random
# L = []
# for i in range(10):
# 	L.append(random.randint(1,100))
# print(L)
# print(heapsort(L))



# string模块
# import string

# s = 'The quick brown fox jumped over the lazy dog.'
# print(s)
# print(string.capwords(s))

# values = {'var':'foo'}
# t = string.Template('''
# Variable 			:$var
# Escape 				:$$
# Variable in text 	:${var}iable
# ''')
# print('template:')
# print(t.substitute(values))

# s = '''
# Variable 			:%(var)s
# Escape 				:%%
# Variable in text 	:%(var)siable
# '''
# print('interpolation:')
# print(s % values)

# s = '''
# Variable 			:{var}
# Escape 				:{{}}
# Variable in text 	:{var}siable
# '''
# print('format')
# print(s.format(**values))

# t = string.Template("$var is here but $missing is not provided")
# try:
# 	print(t.substitute(values))
# except KeyError as err:
# 	print('Error',err)
# print(t.safe_substitute(values))

# 自定义字符串模板
# class MyTemplate(string.Template):
#     delimiter = '%'
#     idpattern = '[a-z]+_[a-z]+'


# template_text = '''
#   Delimiter : %%
#   Replaced  : %with_underscore
#   Ignored   : %notunderscored
# '''

# d = {
#     'with_underscore': 'replaced',
#     'notunderscored': 'not replaced',
# }

# t = MyTemplate(template_text)
# print('Modified ID pattern:')
# print(t.safe_substitute(d))


# t = string.Template('$var')
# print(t.pattern)
# print(t.pattern.pattern)

# import re
# import string


# class MyTemplate(string.Template):
#     delimiter = '{{'
#     pattern = r'''
#     \{\{(?:
#     (?P<escaped>\{\{)|
#     (?P<named>[_a-z][_a-z0-9]*)\}\}|
#     (?P<braced>[_a-z][_a-z0-9]*)\}\}|
#     (?P<invalid>)
#     )
#     '''


# t = MyTemplate('''
# {{{{
# {{var}}
# ''')

# print('MATCHES:', t.pattern.findall(t.template))
# print('SUBSTITUTED:', t.safe_substitute(var='replacement'))


# import inspect
# import string


# def is_str(value):
#     return isinstance(value, str)


# for name, value in inspect.getmembers(string, is_str):
#     if name.startswith('_'):
#         continue
#     print('%s=%r\n' % (name, value))

# print(string.ascii_letters)


# textwrap模块 文本段落处理
# import textwrap

# sample_text = '''
#     The textwrap module can be used to format text for output in
#     situations where pretty-printing is desired.  It offers
#     programmatic functionality similar to the paragraph wrapping
#     or filling features found in many text editors.
#     '''
# print(sample_text)

# s = textwrap.fill(sample_text,width=50)
# print(s)

# s = textwrap.dedent(sample_text)
# print(s)

# dedented_text = textwrap.dedent(sample_text).strip()
# for width in [45, 60]:
#     print('{} Columns:\n'.format(width))
#     print(textwrap.fill(dedented_text, width=width))
#     print()

# dedented_text = textwrap.dedent(sample_text)
# wrapped = textwrap.fill(dedented_text, width=50)
# wrapped += '\n\nSecond paragraph after a blank line.'
# final = textwrap.indent(wrapped, '> ')

# print('Quoted block:\n')
# print(final)


# def should_indent(line):
#     print('Indent {!r}?'.format(line))
#     return len(line.strip()) % 2 == 0


# dedented_text = textwrap.dedent(sample_text)
# wrapped = textwrap.fill(dedented_text, width=50)
# final = textwrap.indent(wrapped, 'EVEN ',
#                         predicate=should_indent)

# print('\nQuoted block:\n')
# print(final)


# dedented_text = textwrap.dedent(sample_text).strip()
# print(textwrap.fill(dedented_text,
#                     initial_indent='',
#                     subsequent_indent=' ' * 4,
#                     width=50,
#                     ))


# dedented_text = textwrap.dedent(sample_text)
# original = textwrap.fill(dedented_text, width=50)

# print('Original:\n')
# print(original)

# shortened = textwrap.shorten(original, 100)
# shortened_wrapped = textwrap.fill(shortened, width=50)

# print('\nShortened:\n')
# print(shortened_wrapped)


# re模块 正则表达式
# import re

# pattern = 'love'
# text = 'you love her,she loves you'

# match = re.search(pattern,text)
# print(dir(match))
# if match:
# 	print('Found "{}" in "{}" at {}~{}'.format(match.re.pattern,match.string,
# 		match.start(),match.end()))
# else:
# 	print('没有匹配到')

# 编译正则表达式

# regexes = [
# 	re.compile(p)
# 	for p in ('this','that')
# ]
# text = 'Does this text match the pattern?'
# for regex in regexes:
# 	print('Seek {} ->'.format(regex.pattern),end=' ')
# 	match = re.search(regex,text)
# 	if match:
# 		print('Match')
# 	else:
# 		print('No match')

# findall 查找所有的匹配
# pattern = r'\d+'
# text = '100+200=300'
# # 返回的是字符串
# for s in re.findall(pattern,text):
# 	print(s)

# he finditer() function returns an iterator 
# that produces Match instances instead of the strings returned by findall().
# pattern = r'(([1-3])\d+)'
# text = '100+200=300'
# for match in re.finditer(pattern,text):
# 	# print(dir(match))
# 	s = match.start()
# 	e = match.end()
# 	print("Found {} at {}~{}".format(text[s:e],s,e))
# 	# 第一种遍历所有匹配组的方式
# 	for i,sub in enumerate(match.groups()):
# 		i += 1
# 		print('分组{}匹配到"{}" at {}~{}'.format(i,sub,match.start(i),match.end(i)))
# 	# 第二种遍历所有匹配组的方式
# 	for i in range(1,len(match.groups())+1):
# 		sub = match.group(i)
# 		print('分组{}匹配到"{}" at {}~{}'.format(i,sub,match.start(i),match.end(i)))


# def test_patterns(text, patterns):
#     """Given source text and a list of patterns, look for
#     matches for each pattern within the text and print
#     them to stdout.
#     """
#     # Look for each pattern in the text and print the results
#     for pattern, desc in patterns:
#         print("'{}' ({})\n".format(pattern, desc))
#         print("  '{}'".format(text))
#         for match in re.finditer(pattern, text):
#             s = match.start()
#             e = match.end()
#             substr = text[s:e]
#             n_backslashes = text[:s].count('\\')
#             prefix = '.' * (s + n_backslashes)
#             print("  {}'{}'".format(prefix, substr))
#         print()
#     return

# 默认为贪婪匹配
# test_patterns(
#     'abbaabbba',
#     [('ab*', 'a followed by zero or more b'),
#      ('ab+', 'a followed by one or more b'),
#      ('ab?', 'a followed by zero or one b'),
#      ('ab{3}', 'a followed by three b'),
#      ('ab{2,3}', 'a followed by two to three b')],
# )

# 非贪婪匹配
# test_patterns(
#     'abbaabbba',
#     [('ab*?', 'a followed by zero or more b'),
#      ('ab+?', 'a followed by one or more b'),
#      ('ab??', 'a followed by zero or one b'),
#      ('ab{3}?', 'a followed by three b'),
#      ('ab{2,3}?', 'a followed by two to three b')],
# )

# 字符类
# test_patterns(
#     'abbaabbba',
#     [('[ab]', 'either a or b'),
#      ('a[ab]+', 'a followed by 1 or more a or b'),
#      ('a[ab]+?', 'a followed by 1 or more a or b, not greedy')],
# )

# 排除特定字符
# test_patterns(
#     'This is some text -- with punctuation.',
#     [('[^-. ]+', 'sequences without -, ., or space')],
# )

# test_patterns(
#     'This is some text -- with punctuation.',
#     [('[a-z]+', 'sequences of lowercase letters'),
#      ('[A-Z]+', 'sequences of uppercase letters'),
#      ('[a-zA-Z]+', 'sequences of letters of either case'),
#      ('[A-Z][a-z]+', 'one uppercase followed by lowercase')],
# )

# . 匹配单个字符 不包括换行符与回车
# test_patterns(
#     'abbaabbba\nbxxx',
#     [('a.', 'a followed by any one character'),
#      ('b.', 'b followed by any one character'),
#      ('a.*b', 'a followed by anything, ending in b'),
#      ('a.*?b', 'a followed by anything, ending in b')],
# )

# test_patterns(
#     'A prime #1 example!',
#     [(r'\d+', 'sequence of digits'),
#      (r'\D+', 'sequence of non-digits'),
#      (r'\s+', 'sequence of whitespace'),
#      (r'\S+', 'sequence of non-whitespace'),
#      (r'\w+', 'alphanumeric characters'),
#      (r'\W+', 'non-alphanumeric')],
# )

# test_patterns(
#     r'\d+ \D+ \s+',
#     [(r'\\.\+', 'escape code')],
# )

# test_patterns(
#     'This is some text -- with punctuation.',
#     [(r'^\w+', 'word at start of string'),
#      (r'\A\w+', 'word at start of string'),
#      (r'\w+\S*$', 'word near end of string'),
#      (r'\w+\S*\Z', 'word near end of string'),
#      (r'\w*t\w*', 'word containing t'),
#      (r'\bt\w+', 't at start of word'),
#      (r'\w+t\b', 't at end of word'),
#      (r'\Bt\B', 't, not start or end of word')],
# )

# text = 'This is some text -- with punctuation.'
# pattern = 'is'

# print('Text   :', text)
# print('Pattern:', pattern)

# # match仅在字符串的起始匹配
# m = re.match(pattern, text)
# print('Match  :', m)
# s = re.search(pattern, text)
# print('Search :', s)


# text = 'This is some text -- with punctuation.'
# pattern = 'is'

# print('Text       :', text)
# print('Pattern    :', pattern)

# m = re.search(pattern, text)
# print('Search     :', m)
# # fullmatch要求完整匹配
# s = re.fullmatch(pattern, text)
# print('Full match :', s)


# 编译的regex的search方法可知道搜素的范围start,end
# 下面用search来实现查找所有的匹配
# text = 'This is some text -- with punctuation.'
# pattern = re.compile(r'\b\w*is\w*\b')

# print('Text:', text)
# print()

# pos = 0
# while True:
#     match = pattern.search(text, pos)
#     if not match:
#         break
#     s = match.start()
#     e = match.end()
#     print('  {:>2d} : {:>2d} = "{}"'.format(
#         s, e - 1, text[s:e]))
#     # Move forward in text for the next search
#     pos = e

# 分组
# test_patterns(
#     'abbaaabbbbaaaaa',
#     [('a(ab)', 'a followed by literal ab'),
#      ('a(a*b*)', 'a followed by 0-n a and 0-n b'),
#      ('a(ab)*', 'a followed by 0-n ab'),
#      ('a(ab)+', 'a followed by 1-n ab')],
# )


# 获取匹配的分组 Match对象的groups方法返回所有分组
# text = 'This is some text -- with punctuation.'

# print(text)
# print()

# patterns = [
#     (r'^(\w+)', 'word at start of string'),
#     (r'(\w+)\S*$', 'word at end, with optional punctuation'),
#     (r'(\bt\w+)\W+(\w+)', 'word starting with t, another word'),
#     (r'(\w+t)\b', 'word ending with t'),
# ]

# for pattern, desc in patterns:
#     regex = re.compile(pattern)
#     match = regex.search(text)
#     print("'{}' ({})\n".format(pattern, desc))
#     print('  ', match.groups())
#     print()

# 获取指定的分组 group(index) 第0个位完整匹配
# text = 'This is some text -- with punctuation.'

# print('Input text            :', text)

# # word starting with 't' then another word
# regex = re.compile(r'(\bt\w+)\W+(\w+)')
# print('Pattern               :', regex.pattern)

# match = regex.search(text)
# print('Entire match          :', match.group(0))
# print('Word starting with "t":', match.group(1))
# print('Word after "t" word   :', match.group(2))

# python扩展了正则表达式的语法 支持命名的分组
# 创建命名分组的语法为 (?P<name>pattern)
# text = 'This is some text -- with punctuation.'

# print(text)
# print()

# patterns = [
#     r'^(?P<first_word>\w+)',
#     r'(?P<last_word>\w+)\S*$',
#     r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
#     r'(?P<ends_with_t>\w+t)\b',
# ]

# for pattern in patterns:
#     regex = re.compile(pattern)
#     match = regex.search(text)
#     print("'{}'".format(pattern))
#     print('  ', match.groups())
#     print('  ', match.groupdict())
#     print()

# def test_patterns2(text, patterns):
#     """Given source text and a list of patterns, look for
#     matches for each pattern within the text and print
#     them to stdout.
#     """
#     # Look for each pattern in the text and print the results
#     for pattern, desc in patterns:
#         print('{!r} ({})\n'.format(pattern, desc))
#         print('  {!r}'.format(text))
#         for match in re.finditer(pattern, text):
#             s = match.start()
#             e = match.end()
#             prefix = ' ' * (s)
#             print(
#                 '  {}{!r}{} '.format(prefix,
#                                      text[s:e],
#                                      ' ' * (len(text) - e)),
#                 end=' ',
#             )
#             print(match.groups())
#             if match.groupdict():
#                 print('{}{}'.format(
#                     ' ' * (len(text) - s),
#                     match.groupdict()),
#                 )
#         print()
#     return

# test_patterns2(
#     'abbaabbba',
#     [(r'a((a*)(b*))', 'a followed by 0-n a and 0-n b')],
# )

# test_patterns2(
#     'abbaabbba',
#     [(r'a((a+)|(b+))', 'a then seq. of a or seq. of b'),
#      (r'a((a|b)+)', 'a then seq. of [ab]')],
# )

# 非获取匹配
# test_patterns2(
#     'abbaabbba',
#     [(r'a((a+)|(b+))', 'capturing form'),
#      (r'a((?:a+)|(?:b+))', 'noncapturing')],
# )

# 忽略大小写
# text = 'This is some text -- with punctuation.'
# pattern = r'\bT\w+'
# with_case = re.compile(pattern)
# without_case = re.compile(pattern, re.IGNORECASE)

# print('Text:\n  {!r}'.format(text))
# print('Pattern:\n  {}'.format(pattern))
# print('Case-sensitive:')
# for match in with_case.findall(text):
#     print('  {!r}'.format(match))
# print('Case-insensitive:')
# for match in without_case.findall(text):
#     print('  {!r}'.format(match))

# text = 'This is some text -- with punctuation.\nA second line.'
# pattern = r'(^\w+)|(\w+\S*$)'
# single_line = re.compile(pattern)
# multiline = re.compile(pattern, re.MULTILINE)

# print('Text:\n  {!r}'.format(text))
# print('Pattern:\n  {}'.format(pattern))
# print('Single Line :')
# for match in single_line.findall(text):
#     print('  {!r}'.format(match))
# print('Multline    :')
# for match in multiline.findall(text):
#     print('  {!r}'.format(match))

# text = 'This is some text -- with punctuation.\nA second line.'
# pattern = r'.+'
# no_newlines = re.compile(pattern)
# dotall = re.compile(pattern, re.DOTALL)

# print('Text:\n  {!r}'.format(text))
# print('Pattern:\n  {}'.format(pattern))
# print('No newlines :')
# for match in no_newlines.findall(text):
#     print('  {!r}'.format(match))
# print('Dotall      :')
# for match in dotall.findall(text):
#     print('  {!r}'.format(match))


# enum 枚举
import enum
# class DayOfWeek(enum.Enum):
# 	sunday = 7
# 	monday = 1
# 	tuesday = 2
# 	wednesday = 3
# 	thursday = 4
# 	friday = 5
# 	saturday = 6
	

# print(type(DayOfWeek.monday)) #<enum 'DayOfWeek'>
# print(isinstance(DayOfWeek.monday,DayOfWeek)) #True
# print(DayOfWeek.monday.name,DayOfWeek.monday.value)

# 遍历枚举
# 按照声明时的顺序遍历
# for dw in DayOfWeek:
# 	print(dw.name,dw.value)

# enum.Enum类型的枚举仅支持 == 与 is 比较运算符
# sun = DayOfWeek.sunday
# sun2 = DayOfWeek.sunday
# mon = DayOfWeek.monday
# print(sun == sun)
# print(sun == sun2)
# print(sun is sun)
# print(sun is sun2)

# print(mon > sun) #TypeError

# 可比较的枚举 enum.IntEnum
# class Nums(enum.IntEnum):
# 	one = 1
# 	two = 2
# 	three = 3
# 	four = 4
# 	five = 5

# for n in Nums:
# 	print(n.name,n.value)

# a = Nums.one
# b = Nums.two
# c = Nums.one

# print(a < b)
# print(a == c)
# print(a is c)

# 相同的值以第一个为准
# class Nums(enum.Enum):
# 	one = 1
# 	two = 2
# 	first = 1

# for n in Nums:
# 	print(n)

# 加上@enum.unique装饰器可以强制枚举值不能重复
# @enum.unique
# class Nums(enum.Enum): #ValueError: duplicate values found in <enum 'Nums'>: first -> one
# 	one = 1
# 	two = 2
# 	first = 1

# 以编程的方式创建枚举
# DayOfWeek = enum.Enum(value='DayOfWeek',names=('mon','tue','wed','thu','fri','sat','sun'))
# print(DayOfWeek.mon)
# for dw in DayOfWeek:
# 	print(dw.name,dw.value)

# DayOfWeek = enum.Enum(value='DayOfWeek',names=('mon tue wed thu fri sat sun'))
# print(DayOfWeek.mon)
# for dw in DayOfWeek:
# 	print(dw.name,dw.value)

# DayOfWeek = enum.Enum(value='DayOfWeek',names=[
# 	('sun',7),('mon',1),('tue',2),('web',3),('thu',4),('fri',5),('sat',6),
# ])
# print(DayOfWeek.mon)
# for dw in DayOfWeek:
# 	print(dw.name,dw.value)

# 复杂的枚举
# class BugStatus(enum.Enum):

#     new = (7, ['incomplete',
#                'invalid',
#                'wont_fix',
#                'in_progress'])
#     incomplete = (6, ['new', 'wont_fix'])
#     invalid = (5, ['new'])
#     wont_fix = (4, ['new'])
#     in_progress = (3, ['new', 'fix_committed'])
#     fix_committed = (2, ['in_progress', 'fix_released'])
#     fix_released = (1, ['new'])

#     def __init__(self, num, transitions):
#         self.num = num
#         self.transitions = transitions

#     def can_transition(self, new_state):
#         return new_state.name in self.transitions


# print('Name:', BugStatus.in_progress)
# print('Value:', BugStatus.in_progress.value)
# print('Custom attribute:', BugStatus.in_progress.transitions)
# print('Using attribute:',
#       BugStatus.in_progress.can_transition(BugStatus.new))


# class BugStatus(enum.Enum):

#     new = {
#         'num': 7,
#         'transitions': [
#             'incomplete',
#             'invalid',
#             'wont_fix',
#             'in_progress',
#         ],
#     }
#     incomplete = {
#         'num': 6,
#         'transitions': ['new', 'wont_fix'],
#     }
#     invalid = {
#         'num': 5,
#         'transitions': ['new'],
#     }
#     wont_fix = {
#         'num': 4,
#         'transitions': ['new'],
#     }
#     in_progress = {
#         'num': 3,
#         'transitions': ['new', 'fix_committed'],
#     }
#     fix_committed = {
#         'num': 2,
#         'transitions': ['in_progress', 'fix_released'],
#     }
#     fix_released = {
#         'num': 1,
#         'transitions': ['new'],
#     }

#     def __init__(self, vals):
#         self.num = vals['num']
#         self.transitions = vals['transitions']

#     def can_transition(self, new_state):
#         return new_state.name in self.transitions


# print('Name:', BugStatus.in_progress)
# print('Value:', BugStatus.in_progress.value)
# print('Custom attribute:', BugStatus.in_progress.transitions)
# print('Using attribute:',
#       BugStatus.in_progress.can_transition(BugStatus.new))