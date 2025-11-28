array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def task(array):
    pos = []
    neg = []
    for i in range(len(array)):
        if array[i] >= 0:
            pos.append(array[i])
        else:
            neg.append(array[i])
    for i in range(len(neg)):
        array[2 * i] = pos[i]
        array[2 * i + 1] = neg[i]
    return array

print(task(array))


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def task(array):
    res = [0] * len(array)
    pos = 0
    neg = 1
    for i in range(len(array)):
        if array[i] >=0:
            res[pos] = array[i]
            pos += 2
        else:
            res[neg] = array[i]
            neg += 2
    return res

print(task(array))