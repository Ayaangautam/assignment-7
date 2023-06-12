def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Get the number of students from the user
n = int(input("Enter the number of students: "))

# Create an empty list to store the marks
marks = []

# Get the marks for each student
for i in range(n):
    mark = int(input(f"Enter the mark for student {i+1}: "))
    marks.append(mark)

# Sort the marks using merge sort
sorted_marks = merge_sort(marks)

# Print the final sorted list
print("List after sorting is:", sorted_marks)
