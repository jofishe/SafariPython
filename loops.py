x = 3
# while x > 0:
while x:
    print(x)
    x -= 1
    if x == 1:
        y = x
        break  # break only exits the immediately enclosing loop
else:
    print("what the heck??")

print("finished... x is ", x, "y is", y)  # NOT BLOCK scoped

names = ["Fred", "Jim", "Sheila"]
for n in names:
    print(n)

for i in range(0, 10, 2):
    print(i)

print(range(1, 10))
print(list(range(1, 10)))

names = {"Fred": "Jones", "Jim": "Smith"}
# for k in names.keys():
for k in names:
    print(k)
    print(type(k))

for k in names.values():
    print(k)
    print(type(k))

for k in names.items():
    print(k[0], k[1])
    print(type(k))
