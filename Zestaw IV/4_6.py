#program that calculates sum of the sequence with nested sequences inside
def sum_seq(sequence):
    sum=0
    for i in sequence:
        if isinstance(i,(list,tuple)):
            sum+=sum_seq(i)
        else:
            sum+=i
    return sum
sequence1 = [[],[4],(1,2),[3,4],(5,6,7)]
print(sum_seq(sequence1))
