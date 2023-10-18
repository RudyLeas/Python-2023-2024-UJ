# program that finds a sum of words lengths in a string
def func(sentence):
    return sum([len(word) for word in sentence.split()])


line = 'I am a cat and I have a ling whiskers and furry paws'
print(func(line))
