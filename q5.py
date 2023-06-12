def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

# Get the input array from the user
arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))

# Sort the array
sorted_arr = sorted(arr)

# Print the sorted array
print("Sorted array:", sorted_arr)

# Get the element to search from the user
element = int(input("Enter the element to search: "))

# Perform binary search
index = binary_search(sorted_arr, element)

if index != -1:
    # Count the occurrences of the element
    occurrences = count_occurrences(sorted_arr, element)
    print(f"Number of occurrences of element {element} is: {occurrences}")
else:
    print("Element not found in the array.")

