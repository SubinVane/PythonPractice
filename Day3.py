#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

set1 = set([1,2,3,4,5,6,1,2,3,4])
print(set1)

set1.add(1)
set1.add(7)
print(set1)

set1.remove(1)
print(set)

set2 = set([3,4,5,8,9])
print(set1 & set2)
print(set1 | set2)

a = ['c','a','b']
a.sort()
print(a)


b = 'abc'
c = b.replace('a','A')
print(b)
print(c)


print(abs(-10.24))
print(abs(100))

print(max(2,3,4,1,-5))

print(int('123'))
print(float('12.34'))
print(str(123))
print(bool(1))
print(bool(""))

print(hex(100))

def myAds(x):
	# 数据类型检查可以用内置函数isinstance()
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')

	if x>0:
		return x;
	else:
		return -x;

print(myAds(12))

# from abstest import my_abs     ///命令行模式 ，  abstest为.py文件， my_abs 为函数

#pass
def nop():
	pass #占位

if 12>11:
	pass # 让程序继续

# 返回多个值
def move(x,y,step,angle = 0):
	nx = x +step * math.cos(angle)
	ny = y -step * math.sin(angle)
	return nx,ny

print(move(100,100,60,math.pi/6))

r = move(100,100,60,math.pi/6)
print(r)

#默认参数必须指向不变对象！
def add_end(L = []):
    L.append('END')
    return L
print(add_end())
print(add_end())

def add_end_modify(L = None):
	if L is None:
		L = []
	L.append('End')
	return L

#可变参数
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum
print(calc(1,2,3,4,5,6))
print(calc(1,2,3,4))
#list 或者 tuple
nums = [1,2,3,4]
print(calc(*nums))


#关键字参数
def fun1(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

fun1('Vane','18')
fun1('Vane','18',city = 'Shenzhen')

extra = {'city':'Shenzhen','gender':'F'}
fun1('Vane','18',gender=extra['gender'])
fun1('Vane','18',**extra)


#命名关键字参数
def fun2(name,age,*gender,address,zipcode):
	print(name,age,gender,address,zipcode)

fun2('Vane','18','F',address = '123',zipcode='dsadsa')














































