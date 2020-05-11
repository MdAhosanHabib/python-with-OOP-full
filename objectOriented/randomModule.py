import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20))

members = ["ahosan", "habib", "rakib"]
#led = random.choice(members)
print(random.choice(members))


class Dice:
    def rand(self):
        first = random.randint(1, 6)
        last = random.randint(1, 6)
        return first, last


dice = Dice()
print(dice.rand())

