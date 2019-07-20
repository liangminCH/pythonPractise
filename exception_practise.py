#处理异常

# try:
#     print(10/0)
# except:
#     print("you can not do it")

try:
    print(10 / 8)
#    print(10/0)
    print(10+'o')
except ArithmeticError as e:
    print(e)
except TypeError as e:
    print('there is something wrong:',e)










