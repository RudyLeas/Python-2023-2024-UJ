def make_ruler(dl):
    ruler = "|"

    for i in range(dl):
        ruler += "....|"

    ruler += "\n"

    for i in range(dl + 1):
        ruler += str(i) + (5 - len(str(i + 1))) * " "

    print(ruler)


# example use:
length = 101
make_ruler(length)
