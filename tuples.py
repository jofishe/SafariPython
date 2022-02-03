# person = ("Fred", 24, 3000.14, (6, 4))
# person = "Fred", 24, 3000.14, (6, 4)
person = "Fred", 24, 3000.14, [6, 4]
print(person)
print(type(person))
print(person[3])
print(type(person[3]))

person[3].append(99)
print(person)
# person[0] = "Frederick"
print(24 in person)