def user_name(f_name, l_name):
    print(f"hi i am {f_name} {l_name}")
    print("first function")


print("function start")
user_name("ahosan", "habib")







def calculate(num):
    return num * num


print(calculate(3))







#emoji
def emo_convert(text):
    words = text.split(" ")
    emo = {
        ":(": "😥",
        ":)": "😀"
    }
    outputs = ""
    for em in words:
        outputs += emo.get(em, em) + " "
    return outputs


text = input(">")
print(emo_convert(text))
