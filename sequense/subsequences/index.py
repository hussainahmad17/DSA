array = [12,34,6]
result = []
subset = []
def subsequences(ind,subset):
    if ind>=len(array):
        result.append(subset.copy())
        return
    subset.append(array[ind])
    subsequences(ind+1,subset)
    subset.pop()
    subsequences(ind+1,subset)