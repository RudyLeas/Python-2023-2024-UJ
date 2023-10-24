# program to print a string made out of first and last letters of words in a sentence
def func(sentence):
    return ''.join([word[0] for word in sentence.split()])
def func2(sentence):
    return ''.join([word[-1] for word in sentence.split()])
line = 'I am a cat and I have a ling whiskers and furry paws'
print(func(line))
print(func2(line))
