# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# def task(matrix):
#     r=len(matrix)
#     c=len(matrix[0])

#     for i in range(r):
#         for j in range(c):
#             print(matrix[i][j])


# print(task(matrix))



# array = [12,14,53,45,9]

# def task(array):
#     target = 23
#     total = 0
#     max_total = 0
#     for i in range(len(array)-1):
#         if array[i] + array[i+1] == target:
#             return (array[i],array[i+1])
    
# print(task(array))



# # optimized
# array = [12, 14, 53, 45, 9]

# def task(array):
#     target = 23
#     seen = set()
    
#     for num in array:
#         diff = target - num
#         if diff in seen:
#             return (diff, num)
#         seen.add(num)
    
#     return None

# print(task(array))



# array = [12,34,123,56,78,1,3,56,89,90,11]

# def task(array):
#     array.sort()
#     target = 134
#     n=len(array)
#     for i in range(n-1):
#         if array[i]+array[i+1] == target:
#             return (i,i+1)
        
# print(task(array))


# array = [12,34,45,67,78,89,90]

# def task(array):
#     for i in range(len(array)-1):
#         if array[i+1]<array[i]:
#             return False
#         else:
#             return True

# print(task(array))


# array = [4,5,6,7,0,1,2]

# def task(array):
#     min_value = array[0]
#     for i in range(len(array)-1):
#         if array[i+1]<min_value:
#             min_value = array[i+1]
#     return min_value
        
# print(task(array))


