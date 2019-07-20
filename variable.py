
# Numbers（数字）

# a=5
# b=10
# c=5.5
# d=10.3432423
# print(5+10)
# print(a+b)
# print(c+d)
#
# # String（字符串）
# name = "intyasefasgg"
# print("inty")
# print(name)
# print(name[0])
# print(name[1])
# print(len(name))
# print(name[2:5])
# print(name*2)
# print(name+"  is a good boy")

#List(列表)
# my_List = ["你好",2018,2018,2018,2018,"English",20000,"你好"]
# #help(my_List)
# # print(len(my_List))
# # print(my_List[0])
# # my_List.append("5000")
# # print(len(my_List))
# # print(my_List)
# # my_List.remove("English")
# # print(my_List)
# print(my_List.count(2018))
# print(my_List.count("你好"))
# my_List.clear()
# print(my_List)
# print(len(my_List))

#tuple 元组
# Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
# 创建空元组
# tup1 = ()
# 元组中只包含一个元素时，需要在元素后面添加逗号
# tup1 = (50,)
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
mylist = [1,2,3,4,5]
mytuple = (1,2,3,4,5)
# print(type(mylist))
# print(type(mytuple))
# print(len(mylist))
# print(len(mytuple))
# print(mylist[0])
# print(mytuple[0])
# dir查询任何一个obeject方法
# print(dir(mylist))
# print("=================================")
# print(dir(mytuple))
#list is mutable
#tuple is inmutable
# mylist.remove(2)
# print(mylist)
#AttributeError: 'tuple' object has no attribute 'remove'
#如果不想数据被用户更改就使用tuple
#mytuple.remove(2)
#print(mytuple)
#因为tuple方法少于list，所以数据量很大的时候，tuple运算速度要快于list

































