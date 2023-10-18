#program that finds number '0' in a big number and prints its index
def func(number):
    number = str(number)
    indices = []
    for i in range(len(number)):

        if number[i] == '0':
            indices.append(i)
    return indices
number = 103123032423804854803
print(func(number))
