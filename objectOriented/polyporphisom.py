class MethodOverloading:
    def sum(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c !=None:
            s = a+b+c
        elif a != None and b != None:
            s = a+b
        else:
            s = a
        return s


overloading = MethodOverloading()
print(overloading.sum(5, 6))





class A:
    def show(self):
        print("in a")


class B:
    def show(self):
        print("in b")


b1 = B()
b1.show()
