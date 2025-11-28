array = [12,45,78,90,4,23,6,78,9,123]
def task(array,k):
    n=len(array)
    for _ in range(0,k):
        array[:] = [array[n-1]] + array[0:n-1]
    return array

print(task(array,3))

# optimal solution
# TC is o(n) as to slice from (n-k) to end is o(k) and to slice from start to (n-k) is o(n-k) so overall it is o(n)
# SC is o(1)
array = [12,45,78,90,4,23,6,78,9,123]
def task(array, k ):
    n=len(array)
    k=k%n # to handle cases where k > n
    array[:] = array[n-k:] + array[:n-k]
    return array

print(task(array,3))

# leetcode solution
# TC is o(n)
# SC is o(1)
array = [12,45,78,90,4,23,6,78,9,123]
n=len(array)
k=3
k=k%n
def reverse(array,left, right):
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    

reverse(array, n-k, n-1) # o(k/2)
reverse(array, 0, n-k-1) # o((n-k)/2)
reverse(array, 0, n-1) # o(n/2)
print(array)

