array1 = [12, 34, 69, 89, 100]
array2 = [12, 23, 34, 45, 56, 67, 78, 89, 90, 100]

def merge_without_duplicates(array1, array2):
    res = []
    i, j = 0, 0
    n1, n2 = len(array1), len(array2)

    while i < n1 and j < n2:
        if array1[i] < array2[j]:
            if not res or res[-1] != array1[i]:
                res.append(array1[i])
            i += 1
        elif array1[i] > array2[j]:
            if not res or res[-1] != array2[j]:
                res.append(array2[j])
            j += 1
        else:  # both are equal
            if not res or res[-1] != array1[i]:
                res.append(array1[i])
            i += 1
            j += 1

    # Add remaining elements
    while i < n1:
        if not res or res[-1] != array1[i]:
            res.append(array1[i])
        i += 1

    while j < n2:
        if not res or res[-1] != array2[j]:
            res.append(array2[j])
        j += 1

    return res

print(merge_without_duplicates(array1, array2))
