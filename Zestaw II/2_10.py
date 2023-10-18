# function that counts the number of words in a text file
def word_count(filename):
    with open(filename, 'r') as file:
        text = file.read()
        result = len(text.split())
        return result


filename = 'text.txt'
print(f'File contains {word_count(filename)} words.')
