for i in range(1,10,2):
    print(i)


prices = [10, 20, 30]
total = 0
for item in prices:
    total += item
print(f"total price is {total}")


numbers = [5, 2, 5, 2, 2]
for i in numbers:
    output = ""
    for j in range(i):
        output += "X"
    print(output)


for x in range(3):
    for y in range(2):
        print(f"({x},{y})")