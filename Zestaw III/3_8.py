# program to find intersection and union of two sequences
seq1 = [1, 2, 3, 4, 5]
seq2 = [4, 5, 6, 7, 8]

intersection = list(set(seq1) & set(seq2))
print(intersection)
union = list(set(seq1) | set(seq2))
print(union)
# works also for strings
string1 = "abcdefg"
string2 = "defghij"
intersection = list(set(string1) & set(string2))
print(intersection)
union = list(set(string1) | set(string2))
print(union)
