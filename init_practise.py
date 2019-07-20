
class students:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name,'can walk')
        print(self.name,'is ',self.age)


s1 = students(name='inty',age='18')
s1.walk()

s2 = students('liangmin',20)
s2.walk()





