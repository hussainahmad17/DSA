array = [1,99,101,98,2,5,3,100]

def task(array):
    maxcount = 0
    for i in range(len(array)):
        num = array[i]
        count = 1
        while num+1 in array:
            count += 1
            num = num+1
        maxcount = max(maxcount,count)   

    return maxcount   

print(task(array))


# optimal solution

array = [1,23,34,3,4,5,78,90,35,21]

array.sort()

    