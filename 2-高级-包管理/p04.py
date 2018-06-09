from p01 import Student, sayHello

# 下句会报错:name 'p01' is not defined
# （因为没有导入p01，所以找不到p01）
# stu = p01.Studend()

stu = Student()
stu.say()

sayHello()