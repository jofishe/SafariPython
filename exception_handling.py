
months = ["January", "February"]

def get_month_name(m):
    if m < 0 or m > 12:  # & and | are bitwise operators!!!  use "and" and "or" for logical operations
        raise ValueError("that's too big of a month")
    return months[m - 1]

try:
    print(get_month_name(-1))
    print("That succeeded")
except ValueError as ve:
    print("oops that broke", ve)
except IndexError as ie:
    print("that wasn't in my list", ie)
finally:
    print("Still going")

