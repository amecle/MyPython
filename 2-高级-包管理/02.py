# 借助于importlib包可以实现导入以数字开头的模块名称
import importlib

# 相当于导入了一个名称为 01 的模块并把导入模块赋值给了baobao
baobao = importlib.import_module('01')

stu = baobao.Student()
stu.say()
