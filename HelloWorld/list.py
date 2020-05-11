numbers = [2, 5, 7, 8,3, 6, 8, 9, 11, 4]
max = numbers[0]
for i in numbers:
    if max < i:
        max = i
print(f"maximum number is {max}")

#2d list
mattrix = [
    [1,2,3],
    [4,5,6],
    [9,8,7]
]
print(f"number is: {mattrix[0][1]}")
for row in mattrix:
    for item in row:
        print(item)

#unique number print
nums = [2, 3, 4, 2, 4, 6, 8, 9, 6]
uniqe = []
for num in nums:
    if num not in uniqe:
        uniqe.append(num)
print(uniqe)