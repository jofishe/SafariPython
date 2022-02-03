
# f = open("text.txt", "r")
with open("text.txt", "r") as f:  # things used in a with stucture must have __enter__
    for l in f:  # by default this includes the line terminator at the end of the string
        print(l, end="")

# f.close()  # not really the reliable approach

