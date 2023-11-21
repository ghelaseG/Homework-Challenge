# Find the minimum and maximum element in an array without built-in array methods:

# Start by checking if the array is empty. If it is, return a message indicating that the array is empty.

class arrayError(ValueError):
    pass

def minMax(array): # let's create a function
    if array == []: 
        return arrayError('Error: this array is empty')
    
# Initialize variables min_element and max_element with the first element of the array.

    min_element = array[0]
    max_element = array[0]

# Iterate through the array to find min and max.

    for element in array:
        if element < min_element: # compare each element with the current min_element 
            min_element = element
        elif element > max_element: # compare each element with the current max_element
            max_element = element
    

    return min_element, max_element

# Example
my_array = [3, -1, 4, 1, 5, 9, 82, 6, 5, 3, 5]
min_val, max_val = minMax(my_array)

print("Minimum element:", min_val)
print("Maximum element:", max_val)