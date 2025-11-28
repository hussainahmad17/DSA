# remove the duplicates

array = [12,12,34,34,40,67,70,90,108,108,156,267,267]
res = []
for i in range(len(array)):
    if array[i] != array[i-1]:
        res.append(array[i])

print(len(res))