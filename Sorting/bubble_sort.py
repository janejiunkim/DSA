arr = input("Enter a list to bubble sort: ")

n = len(arr)
# start at beginning of array of items
for i in range(n):
    # Compare the item you're looking at to the next item in the list
    for j in range(0, n-i-1):

        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(len(arr)):
    print("%d" %arr[i])