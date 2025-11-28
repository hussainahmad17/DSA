# # TC and SC is o(n)
# array = [23,0,23,23,6,0,89,0,0,45]
# temp = [] # in worst case it will be o(n)
# n=len(array)
# for i in range(n): # tc is o(n)
#     if array[i] != 0:
#         temp.append(array[i])

# n2 = len(temp)
# for i in range(n2):      
#     array[i] = temp[i]
#                             # tc is o(n)
# for i in range(n2,n):
#     array[i] = 0
# print(array)


# optimal solution

# array = [0,1,0,3,12]

# def task(array):
#     n=len(array)
#     for i in range(n):
#         for j in range(i+1,n):
#             if array[i] == 0 and array[j] != 0:
#                 array[i], array[j] = array[j], array[i]
#                 break

#     return array    

# print(task(array))


# leetcode solution
array = [0,1,0,3,12]
def task(array):
    n = len(array)
    last_non_zero_index = 0
    
    for i in range(n):
        if array[i] != 0:
            array[last_non_zero_index] = array[i]
            last_non_zero_index += 1
            
    for i in range(last_non_zero_index, n):
        array[i] = 0
        
    return array

print(task(array))