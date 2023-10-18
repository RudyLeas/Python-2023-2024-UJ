# program that prints words in a string in alphabetical order, and ascending lentgh order
def wordsort(line):
    words = line.split()
    words.sort()
    return words


def word_length_sort(line):
    words = line.split()
    words.sort(key=len)
    return words


line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
print(' '.join(wordsort(line)))

print(' '.join(word_length_sort(line)))
