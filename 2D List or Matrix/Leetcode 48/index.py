# Rotate Matrix by 90 Degrees
matrix = [[1,2,3],[4,5,6],[7,8,9]]
def task(matrix):
    n=len(matrix)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n-1-i] = matrix[i][j]
    return res


print(task(matrix))


# optimal solution
matrix = [[1,2,3],[4,5,6],[7,8,9]]

def task(matrix):
    n=len(matrix)

    for i in range(n):
        for j in range(i+1,n): # (i+1) to avoid diognal elements swapping
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

    return matrix

print(task(matrix))



