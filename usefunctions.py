
def add(a: int, b: int) -> int:
    print("you called add")
    return a + b

x = add(1, 2)
print(x)
print(type(x))
x = add
print(type(x))
x(2, 3)

print(add("Hello", " world"))

def day_of_week(day, month, year = 2022):
    """
    This is a function that calculates the day of week
    as 0 = Saturday -> 6 = Friday
    from the day, month and year
    See Zeller's congruence on wikipedia
    :param day:
    :param month:
    :param year:
    :return:
    """
    # pass  # syntax placeholder, can use when incomplete
    # first, month and year if Jan or Feb are treated as months 13 and 14 of previous year
    (month, year) = (month, year) if month > 2 else (month + 12, year - 1)
    # % in Python is MOD not REMAINDER
    return (day + (13 * (month + 1) // 5) + year + year // 4 - year // 100 + year // 400) % 7

print(day_of_week.__doc__)  # try to avoid dunders...
print(day_of_week(3, 2, 2022))
print(day_of_week(month = 2, day = 3, year = 2022))
print(day_of_week(month = 2, day = 3))

# varargs come after positional args
def show_all(a, b, *args, **kwargs):
    print(f"a is {a}, b is {b}")
    for v in args:
        print(">", v)
    print(kwargs, type(kwargs))
    for k, v in kwargs.items():
        print("kw:", k, ":", v)

show_all(99, "Fred", "x", 3, 3.14, sep="ooh!", fruit="Banana")

