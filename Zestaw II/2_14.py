# program that finds a longest word and its len in a string and prints them
def func(string):
    words = string.split()
    longest = max(words, key=len)
    return longest

line = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
print(func(line), len(func(line)))
