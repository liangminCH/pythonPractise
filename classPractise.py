# fruit = "apple"
# print(fruit.upper())
# # objectc oriented
# class Student():
#     def eat(self):
#         print("student can eat !")
#     def study(self):
#         print("student can study!")
#
# # Student().eat()
# inty = Student()
# inty.eat()
# inty.study()
# print("=========================")
# class Student:
#     def eat(self, name, age):
#         print(name + "  student can eat" + 'and he is ' + age)
#         print(name, 'can eat ', 'and he is ', age)
#
#
# Student.eat(2323, "liangmin", '18')
# Student().eat("liangmin", '18')

class Student:
    name = 'inty'
    age = 18
    def eat(self):
        print(self.name, 'can eat ', 'and he is ', self.age)

    @staticmethod
    def walk():
        print('student can walk')
        #print(name,'student can walk')#这边不可以调用name
        #print(self.name,'student can walk')#这边不可以调用self.name

Student().eat()
Student().walk()

student1 = Student()
student1.eat()
student1.walk()

student2 = Student()
student2.walk()
student2.eat()





