# List Comprehension 列表解析式
#list 生产新list的过程就是list comprehension 的一种
#我的需求是:从0-10数字分别乘以2，然后放到新的列表（list）里面

# 传统的做法
newList = []
for i in range(11):
    newList.append(i*2)
print(newList)

#用list comprehension
print([i*2 for i in range(11)])

#应用场景：从网上爬虫一堆数据在list里面，进行筛选
list = ['小明','王二','王八','李四']
emptyList = []
for name in list:
    if name.startswith('王'):
        emptyList.append(name)
print(emptyList)

#应用场景：从网上爬虫一堆数据在list里面，进行筛选，用list comprehension
print([name for name in list if name.startswith('王')])













