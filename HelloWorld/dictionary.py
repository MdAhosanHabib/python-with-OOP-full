nums = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
phone = input("Enter any number: ")
output = ""
for ch in phone:
    output += nums.get(ch, "!") + " "
print(output)


##example

text = input(">")
words = text.split(" ")
emo = {
    ":(": "😥",
    ":)": "😀"
}
outputs = ""
for em in words:
    outputs += emo.get(em, em) + " "
print(outputs)