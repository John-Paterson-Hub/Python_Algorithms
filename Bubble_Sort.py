# starting at the front of the array
# if the second place is greater then the first place swap the location of them 
# if the first is less then the second move onto the next pair
# use a for loop to progress threw the array 
# use another loop to rerun threw the array and sort the rest

def bubblesort(arr):
  numLen = len(arr)-1
  for x in range(numLen):
    for i in range(numLen-1):
      if arr[i] > arr[i+1]:
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
  print(arr)

bubblesort([5,2,4,3,1,7]) #simple numbers
bubblesort([9,2,4,7,6,8,5,3,765]) #outlier
bubblesort([-5,1,-3,-1,7]) #positives and negatives
