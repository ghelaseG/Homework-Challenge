# Pseudocode

# Write a program to sort the given array without built-in array methods:
def sort(array):

# Get the length of the array (n).
    n = len(array)
# Iterate through the array using a loop with the index i ranging from 0 to n-1.
    for i in range(n):

# Assume the current index i as the minimum index (min_index).
        min_index = i
# Nested loop: Iterate through the unsorted part of the array, starting from index i+1 to n-1.
        for j in range(i+1, n):
# Inside the nested loop, compare elements and update min_index if a smaller element is found.
            if array[j] < array[min_index]:
                min_index = j
# Swap the element at index i with the element at the found min_index.
        array[i], array[min_index] = array[min_index], array[i]
# Return the sorted array.
    return array

# Example usage:
my_array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Sorted array:", sort(my_array))  
