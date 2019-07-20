
#打开同级目录下文件，方法一
# file = open('inty.txt')
# text = file.read()
# print(text)
# file.close()#如果不关掉，代码一直在运行状态，记住要关闭

#方法二,这种方法打开文件不需要最后进行close()
# with open('inty.txt') as f:
#     print(f.read())

#打开其他文件夹文件,右击该文件 copy path
# with open('D:\pythonPractise\myFile\inty02.txt') as f:
#     print(f.read())

#写文件
#这种方式覆盖了之前的内容进行写入
# with open('D:\pythonPractise\myFile\inty02.txt','w') as f:
#     f.write('hello world,i love you')

#a   append
# with open('D:\pythonPractise\myFile\inty02.txt','a') as f:
#     f.write('nice to meet you' )

with open('D:\pythonPractise\myFile\inty02.txt','a') as f:
    f.write('nice to meet you \n' )

print(dir(open))
print(help(open))






