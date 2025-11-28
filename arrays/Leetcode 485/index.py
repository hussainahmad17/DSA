# TC is o(n) and SC is o(1)
# nums = [1, 0, 1, 1, 1, 0, 1]
# def findMaxConsecutiveOnes(nums):
#     n= len(nums)
#     count = 0
#     max_count = 0
#     for i in range(n):
#         if nums[i] == 1:
#             count += 1
#             max_count = max(max_count, count)
#         else:
#             count = 0
#     return max_count

# result = findMaxConsecutiveOnes(nums)
# print(result) 


array = [12,45,23,89,56,899,235,67,34,90,12,45,67,89,23,56]

def task(array):
    n=len(array)
    largest = float('-inf')
    s_largest = float('-inf')
    for i in range(n):
        if array[i] > largest:
            s_largest = largest
            largest = array[i]
        elif array[i] > s_largest and array[i] < largest:
            s_largest = array[i]
    return largest, s_largest

result = task(array)
print("Largest:", result[0])
print("Second Largest:", result[1])

