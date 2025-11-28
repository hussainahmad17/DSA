array=[2,45,67,98,45,23,56,79,90,23]

def task(array,left,right):
    while left<right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array

print(task(array,0,len(array)-1))
  