#program that replaces 'GvR' with 'Guido van Rossum' in a string
def func(string):
    return string.replace('GvR', 'Guido van Rossum')
line = 'GvR is the creator of Python.'
print(func(line))