#coding=utf-8
'''
print "Hello，World "
print "你好，世界"

string="Hello"

print string #Hell
print string[0]# o
print string[1:3] #el
print string[2:] #llo
print string*2 #HelloHello
print string+"World" #HelloWorld
'''
#列表可以二次赋值
list=['H','e','l','l','o']
list2=['W','o','r','l','d']

print list #['H', 'e', 'l', 'l', 'o']
print list[0] #H
print list[0:3] #['H', 'e', 'l']
print list[2:] #['l', 'l', 'o']
print list * 2 #['H', 'e', 'l', 'l', 'o', 'H', 'e', 'l', 'l', 'o']
print list + list2 #['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
print list[-1]
list[0]='h'
print list #['h', 'e', 'l', 'l', 'o']
list.append('Python')
print list #['h', 'e', 'l', 'l', 'o', 'Python']
del list[0]
print list #['e', 'l', 'l', 'o', 'Python']
length=len (list) #列表元素个数
print length #5



'''
#元组不能二次赋值，相当于只读列表。
tuple=('H','e','l','l','o')
tuple2=('W','o','r','l','d')

print tuple #('H', 'e', 'l', 'l', 'o')
print tuple[0] #H
print tuple[1:3] #('e', 'l')
print tuple[2:] #('l', 'l', 'o')
print tuple*2 #('H', 'e', 'l', 'l', 'o', 'H', 'e', 'l', 'l', 'o')
print tuple+tuple2 #('H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd')
length=len tuple
print length #5
#tuple[0]='h' 报错，因为元组不能二次赋值
'''
dict={}
dict['one']='This is one'
dict[2]='This is two'
dict1={'name':'zhaolisi','code':2471,'dept':'Testing'}

print dict['one'] #This is one
print dict[2] #This is two
print dict1 #{'dept': 'Testing', 'code': 2471, 'name': 'zhaolisi'}
print dict.keys() #[2, 'one']
print dict.values() #['This is two', 'This is one']

