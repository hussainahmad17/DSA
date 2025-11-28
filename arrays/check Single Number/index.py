array = [1,2,34,4,45,1,2,7,8]

def task(array):
    hash_map = {}
    for val in array:
        hash_map[val] = hash_map.get(val,0)+1
    
    for i in hash_map:
        if hash_map[i] == 1:
            return i
        

print(task(array))
