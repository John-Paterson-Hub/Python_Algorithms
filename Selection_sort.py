arr = [3, 2, 5, 4, 6]

def Selection_sort(arr):
    array_length = len(arr)-1
    for i in range(0, array_length):
        min = arr[i]
        for x in range(i+1, array_length):
            if min > arr[x]:
                temp = arr[x]
                arr[x] = arr[i]
                arr[i] = temp
    return arr

arr = Selection_sort(arr)
print(arr)
