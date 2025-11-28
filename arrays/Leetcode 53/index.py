array = [12,44,67,34,12-1,-45,-67,15,1,67,8]
# TC is O(n^2)
def task(array):
    max_sum = float('-inf')
    for i in range(len(array)):
        total = 0
        for j in range(i, len(array)):
            total += array[j]
            max_sum = max(max_sum, total)
    return max_sum

print(task(array))


# optimal solution
# TC is O(n) ans SC is O(1)
array = [12,44,67,34,12-1,-45,-67,15,1,67,8]

def task(array):
    total = 0
    max_sum = float('-inf')
    for i in range(len(array)):
        total += array[i]
        max_sum = max(max_sum, total)
        if total < 0:
            total = 0
    return max_sum

print(task(array))
