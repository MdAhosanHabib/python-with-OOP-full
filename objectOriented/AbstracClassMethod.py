from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def show(self):
        pass


class A(Computer):
    def show(self):
        print("i am abstruct")


a = A()
a.show()
