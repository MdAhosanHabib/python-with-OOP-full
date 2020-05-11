try:
    age = int(input("enter age: "))
    income = 22000
    rest = income / age
    print(age)
except ZeroDivisionError:
    print("divided by zero not accepted")
except ValueError:
    print("Invalid Value")

