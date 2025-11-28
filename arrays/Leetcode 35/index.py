array = [12,34,56,78,90,100]
def task(array):
    n=len(array)
    target = 91
    l=0
    h=n-1
    while l<h:
        mid = (l+h)//2
        if array[mid] <= target:
            index=mid
            l=mid+1
        elif array[mid] == target:
            return mid
        else:
            h=mid-1
    return index


print(task(array))
    