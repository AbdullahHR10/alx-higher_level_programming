for i in range(1, 100):
    if i == 99:
        print("{}{}".format((i // 10), (i % 10)), end="")
    else:
        print("{}{} ,".format((i // 10), (i % 10)), end="")