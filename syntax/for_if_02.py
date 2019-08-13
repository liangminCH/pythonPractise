
#嵌套的for...[if]...语句可以从多个List中选择满足if条件的元素组成新的List。下面也举几个例子。
a=[12,3,4,6,7,13,21]
b=['a','b','x']

newList=[(x, y) for x in a for y in b]
#print(newList)

newList2=[(x, y) for x in a for y in b if x%2==0 and y<'x']

'''
等价于：
for x in a :
    for y in b:
        if x%2==0 and y<'x'
'''

#print(newList2)

#嵌套的for...[if]...语句与多重for语句相当，最前面的for语句是最外层的循环。


if 'a'<'14':#14字符串，内存解析成了整形来比较
    print('111')
else:
    print('222')



