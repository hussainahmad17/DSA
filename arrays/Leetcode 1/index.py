array = [12,34,56,78,90,13]
target = 124

def find_target_sum(array, target):
    res = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                res.append((i, j))    
    return res

print(find_target_sum(array, target))



# optimal solution

array = [12,34,56,78,90,13]
target = 124 
def task(array , target):
    res = {}
    for i in range(len(array)):
        remin = target - array[i]
        if remin in res:
            return res[remin], i
        res[array[i]] = i
    
task(array, target)
print(task(array, target))
 