'''
什么是*args
arguments 多个参数的意思
'''
# def add3(num1,num2,num3):
#     print(num1+num2+num3)
# add3(1,2,3)
#
# def add2(num1,num2):
#     print(num1+num2)
# add2(1,2)
# # 参数个数不确定

# 这也是一种 syntax sugar 语法糖 让代码更优化
def add(*args):
  #  print(sum(args))
    print(args)
    print(type(args))
    for name in args:
        print('i love ', name)
add(1,1)
add(1,1,2)
add(1,1,3,4)
add('小明','王二','李四','inty')






















