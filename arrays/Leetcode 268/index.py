#TC is o(n^2) and SC is o(1)
array = [0,4,3,2,1] # n=5
def task(array):
    n=len(array)
    for i in range(n+1):
        if i not in array:
            return i
        
print(task(array))

# optimal solution
# TC is o(n) and SC is o(n)
array = [0,4,3,2,1]
dict = {}
def task(array):
    for i in range(len(array)+1):
        dict[i] = 0
    for i in range(len(array)):
        dict[array[i]] = 1
    for k,v in dict.items():
        if v == 0:
            return k
        
print(task(array)) 


# leetcode solution

array = [0,4,3,2,1]

def task(array):
    n=len(array)
    return n*(n+1)//2 - sum(array)

print(task(array)) 

        
        
    