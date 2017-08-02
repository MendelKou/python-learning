# -*- coding: utf-8 -*-
# print("Hello","Tom","Yahioo")
# print("1+2=",1+2)
# name=input()
# name=input("Please enter your name: ")
# print("Hello",name)
# print(1/3)
# print(r'\n\\')
# print(r'''abc
# d\nef
# xxx''')
# print(2<3)
# print(None)
# print(5/2)
# print(5//2)
# a=1;
# b=a;
# a=2;
# print(b)
# print(ord('A'))
# print(chr(65))
# b=b'abc'
# print(b)
# if 2>1:
# 	print(True)
# else:
# 	print(False)
# print(True and False)
# enc = ord('德')
# print(enc)
# print(chr(enc))

# bytes = '李明'.encode('utf-8')
# print(bytes)
# print(bytes.decode('utf-8'))

# print(len('中文'))
# print(len('中文'.encode('utf-8')))

# str = 'name: %s, age: %d, score: %.2f' % ('Tom',23,33.8)
# print(str)

# s1 = 72;
# s2 = 85;
# s = 100*(s2-s1)/s1
# print('%.1f%%' % s)

# students = ['Tom','Jack','Dick',]
# print(students)
# print(len(students))
# print(students[0])
# students.append('Rose')
# students.insert(1,'X01')
# students.insert(0,'X01')
# students.insert(len(students),'Z')
# s = students.pop()
# s = students.pop(1)
# print(s)
# print(students)

# t = (1,)
# t = (1,2,3,)
# t = (1,[2,3])
# print(t)
# t[1][0] = 'xxx'
# print(t)

# if (1,):
# 	print(True)
# else:
# 	print(False)

# h = float(input('身高(单位:m): '))
# w = float(input('体重(单位:kg): '))
# bim = w/(h*h)
# print('bim is %f' % bim)
# if bim<18.5:
# 	print('过轻')
# elif bim<25:
# 	print('正常')6
# elif bim<28:
# 	print('过重')
# elif bim<32:
# 	print('肥胖')
# else:
# 	print('严重肥胖')

# for x in [1,2,3,4]:
# 	print(x)
# print(x)

# print(range(5))
# print(list(range(5)))

# sum = 0;
# for x in range(101):
# 	sum += x
# print(sum)

# info = {'name':'Tom','age':26}
# print(info)
# print(info['name'])
# print('name' in info)
# print(info.get('name'))
# print(info.get('gender') == None)
# print(info.get('gender','未知'))
# print(info.pop('name'))
# print(info)

# myset = set([1,2,3,3])
# print(myset)
# myset.add(4)
# print(myset)
# myset.add((5,6))
# print(myset)

# print(hex(65))

# def my_abs(x):
# 	if x<0:
# 		return -x
# 	else:
# 		return x

# print(my_abs(-1))
# print(my_abs(1))
# print(my_abs('a'))
# print(abs('a'))

# def my_abs(x):
# 	if not isinstance(x,(int,float)):
# 		raise TypeError('bad operand type')
# 	if x<0:
# 		return -x
# 	else:
# 		return x
#
# print(my_abs('a'))

# import math
# def move(x,y,step,angle):
# 	nx = x+step*math.cos(angle)
# 	ny = y+step*math.sin(angle)
# 	return nx,ny
# print(move(0,0,1,math.pi/6))

# import math
# def quadratic(a,b,c):
# 	if a == 0:
# 		raise Error('not quadratic equation')
# 	delta = math.sqrt(b*b-4*a*c)
# 	x1 = (-b+delta)/2
# 	x2 = (-b-delta)/2
# 	# return x1,x2
# 	return {'x1':x1,'x2':x2}
#
# print(quadratic(1,-5,6))

# def power(x,n=2):
# 	r = 1
# 	while n>0:
# 		r *= x
# 		n -= 1
# 	return r
#
# print(power(2,0))
# print(power(2,1))
# print(power(2,2))
# print(power(2))

# def enroll(name,gender,age=18,city='北京'):
# 	print(name,gender,age,city)
# enroll('Jack','male')
# enroll('Rose','male',21)
# enroll('Linda','female',city='四川')
# enroll('Tom','male',22,'上海')

# def add_end(L=[]):
# 	L.append('END')
# 	return L
# print(add_end())
# print(add_end())
# print(add_end())

# def add_end(L=None):
# 	if L == None:
# 		L = []
# 	L.append('END')
# 	return L
# print(add_end())
# print(add_end())
# print(add_end())

# def calc(*numbers):
# 	sum = 0
# 	for num in numbers:
# 		sum += num*num
# 	return sum
#
# print(calc(1))
# print(calc(1,2))
# print(calc(1,2,3))
# print(calc(*[1,2,3]))
# print(calc(*(1,2,3)))

# def person(name,age,**kw):
# 	print('name:',name,'age:',age,'other:',kw)

# person('Tom',23)
# person('Jack',24,gender='男')
# extra = {'isMarried':False,'height':175}
# person('Martin',23,**extra)

# def person(name,age,*,city,job):
# 	print('name:',name,'age:',age,'city:',city,'job:',job)
# person('Tom',22)
# person('Tom',23,city='北京',job='doctor')
# person('Tom',23,city='北京')

# args = ['Jeffery',23]
# kw = {'city':'北京','job':'保洁'}
# person(*args,**kw)

# def hannoi(n,a,b,c):
# 	if n == 1:
# 		print('move %d from %s to %s' % (1,a,c))
# 	else:
# 		hannoi(n-1,a,c,b)
# 		print('move %d from %s to %s' % (n,a,c))
# 		hannoi(n-1,b,a,c)
#
# hannoi(3,'A','B','C')

# list1 = [1,2,3,4,5,6,7];
# list2 = list1[1::2];
# print(list1)
# print(list2)
# list2[0] = 100
# print(list1)
# print(list2)

# t1 = tuple(range(10))
# t2 = t1[1:5]
# print(t1)
# print(t2)

# s1 = 'ABCDEF';
# s2 = s1[1:4]
# print(s1)
# print(s2)

# d = {'a':'apple','b':'banana','c':'cat','d':'donkey'}
# d = [1,2,3,4,5]
# d = (1,2,3,4,5)
# d = 'ABCDEF'
# for key in d:
# 	print(key)

# from collections import Iterable
# print(isinstance([1,2,3],Iterable))
# print(isinstance((1,2,3),Iterable))
# print(isinstance('123',Iterable))
# print(isinstance(123,Iterable)) #False

# L = []
# for i in range(1,11):
# 	L.append(i*i)
# print(L)

# L = [x*x for x in range(1,11)]
# print(L)

# L = [x*x for x in range(1,11) if x % 2 == 0]
# print(L)

# L = [m+n for m in 'ABC' for n in 'XYZ']
# print(L)

# import os
# L = [x for x in os.listdir('d:/')]
# print(L)

# d = {'a':'apple','b':'banana','c':'cat','d':'donkey'}
# for k,v in d.items():
# 	print(k,'=',v)

# d = {'a':'apple','b':'banana','c':'cat','d':'donkey'}
# L = [k+'='+v for k,v in d.items()]
# print(L)

# L = ['World','Apple',18,'Python']
# M = [x.lower() for x in L if isinstance(x,str)]
# print(M)

# g = (x*x for x in range(1,11))
# for v in g:
# 	print(v)

# for v in (x*x for x in range(1,11)):
# 	print(v)

# def fib(n):
# 	a,b = 0,1
# 	while n > 0:
# 		print(b)
# 		a,b = b,a+b
# 		n -= 1

# def fib(n):
# 	a,b = 0,1
# 	while n > 0:
# 		yield b
# 		a,b = b,a+b
# 		n -= 1
#
# for i in fib(10):
# 	print(i)


# def factorial(n):
# 	r = 1
# 	while n > 1:
# 		r *= n
# 		n -= 1
# 	return r
# def combine(m,n):
# 	return factorial(m)//factorial(m-n)//factorial(n)
# def triangles():
# 	m = 0
# 	while True:
# 		yield [combine(m,n) for n in range(0,m+1)]
# 		m += 1
# n = 0
# for L in triangles():
# 	print(L)
# 	if n == 10:
# 		break
# 	n += 1

# from collections import Iterable
# from collections import Iterator
# print(isinstance(range(1,11),Iterable))
# print(isinstance(range(1,11),Iterator))
# print(isinstance(iter(range(1,11)),Iterator))


# def f(x):
# 	return x*x
# r = map(f,[1,2,3,4,5,7])
# # print(list(r))
# for k in r:
# 	print(k)

# print(list(map(str,[1,2,3,4,5,6])))

# from functools import reduce
# def add(x,y):
# 	return x+y
# print(reduce(add,[1,2,3,4,5]))

# from functools import reduce
# def fn(x,y):
# 	return x*10+y
# print(reduce(fn,[6,1,7,4,]))

# from functools import reduce
# def fn(x,y):
# 	return x*10+y
# def char2num(s):
# 	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
# print(reduce(fn,map(char2num,'23478')))

# from functools import reduce
# def str2int(str):
# 	def fn(x,y):
# 		return x*10+y
# 	def char2num(s):
# 		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
# 	return reduce(fn,map(char2num,'23478'))
# print(str2int('16234'))

# from functools import reduce
# def str2int(str):
# 	def char2num(s):
# 		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
# 	return reduce(lambda x,y:x*10+y,map(char2num,'23478'))
# print(str2int('16234'))

# def normalize(name):
	# st = name.upper()[0]
	# name = name.lower()
	# for s in name[1:]:
	# 	st += s
	# return st
# 	return name.capitalize()
# print(list(map(normalize,['tom','jAck'])))

# from functools import reduce
# def prod(L):
# 	return reduce(lambda x,y:x*y,L)
# print(prod([2,3,8]))

# from functools import reduce
# def str2float(s):
# 	def char2num(s):
# 		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
# 	hasDot = s.find('.')
# 	if(hasDot == -1):
# 		return reduce(lambda x,y:x*10+y,map(char2num,s))
# 	elif hasDot == len(s)-1:
# 		return reduce(lambda x,y:x*10+y,map(char2num,s[:hasDot]))
# 	else:
# 		s2 = s[hasDot+1:]
# 		s2 = s2[::-1]+'0'
# 		p1 = reduce(lambda x,y:x*10+y,map(char2num,s[:hasDot]))
# 		p2 = reduce(lambda x,y:x/10+y,map(char2num,s2))
# 		return p1+p2
#
# print(str2float('123.456'))
# print(str2float('123.4'))
# print(str2float('123.'))
# print(str2float('1'))

# from functools import reduce
# def ch2num(ch):
# 	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':-1}[ch]
# def str2float(s):
# 	nums = map(ch2num,s)
# 	point = 0
# 	def to_float(a,b):
# 		nonlocal point
# 		if b == -1:
# 			point = 1
# 			return a
# 		if point == 0:
# 			return a*10+b
# 		point = point*10
# 		return a+b/point
# 	return reduce(to_float,nums)
# print(str2float('123.456'))
# print(str2float('123.4'))
# print(str2float('123.'))
# print(str2float('1'))

# L = list(range(1,8))
# # def is_even(n):
# #     return n % 2 == 0
# # L2 = filter(is_even,L)
# L2 = filter(lambda x: x % 2 == 0,L)
# print(list(L2))

# # 构造一个从3开始的奇数生成器
# def odd_iter():
#     n = 3
#     while True:
#         yield n
#         n += 2
# #返回一个筛选函数
# def not_divisible(n):
#     return lambda x: x % n != 0
# # 利用筛选法构造素数生成器
# def primes():
#     yield 2
#     it = odd_iter();
#     while True:
#         n = next(it) #返回生成的下一个数
#         yield n
#         it = filter(not_divisible(n),it) #过滤掉被n整除的数
#
# i = 0
# for n in primes():
#     print(n)
#     i += 1
#     if(i == 10):
#         break

#过滤回数
# def is_palindrome(n):
#     s1 = str(n)
#     s2 = s1[::-1]
#     return s1 == s2
# print(list(filter(is_palindrome,range(1,1001))))

# list1 = [1,87,23,678,111];
# list2 = sorted(list1)
# list2 = sorted(list1,reverse=True) #逆序排列
# list2 = sorted(list1,key=str) #按字符串排序
# print(list2)

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0]
# def by_score(t):
#     return t[1]
# # L2 = sorted(L,key=by_name)
# L2 = sorted(L,key=by_score)
# print(L2)

# def lazy_sum(*args):
#     def sum():
#         s = 0
#         for v in args:
#             s += v
#         return s
#     return sum
#
# f = lazy_sum(1,2,3,4,5)
# print(f)
# print(f())

# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
# f1,f2,f3 = count()
# print(f1(),f2(),f3())
#
# def count():
#     fs = []
#     def fn(j):
#         def fm():
#             return j*j
#         return fm
#     for i in range(1,4):
#         fs.append(fn(i))
#     return fs
# f1,f2,f3 = count()
# print(f1(),f2(),f3())

# def log(func):
#     def wrapper(*arg,**kw):
#         print('call %s():' % func.__name__)
#         return func(*arg,**kw)
#     return wrapper
# @log #相当于执行了f = log(f)
# def f():
#     print('2017-07-20')
# f()

# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func) #防止函数的__name__改变为wrapper
#         def wrapper(*args,**kw):
#             print('%s %s' % (text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def f():
#     print('abc')
# f()
# print(f.__name__)

# print(int('101'))
# print(int('101',base=2))

# import sys
# def test():
#     args = sys.argv
#     if len(args) == 1:
#         print("Hello World")
#     elif len(args) == 2:
#         print("Hello %s" % args[1])
#     else:
#         print("Too many arguments")
# test()

# import sys
# print(sys.path)

# 图片压缩 需要安装Pillow模块
# from PIL import Image
# im = Image.open('1.jpg')
# print(im.format,im.size,im.mode)
# im.thumbnail((300,200))
# im.save('1-1.jpg','JPEG')


# class Student(object):
# 	def __init__(self,name,score):
# 		self.name = name
# 		self.score = score
# 	def print_score(self):
# 		#print('%s=%d' % (self.name,self.score))
# 		print('{} scored {}'.format(self.name,self.score))
#
# tom = Student('Tom',96)
# jack = Student('Jack',90)
# tom.print_score()
# jack.print_score()

# a = Student('A',1)
# b = Student('B',2)
# a.age = 20
# # print(a.age)
# print(b.age)

# class Person(object):
# 	def __init__(self,name,gender):
# 		self.__name = name
# 		self.__gender = gender
# 	def to_str(self):
# 		print(self.__name,self.__gender)
#
# p = Person('Tom',23)
# # p.to_str()
# # print(p.__name) #AttributeError: 'Person' object has no attribute '__name'
# print(p._Person__name)

# class Animal(object):
# 	def run(self):
# 		print('Animal is running')
# class Dog(Animal):
# 	pass
# class Cat(Animal):
# 	pass
#
# dog = Dog()
# cat = Cat()
# dog.run()
# cat.run()

# class Animal(object):
# 	def run(self):
# 		print('Animal is running')
# class Dog(Animal):
# 	def run(self):
# 		print('Dog is running')
# class Cat(Animal):
# 	def run(self):
# 		print('Cat is running')
# animal = Animal()
# dog = Dog()
# cat = Cat()
# # animal.run()
# # dog.run()
# # cat.run()
# print(isinstance(dog,Animal))
# print(isinstance(cat,Animal))

# def let_run(obj):
# 	obj.run()
# let_run(animal)
# let_run(dog)
# let_run(cat)
#
# class Some(object):
# 	def run(self):
# 		print('some run')
# let_run(Some())

# print(type([]))
# print(type({}))
# print(type({1,2,3}))
# print(type(set([])))
# print(type('abc'))
# print(type(1))
# print(type(1.5))

# def f():
#     pass
# print(type('abc') == str)
# print(type(123) == int)
# print(type(2.5) == float)
# print(type(f))
# print(type(abs))
# print(type(lambda x: x*x))
# print(type(x for x in range(10)))

# import types
# print(type(f) == types.FunctionType)
# print(type(abs) == types.BuiltinFunctionType)
# print(type(lambda x: x*x) == types.LambdaType)
# print(type(x for x in range(10)) == types.GeneratorType)

# print(dir('a'))
# print(dir(f))
# print(len('abc'))
# print('abc'.__len__())

# class Dog(object):
#     def __len__(self):
#         return 1000
# dog = Dog()
# # print(len(dog))
# print(dog.__len__())

# class Dog(object):
#     def __init__(self):
#         self.name = 'Jam'
#         print('调用了__init__方法')
#     def f(self):
#         print(self.name)
# dog = Dog()
# dog2 = Dog()
# print(hasattr(dog,'name'))
# print(hasattr(dog,'age'))
# print(getattr(dog,'name'))
# print(getattr(dog,'age')) #AttributeError
# print(getattr(dog,'age',404))
# setattr(dog,'age',20)
# print(getattr(dog,'age'))
# print(hasattr(dog,'f'))
# print(getattr(dog,'f'))
# g = getattr(dog,'f')
# g()

# class Student(object):
#     name = 'Stu'
# obj = Student()
# print(obj.name)
# print(Student.name)
# obj.name = 'Stud'
# print(obj.name)
# print(Student.name)
# del obj.name
# print(obj.name)
# print(Student.name)

# class Student(object):
#     pass
# s = Student()
# s2 = Student()
# s.name = 'Tom'
# print(s.name)
# def set_age(self,age):
#     self.age = age
# from types import MethodType
# print(set_age)
# print(MethodType(set_age,s))
# s.set_age = MethodType(set_age,s) #给该实例绑定一个方法 仅对该实例有效
# s.set_age(23)
# print(s.age)
# 通过给class绑定方法以让所有实例可用
# Student.set_age = set_age
# s.set_age(20)
# s2.set_age(30)
# print(s.age)
# print(s2.age)

# 通过在类内定义__slots__来限制对象允许绑定的属性
# class Person(object):
#     __slots__ = ('name','gender')
#
# p = Person()
# p.name = 'Tom'
# p.gender = 'male'
# # p.age = 23
# print(p)
# print(dir(p))
# print(p.__dir__())

#父类的__slots__对子类没有限制
# class Person(object):
#     __slots__ = ['name','gender']
# class Student(Person):
#     pass
# p = Person()
# p.name = 'Tom'
# # p.age = 12
# s = Student()
# s.name = 'Rose'
# s.score = 90
# print(s.score)

# class Student(object):
#     def set_score(self,score):
#         if not isinstance(score,int):
#             raise TypeError('score must be integer')
#         if score < 0 or score > 100:
#             raise ValueError('score must between 1~100')
#         self.__score = score
#     def get_score(self):
#         return self.__score
# s = Student()
# s.set_score(23)
# print(s.__score)
# print(s._Student__score)
# s.set_score('abc')
# s.set_score(101)
# s.set_score(90)
# print(s.get_score())

# class Student(object):
#     #score属性的读方法
#     @property
#     def score(self):
#         return self.__score
#     #score属性的写方法
#     @score.setter
#     def score(self,score):
#         if not isinstance(score,int):
#             raise TypeError('score must be integer')
#         if score < 0 or score > 100:
#             raise ValueError('score must between 1~100')
#         self.__score = score
#     #只读属性
#     @property
#     def a(self):
#         return 'a'
# s = Student()
# # s.score = 'abc'
# # s.score = 101
# # s.score = 50
# # print(s.score)
# # s.a = 'b'
# print(s.a)

# class Animal(object):
#     def breathe(self):
#         print('动物呼吸')
# class Mammal(Animal):
#     def breed(self):
#         print('哺乳动物胎生')
# class Bird(Animal):
#     def breed(self):
#         print('鸟类卵生')
# class Flyable(Animal):
#     def run(self):
#         print('会飞')
# class Runnable(Animal):
#     def run(self):
#         print('会跑')
#
# class Dog(Mammal,Runnable):
#     pass
# class Bat(Mammal,Flyable):
#     pass
# class Ostrich(Bird,Runnable):
#     pass
# class Sparrow(Bird,Flyable):
#     pass
# dog = Dog()
# dog.breathe()
# dog.breed()
# dog.run()
# bat = Bat()
# ostrich = Ostrich()
# sparrow = Sparrow()

# class Person(object):
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return self.name
#     #repr用于调试 通常与__str__返回相同
#     # def __repr__(self):
#     #     return self.name
#     #简便写法
#     __repr__ = __str__
# p = Person('Tom')
# print(p)
# print(p.__repr__())

# class Fin(object):
#     def __init__(self,max):
#         self.max = max
#         self.a,self.b = 0,1
#     #返回迭代器
#     def __iter__(self):
#         return self
#     #返回下一个值
#     def __next__(self):
#         self.a,self.b = self.b,self.a+self.b
#         if self.a<=self.max:
#             return self.a
#         raise StopIteration()
#
# for n in Fin(10):
#     print(n)

# class Fin(object):
#     def __getitem__(self,n):
#         self.a,self.b = 0,1
#         for i in range(n):
#             self.a,self.b = self.b,self.a+self.b
#         return self.b
# fib = Fin()
# print(fib[0])
# print(fib[1])
# print(fib[2])
# print(fib[3])
# print(fib[4])
# print(fib[5])

# class Fin(object):
#     def __getitem__(self,n):
#         if isinstance(n,int):
#             a,b = 1,1
#             for i in range(n):
#                 a,b = b,a+b
#             return a
#         if isinstance(n,slice):
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             print('start=',start)
#             print('stop=',stop)
#             L = []
#             a,b = 1,1
#             for i in range(stop):
#                 if i >= start:
#                     L.append(a)
#                 a,b = b,a+b
#             return L
#
# fib = Fin()
# # for i in range(10):
# #     print(fib[i])
# # L = fib[2:9]
# L = fib[:9]
# for i in L:
#     print(i)

# class Student(object):
#     def __init__(self,name):
#         self.name = name
#     def __getattr__(self,name):
#         print('属性',name,'不存在')
#         if name == 'score':
#             return 90
#         if name == 'age':
#             return lambda : 25
# s = Student('Tom')
# print(s.name)
# print(s.score)
# print(s.gender)
# print(s.age())

# class Chain(object):
#     def __init__(self,path):
#         self.__path = path
#     def __getattr__(self,name):
#         def concat(param=None):
#             if param == None or param == '':
#                 return Chain(str.format('{0}/{1}',self.__path,name))
#             else:
#                 return Chain(str.format('{0}/{1}',self.__path,param))
#         return concat
#     def __str__(self):
#         return self.__path
# print(Chain('user').home().work('xyz').tom())

# class Student(object):
#     def __init__(self,name):
#         self.__name = name
#     def __call__(self):
#         return self.__name
# s = Student('Tom')
# print(s())
# print(callable(s))

# from enum import Enum
# Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
# 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# print(Month.Jan)
# print(Month.Jan.value)
# print(Month.Jan.name)
# m1 = Month.Jan
# m2 = Month.Jan
# print(m1 == m2)
# for m in Month:
#     print(m,m.name,m.value)
# for name,member in Month.__members__.items():
#     print(name,member,member.value)

# from enum import Enum,unique
# @unique #@unique装饰器可以帮助我们检查保证没有重复值
# class Weekday(Enum):
#     Sun = 0 #Sun的value被设置为0 默认从1开始
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
# day1 = Weekday.Mon
# print(day1)
# print(day1 == Weekday.Mon)
# print(Weekday.Mon)
# print(Weekday.Mon.name)
# print(Weekday.Mon.value)
# print(Weekday['Mon'])
# print(Weekday['Mon'].value)
# print(Weekday['Mon'].name)
# print(Weekday(1))
# print(Weekday(1) == Weekday.Mon)

# type函数不仅可以返回对象的类型 还可以创建一个新的类型
# 先定义函数
# def fn(self,name='World'):
#     print(str.format('Hello {0:s}',name))
# Hello = type('Hello',(object,),dict(hello=fn))
# h = Hello()
# h.hello()
# print(type(Hello))
# print(type(h))

# class ListMetaclass(type):
#     def __new__(cls,name,bases,attrs):
#         # print(cls,name,bases,attrs)
#         attrs['add'] = lambda self,value:self.append(value)
#         return type.__new__(cls,name,bases,attrs)
#
# class MyList(list,metaclass=ListMetaclass):
#     pass
# L = MyList()
# L.add(1)
# print(L)

# import logging
# try:
#     print('try...')
#     r = 10 / 0
#     print('result:',r)
# except ZeroDivisionError as e:
#     # print('except:',e)
#     logging.exception(e)
# finally:
#     print('finally...')
# print('END')

# def foo(s):
#     return 10/int(s)
# def bar(s):
#     return foo(s)*2
# def main():
#     return bar('0')
# main()

# class FooError(ValueError):
#     pass
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError(str.format('Invalid value {0}',s))
#     return 10/n
# print(foo('0'))

# def foo(s):
#     n = int(s)
#     if n ==0:
#         assert n != 0,'n is zero'
#     return 10/n
# print(foo('0'))

# import logging
# logging.basicConfig(level=logging.INFO)
# def foo(s):
    # n = int(s)
#     logging.info(str.format('n={0}',n))
    # return 10/n
# print(foo('0'))

# import pdb
# def foo(s):
#     n = int(s)
#     pdb.set_trace() #设置一个断点
#     return 10/n
# print(foo('0'))

# 自定义一个可以通过属性访问元素的dict
# class Dict(dict):
#     def __init__(self,**kw):
#         super().__init__(**kw)
#     def __getattr__(self,key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError('Dict has no attribute %s' % key)
#     def __setattr__(self,key,value):
#         self[key] = value
# d = Dict(name='Tom')
# print(d['name'])
# print(d.name)

#文件IO操作
# f = None
# try:
#     f = open('d:/abc.txt','r')
#     str = f.read()
#     print(str)
# finally:
#     if f:
#         f.close()

# with语句会自动调用close方法
# with open('d:/abc.txt','r') as f:
#     str = f.read()
#     print(str)

# f = None
# try:
#     # f = open('d:/abc.txt','r')
#     # f = open('d:/abc.txt','r',encoding='gbk',errors='ignore')
#     f = open('d:/abc.txt','rb')
#     while True:
#         # s = f.read(10)
#         s = f.readline() #每次读取一行
#         # s = s.rstrip() #去掉右边的空白字符
#         # print(type(s)) #class str
#         if len(s) == 0:
#             break;
#         print(s)
#         print(s.decode('gbk').strip())

    # print(f.readlines())
    # for line in f.readlines():
    #     print(line.rstrip('\n'))
# finally:
#     if f:
#         f.close()

# with open('d:/x01.txt','w') as f:
#     f.write('dkafkd')

#StringIO
# from io import StringIO
#写
# sio = StringIO()
# sio.write('abc')
# sio.write('dfka')
# print(sio.getvalue())

#读
# f = StringIO('adkfdk\nHello\n都卡附近看到')
# while True:
#     s = f.readline()
#     if s != '':
#         print(s.rstrip())
#     else:
#         break

# from io import BytesIO
# bo = BytesIO()
# bo.write('的看法\n'.encode('UTF-8'))
# bo.write('都近看到'.encode('UTF-8'))
# print(bo.getvalue())
# print(bo.getvalue().decode('UTF-8'))

# bo = BytesIO(b'\xe7\x9a\x84\xe7\x9c\x8b\xe6\xb3\x95\n\xe9\x83\xbd\xe8\xbf\x91\xe7\x9c\x8b\xe5\x88\xb0')
# while True:
#     bs = bo.readline()
#     if  len(bs) > 0:
#         print(bs)
#         print(bs.decode('UTF-8').rstrip())
#     else:
#         break

# import os
# print(os.name)
# print(dir(os))
# print(os.environ)
#获取摸个环境变量的值
# print(os.environ.get('JAVA_HOME'))
# print(os.environ.get('xxxx','未知'))

# import os
# 查看当前目录的绝对路径
# print(os.path.abspath(''))
# print(os.path.abspath('.'))
# 合并路径
# print(os.path.join('d:/aaa','def','ccc'))
# 拆分路径
# ps = os.path.split('d:\\aaa\\bbb\ccc\\abc.txt')
# print(ps)
# print(ps[0])
# print(ps[1])
# ps = os.path.splitext('d:\\aaa\\bbb\ccc\\abc.txt')
# print(ps)
# print(ps[0])
# print(ps[1])
# 重命名文件
# os.rename('x02.txt','x01.txt')
# 删除文件
# print(os.remove('x01.txt'))
# import shutil
# 复制文件
# print(shutil.copyfile('.\\P.java','.\\PP.java'))

# import os
# print(os.listdir('.'))
# 列出当前目录下的所有文件名
# for f in os.listdir('.'):
#     # print(type(f))
#     print(f)
# print([x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py'])


# import pickle
# d = {'name':'Tom','age':23,'gender':'male'}
# print(type(d))
# print(d)
#转为为字节
# bs = pickle.dumps(d)
# print(bs)
# 序列化到文件
# with open('./obj.txt','wb') as f:
#     rs = pickle.dump(d,f)
#     print(rs)
# 反序列化
# with open('./obj.txt','rb') as f:
#     # d = pickle.loads(f.read())
#     d = pickle.load(f)
#     print(d)

import json
# d = dict(name='Jack',gender='男',isMarried=True,age=23,weight=75.6,nickname=None)
#返回json字符串
# str = json.dumps(d)
# print(str)
#以json字符串序列化到文件
# with open('./json.txt','w') as f:
#     json.dump(d,f)
#反序列化
# with open('./json.txt','r') as f:
#     # jsn = json.loads(f.read())
#     jsn = json.load(f)
#     print(jsn)
#对象序列化为json
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

# import os
# print(str.format('Process {0} start...',os.getpid()))
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print(str.format('I am a child process {0}, my parent is {1}',os.getpid(),os.getppid()))
# else:
#     print(str.format('I ({0}) created a child process {1}',os.getpid(),pid))

# 跨平台的多进程模块
# from multiprocessing import Process
# import os
# def run_proc(name):
#     print(str.format('child process {0} ({1})',name,os.getpid()))
# if __name__ == '__main__':
#     print(str.format('main process {0}',os.getpid()))
#     #创建子进程 target是进程执行的函数  args是函数参数元组
#     p = Process(target=run_proc,args=('subp01',))
#     #启动进程
#     p.start()
#     #等待p进程执行完毕
#     p.join()
#     print('main process end')

# 进程池
# from multiprocessing import Pool
# import os,time,random
# def random_time_task(name):
#     print(str.format('Run task {0}, pid={1}',name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3+1)
#     end = time.time()
#     print(str.format('Task {0} runs {1} seconds',name,end-start))
# if '__main__' == __name__:
#     print(str.format('Main process, pid={0}',os.getpid()))
#     #创建容量为4的线程池
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(random_time_task,args=(i,))
#     p.close() #调用close后再不能添加进程
#     print('Wait all sub processes done...')
#     p.join() #等待池中的所有进程运行完毕 调用join()之前必须先调用close()
#     print('Main process end')

# 控制子进程的输入输出
# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print(str.format('Exit code: {0}',r))

# import subprocess
# print('$ nslookup')
# p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,
# stderr=subprocess.PIPE)
# output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('gbk'))
# print('Exit code:',p.returncode)

# 进程间通信
# from multiprocessing import Process,Queue
# import os,time,random
# # 读进程执行的函数
# def write(q):
#     for ch in '123456':
#         print(str.format('process {0} writes {1} to queue',os.getpid(),ch))
#         q.put(ch)
#         time.sleep(random.random())
# # 写进程执行的函数
# def read(q):
#     while True:
#         ch = q.get(True)
#         print(str.format('process {0} reads {1} from queue',os.getpid(),ch))
#
# if __name__ == '__main__':
#     # 父进程创建Queue，并传给各个子进程
#     q = Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read,args=(q,))
#     # 启动子进程pw 写入
#     pw.start()
#     # 启动子进程 读取
#     pr.start()
#     # 等待pw结束
#     pw.join()
#     # pr进程是死循环，无法等待其结束，只能强行终止
#     pr.terminate()

# 线程
# import time,random,threading
# def loopThread():
#     print(str.format('Thread {0} start...',threading.current_thread().name))
#     n = 0
#     while n < 5:
#         print(str.format('Thread {0} prints {1}',threading.current_thread().name,n))
#         n += 1
#         time.sleep(random.random())
#     print(str.format('Thread {0} end',threading.current_thread().name))
#
# print(str.format('Main thread {0} start...',threading.current_thread().name))
# t = threading.Thread(target=loopThread,name='LoopThread')
# # print(dir(t))
# t.start()
# t.join()
# print(str.format('Main thread {0} end',threading.current_thread().name))

# 线程共享数据带来的问题
# import threading
# balance = 0
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)
# t1 =threading.Thread(target=run_thread,args=(1,))
# t2 =threading.Thread(target=run_thread,args=(2,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# 锁
# import threading
# balance = 0
# lock = threading.Lock() #创建锁
# def change_it(n):
#     global balance
#     lock.acquire()
#     try:
#         balance += n
#         balance -= n
#     finally:
#         lock.release()
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)
# t1 =threading.Thread(target=run_thread,args=(1,))
# t2 =threading.Thread(target=run_thread,args=(2,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# import threading,multiprocessing
# cpu_count = multiprocessing.cpu_count()
# print(str.format('CPU核心数：{0}',cpu_count))
# def loop():
#     n = 1
#     while True:
#         n = n ^ 1
# for i in range(cpu_count):
#     t = threading.Thread(target=loop)
#     t.start()

# ThreadLocal
# import threading
# # 创建全局的ThreadLocal对象
# local_school = threading.local()
# def process_thread(name):
#     local_school.student = name
#     process_student()
# def process_student():
#     name = local_school.student
#     print(str.format('Hello {0} (in Thread {1})',name,threading.current_thread().name))
# t1 = threading.Thread(target=process_thread,args=('Jack',),name='Thread-A')
# t2 = threading.Thread(target=process_thread,args=('Rose',),name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# 正则表达式
# import re
# s = 'abc123abc'
# reg = r'\d{3,}'
# #match只在开始位置匹配
# # m = re.match(reg,s)
# # search会在整个字符串中查找匹配
# m = re.search(reg,s)
# if m:
#     # print(dir(m))
#     # print('匹配到了',m.group(),',匹配位置：',m.span(),m.start(),m.end())
# else:
#     print('匹配失败')

# reg = r'[\s,]+'
# s = 'a,b,c d  e, f'
# # 分割字符串
# L = re.split(reg,s)
# print(L)

# 分组
# reg = r'(\d{3})-(\d{4,7})'
# s = 'abc029-2348788'
# m = re.search(reg,s)
# print(m.group()) #完整匹配
# print(m.group(0)) #完整匹配
# print('完整匹配的位置',m.start(),m.end())
# print('完整匹配的位置',m.start(0),m.end(0))
# print(m.group(1)) #匹配的第一个分组
# print('匹配的位置',m.start(1),m.end(1))
# print(m.group(2)) #匹配的第二个分组
# print('匹配的位置',m.start(2),m.end(2))

# reg = r'^([0-9]|0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
# # s = '12:34:59'
# # s = '12:00:59'
# # s = '2:00:59'
# s = '02:00:59'
# m = re.search(reg,s)
# print(m.groups())

# 编译正则表达式
# reg = re.compile(r'\d+')
# s = 'a23kmd6174xyz789'
# m = reg.search(s)
# print(m.span())
# print(m.group())
# 以列表形式返回所有匹配的子串
# L = reg.findall(s)
# print(L)
#返回一个顺序访问每一个匹配结果的迭代器
# ms = reg.finditer(s)
# for m in ms:
#     print(m.group(),m.span())
#替换
# s2 = reg.sub('*',s)
# print(s2)
# 替换中引用分组
# print(re.sub(r'(\d+)',r'*\1*','a23kmd6174xyz789'))

# 日期时间
# from datetime import datetime,timedelta,timezone
# d = datetime.now() #返回当前日期时间
# d = datetime(2015,3,20,23,20,33) #创建指定日期时间
# print(d)
# 获取时间戳 秒数
# ts = datetime.now().timestamp()
# print(ts)
# 获取时间分量
# dt = datetime.now()
# print(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second,dt.microsecond,dt.weekday(),
# dt.utcoffset())
# ts = datetime.now().timestamp()
# 时间戳转换为本地datetime
# dt = datetime.fromtimestamp(ts)
# 时间戳转换为标准时区的datetime
# dt = datetime.utcfromtimestamp(ts)
# print(dt)
# 字符串转换为datetime
# dt = datetime.strptime('2017-07-01 23:34:49','%Y-%m-%d %H:%M:%S')
# print(dt)
# datetime格式化为字符串
# s = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f %a %w %z')
# print(s)
# datetime加减
# dt = datetime.now()
# print(dt)
# dt2  = dt+timedelta(days=10) #加一天
# print(dt2)
# dt3 = dt+timedelta(hours=1,minutes=20)
# print(dt3)
#replace替换属性
# tz_utc_W5 = timezone(timedelta(hours=-5)) #创建时区UTC-5:00
# dt = datetime.now(tz=tz_utc_W5)
# print(dt)
# tz_utc_E8 = timezone(timedelta(hours=8))
# dt2 = dt.replace(tzinfo=tz_utc_E8) #设置为指定时区 只是修改了时区 其它时间分量没有变
# print(dt2)
# dt = datetime.utcnow()
# print(dt)
# print(dt.tzinfo) #None
# dt2 = dt+timedelta(hours=8)
# print(dt2)
#时区转换
#拿到utc时间并将其时区设置为UTC+0:00 因为默认不带时区信息
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8))) #转换为北京时间
# print(bj_dt)
# ny_dt = utc_dt.astimezone(timezone(timedelta(hours=-5))) #转换为纽约时间
# print(ny_dt)

# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，
# 请编写一个函数将其转换为timestamp
# import re
# from datetime import datetime,timezone,timedelta
# def to_timestamp(dt_str,tz_str):
#     L = [int(s) for s in re.split(r'\D+',dt_str)]
#     hours = int(re.search(r'[+-]\d+',tz_str).group())
#     dt = datetime(year=L[0],month=L[1],day=L[2],hour=L[3],minute=L[4],second=L[5],tzinfo=timezone(timedelta(hours=hours)))
#     return dt.timestamp()
# print(to_timestamp('2017-7-26 18:02:00','UTC+8:00'))
# print(datetime.now().timestamp())

# collections模块
# from collections import namedtuple
# 创建一个自定义的tuple
# Point = namedtuple('Point',['x','y'])
# p = Point(1,2)
# print(p)
# print(p.x)
# print(p[0])
# print(isinstance(p,Point))
# print(isinstance(p,tuple))
# print(dir(p))

#deque 双端队列
# from collections import deque
# dq = deque(['b','c','d'])
# print(dq)
# dq.append('x')
# dq.appendleft(3)
# print(dq)
# print(dq.pop())
# print(dq)
# print(dq.popleft())
# print(dq)
# for e in dq:
#     print(e)

#dict当key不能存在时会排除KeyError
# d = {'name':'Tom','age':23,0:111}
# print(d[2])
# collectins中提供的defaultditc可设置键不能存在时的默认的返回值
# from collections import defaultdict
# # dd = defaultdict(lambda:'N/A')
# dd = defaultdict(lambda:None)
# dd['name'] = 'Tom'
# print(dd['name'])
# print(dd['nam'])

#dict的key是无序的
# d = {'a':1,'c':3,'b':2,}
# print(d)
# OrderedDict的键会按照插入顺序排序
# from collections import OrderedDict
# od = OrderedDict([('a',1),('c',3),('b',2)])
# print(od)

# 使用OrderedDict实现一个FIFO(先进先出)的dict，当容量超出限制时 先删除最早添加的key
# from collections import OrderedDict
# class LastUpdatedOrderedDict(OrderedDict):
#     def __init__(self,capacity):
#         super(LastUpdatedOrderedDict,self).__init__()
#         self._capacity = capacity
#     def __setitem__(self,key,value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove:',last)
#         if containsKey:
#             del self[key]
#             print('set:',(key,value))
#         else:
#             print('add:',(key,value))
#         OrderedDict.__setitem__(self,key,value)
# d = LastUpdatedOrderedDict(2)
# d['a'] = 1
# d['b'] = 2
# d['a'] = 3
# print(d)

# Counter是一个简单的计数器
# from collections import Counter
# c = Counter()
# for ch in 'opppoa':
#     c[ch] += 1
# print(c)

# base64
# import base64
# b = base64.b64encode(b'01234string')
# print(b)
# print(base64.b64decode(b))

# bs = b'i\xb7\x1d\xfb\xef\xff'
# print(bs)
# ebs = base64.b64encode(bs)
# sebs = base64.urlsafe_b64encode(bs)
# print(ebs)
# print(sebs)
# print(base64.urlsafe_b64decode(sebs))

# struct模块的pack函数吧任意数据类型转换为bytes
# import struct
# >表示big-endian I表示4字节无符号整数
# bs = struct.pack('>I',8)
# print(bs)
# unpack把bytes转换为相应的数据类型
# d  = struct.unpack('>I',b'\x00\x00\x18\x1e')
# print(d)

# import struct
# #位图文件头部编码实例
# bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# #根据位图的格式 解码
# data = struct.unpack('<ccIIIIIIHH',bmp_header)
# print(data)

# 摘要算法
# import hashlib
# md5 = hashlib.md5()
# md5.update('do you love Sam?'.encode('utf-8'))
# rs = md5.hexdigest()
# print(rs)
# print(type(rs))
# print(len(rs))

# sha1 = hashlib.sha1()
# sha1.update('do you love Sam?'.encode('utf-8'))
# rs = sha1.hexdigest()
# print(rs)
# print(type(rs))
# print(len(rs))

# 内建的itertools模块提供了操作迭代对象的函数
#count会创建一格无限的迭代器
# import itertools
# naturals =  itertools.count(0)
# for n in naturals:
#     print(n)

# cycle把传入的一个序列无限重复下去
# cyc = itertools.cycle('ABC')
# for ch in cyc:
#     print(ch)

# repeat返回一个重复指定元素的序列 第二个参数可以指定重复次数
# seq = itertools.repeat('A') #无限重复
# seq = itertools.repeat('A',3)
# for c in seq:
#     print(c)

# takewhile根据条件的到一个序列的子序列
# naturals = itertools.count(0)
# ns = itertools.takewhile(lambda x: x < 10,naturals)
# print(ns)
# print(list(ns))

# chain可以把一组迭代对象串联起来
# for e in itertools.chain([1,2,3],'abc',(3,5)):
#     print(e)

# groupby把相邻的重复元素分组
# for k,group in itertools.groupby('AAABBCDdAA'):
#     print(k,list(group))
# 自定义分组函数
# for k,group in itertools.groupby('AaaBBCDdAA',lambda s: s.upper()):
#     print(k,list(group))

#任何实现了上下文管理的对象都可以在with语句中使用
# 现上下文管理是通过__enter__和__exit__这两个方法实现
# class Query(object):
#     def __init__(self,name):
#         self.name = name
#     def __enter__(self):
#         print('Begin')
#         return self
#     def __exit__(self,exc_type,exc_value,traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#     def query(self):
#         print(str.format('Query info about {0}...',self.name))
# with Query('Bod') as q:
#     q.query()

# contextlib模块可以简化上下文管理
# from contextlib import contextmanager
# class Query(object):
#     def __init__(self,name):
#         self.name = name
#     def query(self):
#         print(str.format('Query info about {0}...',self.name))
# @contextmanager
# def create_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')
# with create_query('Jack') as q:
#     q.query()

# @contextmanager装饰器可以在某段代码前后执行特定的代码
# from contextlib import contextmanager
# @contextmanager
# def tag(name):
#     print(str.format('start {0}',name))
#     yield
#     print(str.format('end {0}',name))
# with tag('kmd'):
#     print('Hello')
#     print('World')

# @closing
# 如果一个对象没有实现上下文，我们就不能把它用于with语句。
# 这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：
# from contextlib import closing
# from urllib.request import urlopen
# with closing(urlopen('https://www.python.org')) as page:
#     for line in page:
#         print(line)

# xml解析
# from xml.parsers.expat import ParserCreate
# class MySaxHandler(object):
#     def __init__(self):
#         self.books = []
#         self.book = None
#         self.data = ''
#     def start_element(self,name,attrs):
#         print('start_element:',name,attrs)
#         if name == 'book':
#             self.book = {'id':attrs['id']}
#     def char_data(self,text):
#         print('char_data:',text)
#         self.data += text.strip()
#     def end_element(self,name):
#         print('end_element:',name)
#         if name == 'book':
#             self.books.append(self.book)
#         elif name == 'name':
#             self.book['name'] = self.data
#         elif name == 'price':
#             self.book['price'] = float(self.data)
#         self.data = ''
#
# xmlStr = r'''<?xml version="1.0" encoding="utf-8"?>
# <books>
#     <book id="1001">
#         <name>Java</name>
#         <price>89</price>
#     </book>
#     <book id="1002">
#         <name>Python</name>
#         <price>88</price>
#     </book>
# <books>
# '''
# handler = MySaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.CharacterDataHandler = handler.char_data
# parser.EndElementHandler = handler.end_element
# parser.Parse(xmlStr)
# print(handler.books)

# html解析
# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#     def handle_endtag(self, tag):
#         print('</%s>' % tag)
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
#     def handle_data(self, data):
#         print(data)
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
#     def handle_entityref(self, name):
#         print('&%s;' % name)
#     def handle_charref(self, name):
#         print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')

# 网络编程
# from urllib import request
# # urlstr = 'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=python'
# # encoding = 'gbk'
# urlstr = 'https://api.douban.com/v2/book/2129650'
# encoding = 'utf-8'
# with request.urlopen(urlstr) as f:
#     data = f.read()
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print(str.format('{0}={1}',k,v))
#     print('Data:',data.decode(encoding))

# 模拟浏览器发送get请求
# from urllib import request
# urlstr = 'http://www.douban.com/'
# encoding = 'utf-8'
# req = request.Request(urlstr)
# #伪装成iphone6
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     data = f.read()
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print(str.format('{0}={1}',k,v))
#     print('Data:',data.decode(encoding))

# 模拟微博登录
# from urllib import request,parse
# print('Login to weibo.cn...')
# email = input('Email:')
# passwd = input('Password:')
# login_data = parse.urlencode([
#     ('username',email),
#     ('password',passwd),
#     ('entry','mweibo'),
#     ('client_id',''),
#     ('savestate',1),
#     ('ec',''),
#     ('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin','https://passport.weibo.cn')
# req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer','https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
# with request.urlopen(req,data=login_data.encode('utf-8')) as f:
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print(str.format('{0}={1}',k,v))
#     print(f.read().decode('utf-8'))

#使用httplib模块 python3后改为http.client
# import http.client
# 发送get请求
# conn = http.client.HTTPConnection('www.baidu.com')
# conn.request('GET','http://www.baidu.com/')
# res = conn.getresponse()
# print('Status:',res.status,res.reason)
# data = res.read()
# print(type(data))
# for k,v in res.getheaders():
#     print(str.format('{0}={1}',k,v))
# print('Data:',data.decode('gbk'))
# conn.close()

# 发送post请求
# import http.client,urllib.parse
# params = urllib.parse.urlencode({'@number':12524,'@type':'issue','@action':'show'})
# headers = {'Content-Type':'application/x-www-form-urlencoded','Accept':'text/plain'}
# conn = http.client.HTTPConnection('bugs.python.org')
# conn.request('POST','',params,headers)
# res = conn.getresponse()
# data = res.read()
# for k,v in res.getheaders():
#     print(str.format('{0}={1}',k,v))
# print('Data:',data.decode('utf-8'))
# conn.close()

# 图像压缩
# from PIL import Image
# im = Image.open('1.jpg')
# w,h = im.size
# print('Original size:',im.size)
# rate = 4
# new_size = (w//rate,h//rate)
# im.thumbnail(new_size)
# print('Resize to:',new_size)
# im.save('a02.jpg','jpeg')

# #模糊滤镜
# from PIL import Image,ImageFilter
# im = Image.open('1.jpg')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('2-filter.jpg','jpeg')

# from PIL import Image,ImageDraw,ImageFont,ImageFilter
# import random
# #随机字符
# def rndChr():
#     s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     return s[int(random.random()*len(s))]
# #随机颜色
# def rndColor(a,b):
#     return (random.randint(a,b),random.randint(a,b),random.randint(a,b))
# width = 60*4
# height = 60
# image = Image.new('RGB',(width,height),(255,255,255))
# #创建字体对象
# font = ImageFont.truetype('C:/Windows/Fonts/arialbi.ttf',36)
# # 获取Draw对象
# draw = ImageDraw.Draw(image)
# # 填充每个像素
# for x in range(width):
#     for y in range(height):
#         draw.point((x,y),fill=rndColor(64,255))
# # 输出文字
# for i in range(4):
#     draw.text((60*i+10,10),rndChr(),font=font,fill=rndColor(32,127))
# #模糊
# # im = image.filter(ImageFilter.BLUR)
# # im.save('vcode.jpg','jpeg')
# image.save('vcode.jpg','jpeg')

# 图形界面 GUI
# python自动的Tkinter图形库是对Tk图形库的简单封装
# GUI版的Hello World
# 导入Tkinter包的所有内容
# from tkinter import *
# # 从Frame派生出一个所有Widget的父容器
# class Application(Frame):
#     def __init__(self,master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()
#     def createWidgets(self):
#         self.helloLabel = Label(self,text='Hello, world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self,text='Quit',command=self.quit)
#         self.quitButton.pack()
# # 实例化Application 并启动消息循环
# app = Application()
# # 设置窗口标题
# app.master.title('hello world')
# # 主消息循环
# app.mainloop()

# from tkinter import *
# import tkinter.messagebox as messagebox
# class Application(Frame):
#     def __init__(self,master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self,text='Hello',command=self.hello)
#         self.alertButton.pack()
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message','Hello, %s' % name)
# app = Application()
# app.master.title('Hello World')
# app.mainloop()

# 网络编程
# 基于TCP的Socket
# 导入socket库
# import socket
# # 模拟一个客户端socket
# # 创建一个socket AF_INET指定使用IPv4协议 SOCK_STREAM指定使用面向流的TCP协议
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 建立连接 注意参数是由ip地址与端口号组成的元组
# s.connect(('www.sina.com.cn',80))
# # 发送数据
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # 接收数据
# buffer = []
# while True:
#     d = s.recv(1024) #每次最多接受1k字节
#     if d: #如果recv返回不为空
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# # 关闭连接
# s.close()
# # 接收到的数据HTTP头和网页 需要把两者分离
# header,html = data.split(b'\r\n\r\n',1) #第二个参数1表示最多进行一次分割
# print(header.decode('utf-8'))
# # 把接收到的数据写入文件
# with open('sina.html','wb') as f:
#     f.write(html)

# import socket,threading,time
# def tcplink(sock,addr):
#     print('Accept new connection from %s' % str(addr))
#     sock.send(b'Welcome!')
#     while True:
#         data = sock.recv(1024)
#         # time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
#         print('客户端说:',data.decode('utf-8'))
#         sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print('Connection from %s closed' % str(addr))
# # 服务器端socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 监听本机的指定端口
# s.bind(('127.0.0.1',9999))
# # 监听连接
# s.listen(5) #参数为最大连接数
# print('Waiting for connection...')
# while True:
#     sock,addr = s.accept() #接收一个连接
#     # 创建新线程处理此连接
#     t = threading.Thread(target=tcplink,args=(sock,addr))
#     t.start()

# email 发送邮件
# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email.utils import parseaddr,formataddr
# import smtplib
# email_config = {
#     'from_addr' : 'kmd6174@163.com',
#     'password' : 'kmd/6174',
#     'smtp_addr' : 'smtp.163.com'
# }
# def _format_addr(s):
#     name,addr = parseaddr(s)
#     return formataddr((Header(name,'utf-8').encode(),addr))

#收件人邮箱列表
# to_list = ['1509102310@qq.com','kmd6174@sohu.com']

#文本邮件 start
# msg = MIMEText('hello, send by Python...','plain','utf-8')
#文本邮件 end

#HTML邮件 start
# msg = MIMEText('<html><body><h1>Hello</h1><p>send by <a href="http://www.python.org">Python...</a></p></body></html>','html','utf-8')
#HTML邮件 end

# 同时支持HTML和plain格式 start
# 当用户不支持HTML时自动降级查看plain格式
# msg = MIMEMultipart('alternative')
# msg.attach(MIMEText('plain text','plain','utf-8'))
# msg.attach(MIMEText('<html><body><h1>html text</h1></body></html>','html','utf-8'))
# 同时支持HTML和plain格式 end

#带附件的邮件 start
# msg = MIMEMultipart() #邮件对象
#带附件的文本邮件 start
# msg.attach(MIMEText('an email with file...','plain','utf-8'))
#带附件的文本邮件 end
#将图片嵌入的html邮件 start
# msg.attach(MIMEText('<html><body><h1>Hello</h1><p><img src="cid:0"/></p></body></html>','html','utf-8'))
#将图片嵌入的html邮件 end
#添加附件就是加上一个MIMIEBase,这里从本地读取一个图片
# with open('2.jpg','rb') as f:
#     mime = MIMEBase('image','jpeg',filename='test.jpg')
#     mime.add_header('Content-Disposition','attachment',filename='test.jpg')
#     mime.add_header('Content-ID','<0>')
#     mime.add_header('X-Attachment-Id','0')
#     mime.set_payload(f.read()) #把附件的内容读进来
#     encoders.encode_base64(mime)
#     msg.attach(mime)
#带附件的邮件 end

# msg['From'] = _format_addr('Python爱好者 <%s>' % email_config['from_addr']) #如果不使用_format_addr 则不能包含中文
# msg['To'] = ';'.join([_format_addr('<%s>' % addr) for addr in to_list]) #如果不使用_format_addr 则不能包含中文
# msg['Subject'] = Header('来自KMD的问候...','utf-8').encode()

# 无加密的smtp start
# server = smtplib.SMTP(email_config['smtp_addr'],25) #SMTP协议默认端口为25
# server.set_debuglevel(1) #显示交互信息
# server.login(email_config['from_addr'],email_config['password'])
# server.sendmail(email_config['from_addr'],to_list,msg.as_string())
# server.quit()
# 无加密的smtp end

# 加密的smtp start
# 可能由于网络问题而发送失败
# server = smtplib.SMTP('smtp.gmail.com',587) #Gmail的SMTP端口是587
# server.starttls() #主要是增加了这个打开ssl安全连接的语句
# server.set_debuglevel(1) #显示交互信息
# gmail_addr = 'mendelkou@gmail.com'
# gmail_pwd = 'koumengde/123'
# server.login(gmail_addr,gmail_pwd)
# server.sendmail(gmail_addr,to_list,msg.as_string())
# server.quit()
# 加密的smtp end

#调用自定义的发送邮件模块
# from kmdemail.myemail import sendemail
# smtp_config = {
#     'smtp_addr' : 'smtp.163.com',
#     'from_addr' : 'kmd6174@163.com',
#     'password' : 'kmd/6174'
# }
# sendemail(
#     smtp_config,
#     ctype='plain',
#     to_list = ['kmd6174@sohu.com','mendelkou@gmail.com'],
#     subject = 'python email 测试',
#     content = 'Hello friends, 我在学python',
#     attach_list=[],
#     encoding='utf-8',
#     debuglevel=1
#     )

# sendemail(
#     smtp_config,
#     ctype='html',
#     to_list = ['kmd6174@sohu.com','mendelkou@gmail.com'],
#     subject = 'python email 测试',
#     content = '<html><h1>Hello friends</h1> <p>我在学python</p></html>',
#     attach_list=[],
#     encoding='utf-8',
#     debuglevel=1
#     )

# sendemail(
#     smtp_config,
#     ctype='alternative',
#     to_list = ['kmd6174@sohu.com','mendelkou@gmail.com'],
#     subject = 'python email 测试',
#     content={
#         'plain':'我在学python',
#         'html':'<html><h1>Hello friends</h1> <p>我在学python</p></html>'
#     },
#     debuglevel=1
#     )

# rs = sendemail(
#     smtp_config,
#     ctype='multi',
#     to_list = ['1509102310@qq.com','kmd6174@sohu.com','mendelkou@gmail.com'],
#     subject = 'python email 测试',
#     content = 'Hello friends, 我在学python',
#     attach_list=[
#         {
#             'path':'2.jpg',
#             'type':'image',
#             'sub_type':'jpeg',
#             'filename':'image-1.jpg'
#         }
#     ],
#     debuglevel=None
#     )
# print(rs)

#python操作数据库 python内置了sqlite
# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可
# sqlite数据库的使用
# 导入SQLite驱动
# import sqlite3
# # 数据库文件是如果不存在 则会在当前路径下创建 返回一个连接
# try:
#     conn = sqlite3.connect('db01.db')
#     # # 创建一个cursor
#     cursor = conn.cursor()
#     # 执行一条sql语句 创建表
#     cursor.execute('create table user(id int primary key,name varchar(32))')
#     # 插入一条记录
#     cursor.execute('insert into user(id,name) values(1,"Jack")')
#     带有参数的语句
#     cursor.execute('insert into user(id,name) values(?,?)',(2,'Rose'))
#     # 打印插入的行数
#     print(cursor.rowcount)
#     查询语句
#     cursor.execute('select id,name from user')
#     L = cursor.fetchall()
#     for r in L:
#         print(r)
#     conn.commit() #提交事务
# except Exception as e:
#     print(e)
# finally:
#     cursor.close() #关闭cursor
#     conn.close() #关闭连接

#操作mysql数据库
#请先通过 命令 pip install pymysql 安装mysql驱动
#python的数据库操作接口是一致的 所有与之前的操作类似
# import  pymysql
# import pymysql.cursors
# conn = None
# cursor = None
# try:
    #注意这里是utf8 写utf-8报错
    # conn = pymysql.connect(host='localhost',user='root',password='',db='db01',port=3306,charset='utf8')
    # cursor = conn.cursor()
    #查询
    # cursor.execute('select * from emp')
    # rowList = cursor.fetchall()
    # for row in rowList:
    #     print(row)
    # print(len(rowList))

    #带参数的查询
    # cursor.execute('select id,name,gender from emp where id>%d' % (2,))
    # rowList = cursor.fetchall()
    # for row in rowList:
    #     print(row)
    # print(len(rowList))

    #返回单行的查询
    # cursor.execute('select id,name,gender,salary from emp where id=1')
    # row = cursor.fetchone()
    # print(row)

    #插入数据
    # cursor.execute("insert into emp(name,gender,salary) values('%s','%s',%f)" % ('x03','女',2843.5))
    # print(cursor.rowcount) #影响的啊行数
    # new_id = cursor.lastrowid #获取新增行的id
    # print(new_id)

    # 删除数据
    # cursor.execute("delete from emp where name like 'x%'")
    # print(cursor.rowcount)
    # conn.commit()
# except Exception as e:
#     # conn.rollback()
#     print(e)
# finally:
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()

# ORM:对象关系映射 就是将数据库中的表映射为类 一行数据就是类的一个实例
# 在Python中，最有名的ORM框架是SQLAlchemy
# 安装SQLAlchemy的命令：pip install sqlalchemy
# from sqlalchemy import Column, String,INT,VARCHAR,CHAR ,DECIMAL,create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# # 创建表示数据表的类的基类
# Base = declarative_base()
# # 根据emp表创建Emp类
# class Emp(Base):
#     #表名
#     __tablename__ = 'emp'
#     #表的结构
#     id = Column(INT(),primary_key=True)
#     name = Column(VARCHAR(32))
#     gender = Column(CHAR(1))
#     salary = Column(DECIMAL(10,2))
#
# session = None;
# try:
#     # 初始化数据库连接
#     engine = create_engine('mysql+pymysql://root:@localhost:3306/db01?charset=utf8')
#     # 创建dbSession类型
#     DBSession = sessionmaker(bind=engine)
#     # 创建session 数据库会话
#     session = DBSession()

    # 插入记录
    # emp = Emp(name='x01',gender='男',salary=897.5)
    # session.add(emp)
    # session.commit()

    # 查询数据
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    # emps = session.query(Emp).filter(Emp.id>1).all()
    # for e in emps:
    #     print(e.id,e.name,e.gender,e.salary)

    # 更新单条记录
    # emp = session.query(Emp).get(11) #根据主键查询
    # print(emp.salary)
    # emp.salary = 1200
    # # session.flush()
    # session.commit()

    # 删除记录
    # emp = session.query(Emp).get(11)
    # session.delete(emp)
    # session.flush()
    # session.commit()
# except Exception as e:
#     print(e)
# finally:
#     if session:
#         session.close()

# python中的生成器可实现协程
#一个简单的生成者与消费者的协程模型的实现
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if n:
#             print('Consuming... %s' % n)
#             r = '200 OK'
#         else:
#             return
# def producer(c):
#     c.send(None) #启动生成器 相当于next(c)
#     n = 1
#     while n <= 5:
#         print('Produced %s' % n)
#         r = c.send(n)
#         print('Consumer return %s' % r)
#         n += 1
#     c.close()
#
# c = consumer()
# producer(c)

# syncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持
# import asyncio
# @asyncio.coroutine #把一个生成器标记为coroutine类型
# def hello():
#     print('Hello world!')
#     r = yield from asyncio.sleep(1) #线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环
#     print('Hello again!')
# # 获取EventLoop
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# 用Task封装两个coroutine
# import threading,asyncio,random
# @asyncio.coroutine
# def hello():
#     n = random.randint(1,100)
#     print('%d:Hello world! (%s)' % (n,threading.currentThread()))
#     yield from asyncio.sleep(1)
#     print('%d:Hello world! (%s)' % (n,threading.currentThread()))
# loop = asyncio.get_event_loop()
# tasks = [hello(),hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# 使用异步网络获取几个网站的首页
# import asyncio
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host,80)
#     reader,writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s reader > %s' % (host,line.decode('utf-8').rstrip()))
#     writer.close()
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com','www.sohu.com','www.qq.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# 为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await
# async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
# 1)把@asyncio.coroutine替换为async；
# 2)把yield from替换为await
# import asyncio,threading,random
# async def f():
#     n = random.randint(1,1000)
#     m = random.random()+1
#     print('%d:%s' % (n,threading.currentThread()))
#     await asyncio.sleep(m)
#     print('%d:%f,%s' % (n,m,threading.currentThread()))
# loop = asyncio.get_event_loop()
# tasks = [f(),f()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# syncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架
# 安装aiohttp: pip install aiohttp
# 编写一个HTTP服务器，分别处理以下URL：
# / - 首页返回b'<h1>Index</h1>'；
# /hello/{name} - 根据URL参数返回文本hello, %s!
# import asyncio
# from aiohttp import web
# async def index(request):
#     await asyncio.sleep(0.5)
#     return web.Response(body=b'<h1>Index</h1>',content_type='text/html')
# async def hello(request):
#     await asyncio.sleep(0.5)
#     text = '<h1>hello, %s!</h1>' % request.match_info['name']
#     return web.Response(body=text.encode('utf-8'),content_type='text/html')
# async def init(loop): #init()也是一个coroutine
#     app = web.Application(loop=loop)
#     app.router.add_route('GET','/',index)
#     app.router.add_route('GET','/hello/{name}',hello)
#     srv = await loop.create_server(app.make_handler(),'127.0.0.1',8000)
#     print('Server started at http://127.0.0.1:8000...')
#     return srv
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()
