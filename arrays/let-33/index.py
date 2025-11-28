array = [17,18,20,1,3,4,5,7,8,10,11,13,14,16]

def task(array):
    target = 4
    n=len(array)
    l=0
    h=n-1
    while l<=h:
        mid=(l+h)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            h=mid-1
        elif array[mid] > target:
            l=mid+1
        else:
            return -1
 
print(task(array))
