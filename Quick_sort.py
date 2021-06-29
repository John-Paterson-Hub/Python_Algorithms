
# select last number for pivot point 
# iterate threw the array compairing the value to the pivot point
# if value is smaller then our pivot point add it to the list for smaller values
# if the value is larger then the pivot point add it to the list for larger values
# apply this method again for the two separate lists created
# return the sorted list

# Quick Sort

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_smaller = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_smaller.append(item)

    return quick_sort(items_smaller) + [pivot] + quick_sort(items_greater)

arr = [4,3,12,5,4,2,8,7,5]

print(quick_sort(arr))
