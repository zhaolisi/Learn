#coding=utf-8
'''
#类的继承
class Father(object):
    def __init__(self, name):
        self.name = name
        print ("name: %s" % (self.name))

    def getName(self):
        return 'Father ' + self.name
#子类不重写 __init__，实例化子类时，会自动调用父类定义的 __init__
class Son(Father):
    def __init__(self, name):#重写了__init__ 时，实例化子类，就不会调用父类已经定义的 __init__
        print ("hi")
        self.name = name
    def __init__(self, name):#如果重写了__init__ 时，要继承父类的构造方法，可以使用 super 关键字：
        super(Son, self).__init__(name)
        print ("hi")
        self.name = name

    def getName(self):
        return 'Son ' + self.name
if __name__ == '__main__':
    son = Son('zhaolisi')
    print (son.getName())
'''

#私有变量和私有方法
class JustCounter(object):
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount
    def __minus(self): # 私有方法
        self.__secretCount +=2
        self.publicCount +=2
    def add(self):
        self.__minus()#私有方法只能在类的内部调用self.__private_methods
        print self.__secretCount

counter = JustCounter()
print counter._JustCounter__secretCount#使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问私有变量
counter.count()
print counter.publicCount
counter.add()
counter.__minus() #报错，私有方法不能在类的外部调用
print counter.publicCount
print counter.__secretCount # 报错，实例不能访问私有变量

#__foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
#_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
#__foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了
