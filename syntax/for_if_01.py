
# 简单的for...[if]...语句
# Python中，for...[if]...语句一种简洁的构建List的方法，从for给定的List中选择出满足if条件的元素组成新的List，其中if是可以省略的。
a=[12,3,4,6,7,13,21]

newList =[x for x in a]
print(newList)

newList2 =[x for x in a if x%2==0]
print(newList2)


#省略if后，newList构建了一个与a具有相同元素的List。但是，newList和a是不同的List。
# 执行b=a，b和newList是不同的。newList2是从a中选取满足x%2==0的元素组成的List。如果不使用for...[if]..语句，
# 构建newList2需要下面的操作。
newList3=[]
for x in a:
    if x%2==0:
        newList3.append(x)
print(newList3)

# 显然，使用for...[if]...语句更简洁一些