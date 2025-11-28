array = [1,2,2,2,3,3,3,3,3,99,34,6,7,9]

def task(array):
    array.sort()  # Binary search works only on sorted array
    target = 3
    n = len(array)

    # Find lower bound
    l, h = 0, n-1
    lb = -1
    while l <= h:
        mid = (l+h)//2
        if array[mid] >= target:
            lb = mid
            h = mid-1
        else:
            l = mid+1

    # Find upper bound
    l, h = 0, n-1
    ub = -1
    while l <= h:
        mid = (l+h)//2
        if array[mid] > target:
            ub = mid-1
            h = mid-1
        else:
            l = mid+1

    return (lb, ub, ((ub-lb)+1))

print(task(array))
