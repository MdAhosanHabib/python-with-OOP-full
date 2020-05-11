class Mammal:
    def talk(self):
        print("say")


class Dog(Mammal):
    def dis(self):
        print("hi")


class Cat(Mammal):
    def biral(self):
        print("I am Cat")


dog1 = Dog()
dog1.dis()

cat1 = Cat()
cat1.biral()