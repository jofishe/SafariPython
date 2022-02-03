scores = {"Fred":99, "Jim": 76, "Sheila":100}
print(scores)
print(type(scores))
print(scores["Fred"])
if "Albert" in scores:
    print(scores["Albert"])
else:
    print("Albert isn't there...")
print(scores.get("Albert"))  # None is a singleton that represents "there isn't one"

scores["Albert"] = 97
print(scores)

scores["Fred"] = 87
print(scores)

del scores["Fred"]
print(scores)

x = 100  # all data is in a "namespace" (which is a dictionary)
print(x)
print(vars())
del x
print(vars())
# print(x)
