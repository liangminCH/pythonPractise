# a=10
# b=20
# if b>a:
#     print("b>a")
# if b<30:
#     print("hello")
#age = input("please inter age: ")
age = int(input("please inter age: "))
print(type(age))

if age<21:
    print("you can not smoke")
elif age == 21:
    print("you are now 21, you can go to smoke")
elif age == 100:
    print("you are 100 years old , please quit smoking")
else:
    print("you can smoke")







