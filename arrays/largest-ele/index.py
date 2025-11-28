array = [12,34,67,89,211,90]
max_ele = array[0]
n=len(array)
for i in range(0,n):
    if array[i]>max_ele:
        max_ele = array[i]
print(max_ele)