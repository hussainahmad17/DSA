# def task(matrix):
#     r=len(matrix)
#     c=len(matrix[0])
#     for i in range(r):
#         for j in range(c):
#             if matrix[i][j] == 0:
#                 markinf(matrix,i,j)
#     for i in range(r):
#         for j in range(c):
#             if matrix[i][j] == float('inf'):
#                 matrix[i][j] = 0



# def markinf(matrix,row,col): 
#     r=len(matrix)
#     c=len(matrix[0])
#     for i in range(r):
#         if matrix[i][col] != 0:
#             matrix[i][col] = float('inf')
#     for j in range(c):
#         if matrix[row][j] != 0:
#             matrix[row][j] = float('inf')



# optimal approach

# TC is o(2(n*m)) = o(n*m) 
# Sc is o(n+m)
def task(matrix):
    r=len(matrix)
    c=len(matrix[0])

    rowtrack = [0 for _ in range(r)]
    coltrack = [0 for _ in range(c)]

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                rowtrack[i] = 1
                coltrack[j] = 1

    for i in range(r):
        for j in range(c):
            if rowtrack[i] == 1 or coltrack[j] == 1:
                matrix[i][j] = 0

