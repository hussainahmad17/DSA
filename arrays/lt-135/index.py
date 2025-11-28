array = [7,8,9,1,2,3,4]

def task(array):
    mini = float("inf")
    n=len(array)
    l=0
    h=n-1
    while l<=h:
        mid = (l+h)//2
        if array[l]<=array[mid]:
            mini = min(mini,array[l])
            l=mid+1
        else:
            mini = min(mini, array[mid])
            h = mid - 1

    return mini

print(task(array))



