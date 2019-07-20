
class Father:
    def eat(self):
        print("father can eat")

class Mother:
    def walk(self):
        print("walk like mother")


class Son(Father):
    pass

class Son01(Father,Mother):
    def eat(self):
        print("eat like son")

littleInty = Son()
littleInty.eat()

littleLm = Son01()
littleLm.eat()
littleLm.walk()


















