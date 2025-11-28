array = [12,67,34,90,45,24]
 
def task(array):
    for i in range(0,len(array)-1):
        if array[i]>array[i+1]:
            return False
    return True
   
print(task(array))