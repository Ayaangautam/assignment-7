def remove_duplicates(arr):
    return list(set(arr))

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Get the input array from the user
arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))

# Remove duplicates from the array
unique_arr = remove_duplicates(arr)

# Sort the array using selection sort
selection_sorted_arr = selection_sort(unique_arr)

# Sort the array using bubble sort
bubble_sorted_arr = bubble_sort(unique_arr)

# Print the sorted arrays
print("Sorted array using selection sort:", selection_sorted_arr)
print("Sorted array using bubble sort:", bubble_sorted_arr)

