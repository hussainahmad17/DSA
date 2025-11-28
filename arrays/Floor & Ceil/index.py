array = [12,34,56,78,90,120]

def task(array):
    target = 912
    n=len(array)
    ceil = -1
    floor = -1
    l=0
    h=n-1
    while l<=h:
        mid = (l+h)//2
        if array[mid] == target:
            return (array[mid],array[mid])
        elif array[mid] < target:
            floor = array[mid]
            l=mid+1
        else:
            ceil = array[mid]
            h=mid-1
    return (floor,ceil)

print(task(array))
