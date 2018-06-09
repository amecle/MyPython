class Student():
    def __init__(self, name='NoName', age=18):
        self.name = name
        self.age = age

    def say(self):
        print('My name is {0}'.format(self.name))
        print('I am {}'.format(self.age))

def sayHello():
    print('Hi,欢迎学习python！')

print('我是模块p01.')