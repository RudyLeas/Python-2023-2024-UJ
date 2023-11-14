#program to flatten the sequence with possible nested sequences inside
def flatten(sequence):
    result=[]
    for i in sequence:
        if isinstance(i,(list,tuple)):
            result+=flatten(i)
        else:
            result.append(i)
    return result
sequence1 = [[([])],[4],(1,2),[3,4],(5,6,7)]
print(flatten(sequence1))