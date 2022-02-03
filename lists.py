names = ["Fred's","Jim", "Sheila"]
print(names)
print(type(names))
print(names[0])  # indexed from zero
names[0] = "Frederick"  # lists are "mutable"
print(names)

numbers = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
print(numbers)
print(numbers[2:9:2])  # slicing can be done with your own data types
print(numbers[2::2])
print(numbers[::2])
print(numbers[-1])  # index from "the end"
print(numbers[-3])
print(numbers[::-1])
print(numbers[3::-1])
print(numbers[3:0:-1])

things = ["Hello", 99, 3.14]
print(things)

print("Hello" in things)