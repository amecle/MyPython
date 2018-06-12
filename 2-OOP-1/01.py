
'''
定义一个学生类，用来形容学生
'''

# 定义一个类
class Student():
    pass

# 定义一个对象
std = Student()

# 再定义一个类，学习python的学生
class PythonStudent():
    name = None
    age = 18
    course = 'python'

    # 1.def 缩进和属性同级
    # 2.系统默认出一个self参数
    def doHomework(self):
        print('I 在做作业')
        return None

# 实例化一个叫wang的学社，是一个具体的对象
wang = PythonStudent()
print(wang.name)
print(wang.age)
# 注意成员函数的调用没有传递参数
wang.doHomework()