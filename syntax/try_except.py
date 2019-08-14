#在异常处理语句中，else有相似的用法，当try代码块没有抛出任何的异常时，else语句块会被执行到。

def my_to_int(str_param):
    try:
        int(str_param)
        print(str_param)
    except ValueError:
        print('cannot convert {} to a integer'.format(str_param))
    else:
        print('convert {} to integer successfully'.format(str_param))

my_to_int("123")
my_to_int("me123")

'''
如打印日志所示，在转换成功未发生错的的时候，else语句里的逻辑会被执行，当然这个例子可能并没有什么太多的实际的用处，
但大致能说明else在错误处理中的用处：简化逻辑，避免使用一些标志值就能够准确把握是否发生错误的情况来做一些实际的操作
（比如在保存数据的时候如果发生错误，在else语句块中进行rollback的操作，然后紧接着还能加上finally语句完成一些清理操作。

善用else语句块能够让我们编写出更加简明，更加接近自然语言的语义的代码，当然也会更加的pythonic，细微之处大家可以慢慢体会。
'''
