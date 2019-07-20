'''
**kwargs
key word args
the type of args is : <class 'tuple'>
the type of kwargs is : <class 'dict'>
'''
def m1(*args, **kwargs):
    print('the type of args is :',type(args))
    print('the type of kwargs is :',type(kwargs))

m1()

dic_inty = {'name':'inty','age':'18 years old','height':'190cm','weight':'195lb'}
for k,v in dic_inty.items():
    print(k,':',v)

print("==================")

# def someone(dic_someone):
#     for k, v in dic_someone.items():
#         print(k, ':', v)
# someone(dic_inty)

def someone(**kwargs):
    for k,v in kwargs.items():
        print(k, ':', v)
someone(name='xiaohong',age='20')
someone(name='xiaohong',age='20',height='180')
someone(name='xiaohong',age='20',height='180',weight='150kg')



































