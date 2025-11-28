# TC is o(n)
array = [12,45,78,23,90,12,56,78]
n=len(array)
array[:] = [array[n-1]]+array[0:n-1]
print(array)

# second way

array = [12,45,67,873,23,56,34]
def task(array):
    n=len(array)
    temp = array[n-1]
    for i in range(n-2,-1,-1):
        array[i+1] = array[i]
    array[0]=temp

task(array)
print(array)