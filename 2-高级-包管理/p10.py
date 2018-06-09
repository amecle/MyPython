from pkg02 import *

stu = p01.Student()
stu.say()

# 下句会报错，因为__init__模块中有__all__，所以__init__中的内容不再执行
# inInit()
