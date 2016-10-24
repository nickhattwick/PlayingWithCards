x = ["one", "two"]
try:
    y = x.index("three")
    print(y)
except ValueError:
    print("check")
