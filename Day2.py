#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

print('Hello,%s' % 'world')
print('亲爱的%s,你好!你%d月的话费是%s' % ('Vane',1,50))
print('你好，{0} ，您的余额是 {1:.2f}'.format('Vane',50.00000))

people = ['Vane','Bingo','Nanzeng','Lyman']
print(people)
print(len(people))

print(people[0])
#-1表示list 最后一个元素的索引，-2，-3 以此类推，也存在数组越界
print(people[-1])

#往list中追加元素到末尾
people.append('111')
print(people[-1])

#把元素插入到指定的位置
people.insert(4,'000')
print(people)

#删除list末尾的元素
people.pop()
print(people)

people.pop(-1)
print(people)

#有序列表叫元组：tuple
person = ('Vane','Bingo','Nanzeng','Lyman')
person = ('000',people)
people.append('111')
print(person)

age = int(input('请输入您的年龄'))
if age >= 18:
    print('你成年了')
elif age>=6:
    print('你是青少年了')
else :
	print('你是个儿童')

if age:
	print('age 非零数值、非空字符串、非空list')


#for.. in ..
for peo in people:
	print(peo)


sum =0 
for x in range(101):
	sum +=x
print(sum)

#dict
map = {'Vane':100,'Bingo':0,'...':0}
print(map['Bingo'])
map['Bingo'] = 90
print(map['Bingo'])

print('Nanzeng' in map)
print('Vane' in map)

print(map.get('Nanzeng')) #None
print(map.get('Nanzeng',90))

print(map.pop('...'))
print(map)

