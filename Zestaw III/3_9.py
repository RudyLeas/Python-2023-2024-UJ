#Program to return the sum of elements in a sequence into a new list
def sequence_sum(sequences):
    output = []

    for sequence in sequences:
        result = sum(sequence)
        output.append(result)

    return output

sequence1 = [[],[4],(1,2),[3,4],(5,6,7)]

print(sequence_sum(sequence1))

