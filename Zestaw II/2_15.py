# program that turns numbers in a list into strings, puts them together and prints them
def func(list):
    list = [str(x) for x in list]
    return ''.join(list)


list = [1, 2, 3, 4, 5, 10, 1000, 999, 9999]
print(func(list))
