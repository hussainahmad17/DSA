# TC is o(n+n) = o(2n) = o(n)
def second_largest(array):
    max_ele = float("-inf")
    sec_max_ele = float("-inf")
    n = len(array)

    # First find the maximum
    for i in range(n):
        if array[i] > max_ele:
            max_ele = array[i]

    # Then find the second maximum
    for j in range(n):
        if array[j] > sec_max_ele and array[j] < max_ele:
            sec_max_ele = array[j]

    return sec_max_ele


array = [12, 90, 56, 3, 23, 8, 89]
print(second_largest(array))  # Output: 89



# optimal solution

array = [12,90,45,23,89,46,200]

def task(array):
    n=len(array)
    largest = float('-inf')
    s_largest = float('-inf')   

    for i in range(n):
        if array[i]>largest:
            s_largest = largest
            largest = array[i]
        elif array[i] < largest and array[i] > s_largest:
            s_largest = array[i]
    return s_largest

res = task(array)
print(res)
