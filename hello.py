# from __future__ import braces

print("Hello Python World", "It's really cold in Colorado", sep="--", end="")
print('really')

x = 99  # also octal and hexadecimal formats
print(x)
print(type(x))

x = x ** 80
print(x)

x = "Hello"
print(x)
print(type(x))

x = 3.14
print(x)
print(type(x)) # IEE 754, 64 bit

x = 1 + 2j
print(x)
x = 0 + 1j
print(x, x **2)

print(f"the value of x is {x ** 2}")

x = 99
print("the value of x is " + "99")  # overloaded __add__
print("the value of x is " + str(99))  # str intended for "human" use
print("the value of x is " + repr(99))  # repr is for "machine" use

y = 100
print(x == y)
print(type(x == y))
y = 99
print(x == y)
print(x is y)

x = "Hello"
y = "He"
y += "llo"
print(x == y)  #  __eq__
print(x is y)

x = 100
# x++ NOPE!

print(x, bool(x))
x = 0
print(x, bool(x))
x = "False"
print(x, bool(x))

if x:
    print("x had a truthy value")
    print("oopps")
# else:
#     if x > 100:
#         print("x was falsy")
elif x > 100:
    print("aha, no additional indent needed with elif")

# BAD
# if x: print("yup, it's still true")
#     print("more")
# OK, but why?
if x: print("yup, it's still true"); print("more")

# list, tuple, dict
