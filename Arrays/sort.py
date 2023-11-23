# Pseudocode

# Write a program to sort the given array without built-in array methods:

# Get the length of the array (n).

# Iterate through the array using a loop with the index i ranging from 0 to n-1.

# Assume the current index i as the minimum index (min_index).

# Nested loop: Iterate through the unsorted part of the array, starting from index i+1 to n-1.

# Inside the nested loop, compare elements and update min_index if a smaller element is found.

# Swap the element at index i with the element at the found min_index.

# Continue this process until the outer loop completes, resulting in a sorted array.

# Return the sorted array.