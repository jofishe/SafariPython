
# c is captured by "closure"
def inc_by(c):
    return lambda a: a + c  # lambdas are restricted to arg-list : expression

plus_two = inc_by(2)
print(plus_two(3))

