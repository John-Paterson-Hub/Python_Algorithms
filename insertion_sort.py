# Divide unsorted list into 2 sub lists
# The sorted list will start with a length of 1 and comprised of the first value in the initial lit
# All other items will go into the unsorted list
# Take farthest left item in the unsorted list and move it into the sorted list
# Compair this to the value to the value on its left if this value is larger swap position
# If value is smaller then the value being sorted it is in the correct position
# Continue threw to the next iteration of the unsorted list


# Insertion Sort

def insertion_sort(sequence):
    indexing_length = range(1, len(sequence))
    for i in indexing_length:
        value = sequence[i]

        while sequence[i-1] > value and i > 0:
            sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
            i = i -1
    return sequence

print(insertion_sort([5,3,7,4,9]))
