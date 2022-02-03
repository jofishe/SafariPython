
#  classes don't "declare" fields, we simply add items to the dictionary!
class CrudeDate:
    # effectively creates a "static" element.
    # It belongs to the *class* rather than the individual objects
    x = 100

    pass

d = CrudeDate()  # Python doesn't say "new"
print(d)
print(type(d))

d.day = 3
d.month = 2
print("day is", d.day)
print("month is", d.month)
# print(d.__dict__)  # potentially implementation dependent
print(vars(d))
print(type(vars(d)))

print(CrudeDate.x)
print(d.x)