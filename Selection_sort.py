# find the minimum value and swap it with the first element
# start position at 0 and each iteration increasing where the position is swapped
# once entire array is sorted return the new array

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
