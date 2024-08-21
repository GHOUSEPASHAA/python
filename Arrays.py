# 1. Write a function to add integer values of an array
def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# 2. Write a function to calculate the average value of an array of integers
def average_of_array(arr):
    total = sum_of_array(arr)
    return total / len(arr) if len(arr) > 0 else 0

# 3. Write a program to find the index of an array element
def find_index(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1  # If element is not found

# 4. Write a function to test if array contains a specific value
def contains_value(arr, value):
    for num in arr:
        if num == value:
            return True
    return False

# 5. Write a function to remove a specific element from an array
def remove_element(arr, value):
    new_arr = []
    for num in arr:
        if num != value:
            new_arr.append(num)
    return new_arr

# 6. Write a function to copy an array to another array
def copy_array(arr):
    new_arr = []
    for num in arr:
        new_arr.append(num)
    return new_arr

# 7. Write a function to insert an element at a specific position in the array
def insert_element(arr, value, position):
    new_arr = []
    for i in range(len(arr)):
        if i == position:
            new_arr.append(value)
        new_arr.append(arr[i])
    if position >= len(arr):
        new_arr.append(value)
    return new_arr

# 8. Write a function to find the minimum and maximum value of an array
def find_min_max(arr):
    if len(arr) == 0:
        return None, None
    min_val = arr[0]
    max_val = arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

# 9. Write a function to reverse an array of integer values
def reverse_array(arr):
    new_arr = []
    for i in range(len(arr)-1, -1, -1):
        new_arr.append(arr[i])
    return new_arr

# 10. Write a function to find the duplicate values of an array
def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

# 11. Write a program to find the common values between two arrays
def find_common_values(arr1, arr2):
    common_values = []
    for num in arr1:
        if num in arr2 and num not in common_values:
            common_values.append(num)
    return common_values

# 12. Write a method to remove duplicate elements from an array
def remove_duplicates(arr):
    new_arr = []
    for num in arr:
        if num not in new_arr:
            new_arr.append(num)
    return new_arr

# 13. Write a method to find the second largest number in an array
def second_largest(arr):
    if len(arr) < 2:
        return None
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

# 14. Write a method to find the second smallest number in an array
def second_smallest(arr):
    if len(arr) < 2:
        return None
    first = second = float('inf')
    for num in arr:
        if num < first:
            second = first
            first = num
        elif num < second and num != first:
            second = num
    return second

# 15. Write a method to find the number of even and odd numbers in an array
def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

# 16. Write a function to get the difference of largest and smallest value
def difference_min_max(arr):
    min_val, max_val = find_min_max(arr)
    return max_val - min_val

# 17. Write a method to verify if the array contains two specified elements (12, 23)
def contains_two_elements(arr, elem1, elem2):
    found_elem1 = found_elem2 = False
    for num in arr:
        if num == elem1:
            found_elem1 = True
        if num == elem2:
            found_elem2 = True
    return found_elem1 and found_elem2

# 18. Write a program to remove the duplicate elements and return the new array
def remove_and_return_unique(arr):
    return remove_duplicates(arr)

# Example usage
arr = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9]

print("Sum of array:", sum_of_array(arr))
print("Average of array:", average_of_array(arr))
print("Index of element 4:", find_index(arr, 4))
print("Array contains 5:", contains_value(arr, 5))
print("Array after removing 5:", remove_element(arr, 5))
print("Copy of array:", copy_array(arr))
print("Array after inserting 10 at position 3:", insert_element(arr, 10, 3))
min_val, max_val = find_min_max(arr)
print("Minimum and Maximum values:", min_val, max_val)
print("Reversed array:", reverse_array(arr))
print("Duplicate values in array:", find_duplicates(arr))
print("Common values between two arrays:", find_common_values(arr, [2, 3, 5, 10]))
print("Array after removing duplicates:", remove_duplicates(arr))
print("Second largest value in array:", second_largest(arr))
print("Second smallest value in array:", second_smallest(arr))
even_count, odd_count = count_even_odd(arr)
print("Number of even and odd numbers:", even_count, odd_count)
print("Difference between largest and smallest values:", difference_min_max(arr))
print("Array contains 12 and 23:", contains_two_elements(arr, 12, 23))
print("Array after removing duplicates:", remove_and_return_unique(arr))
