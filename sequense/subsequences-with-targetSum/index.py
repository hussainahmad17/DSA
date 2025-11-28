target = 9
array = [12,34,56]
result = []
def subquences(ind,total,subset):
    if total == target:
        result.append(subset.copy())
        return
    elif total>target:
        return
    if ind >= len(array):
        return

    subset.append(array[ind])
    sum = total+array[ind]
    subquences(ind+1,sum,subset)
    e=subset.pop()
    sum=sum-e
    subquences(ind+1,sum,subset)