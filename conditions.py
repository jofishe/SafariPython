x = True

y = "Hello" if x else "Bonjour"
print(y)

#  match, NEW WITH 3.10
# x = 200
x = ["Fred", "Jones"]

match x:
    case 100 | 200:
        print("it's 100 or 200")
    case [a, b]:
        print(f"it's a list of two elements a is {a}, and b is {b}")
    case _:
        print("it's something else")

