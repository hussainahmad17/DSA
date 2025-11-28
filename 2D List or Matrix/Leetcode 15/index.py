array = [1,2,3,4,5,6,7,8,9]

def task(array):
    array.sort()
    res = []
    n=len(array)
    for i in range(n):
        if i != 0 and array[i] == array[i-1]:
            continue
        j = i+1
        k = n-1
        while j<k:
            total = array[i]+array[j]+array[k]
            if total < 0:
                j+=1
            elif total > 0:
                k-=1
            else:
                temp = [array[i],array[j],array[k]]
                res.append(temp)
                j+=1
                k-=1
                
                while j<k and array[j] == array[j-1]:
                    j+=1
                while j<k and array[k] == array[k+1]:
                    k-=1
    return res


print(task(array))
                

    