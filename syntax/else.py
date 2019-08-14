a, b, c = 0, -1, 3
print('a: ',a,'  b:',b,'  c :',c)

# 1.常规
if a > b:
    c = a
else:
    c = b

print('a: ',a,'  b:',b,'  c :',c)

#2.表达式
c = a if a>b else b
print('a: ',a,'  b:',b,'  c :',c)

#3.二维列表
c = [b,a][a>b]
print('a: ',a,'  b:',b,'  c :',c)

#4.传说是源自某个黑客
c = (a>b and [a] or [b])[0]
print('a: ',a,'  b:',b,'  c :',c)

'''
and, or:
 # 判断变量是否为0， 是0则为False，非0判断为True，
 # and中含0，返回0； 均为非0时，返回后一个值， 
2 and 0   # 返回0
2 and 1   # 返回1
1 and 2   # 返回2

# or中， 至少有一个非0时，返回第一个非0,
2 or 0   # 返回2
2 or 1   # 返回2
0 or 1   # 返回1 
'''

