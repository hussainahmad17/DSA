array = [19, 7, 6, 12, 15, 2, 5, 8, 11, 10]
stack = []

def task(array,index=0):

    if index == len(array):
        return
    
    next_greater = -1
    for i in range(index+1,len(array)):
        if array[i]>array[index]:
            next_greater = array[i]
            break

    stack.append(next_greater)
    task(array,index+1)
    return stack

print(task(array,0))