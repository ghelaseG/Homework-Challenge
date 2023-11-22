# Write a program to reverse the array without built-in array methods

## Find the length of the array 
def reverseArr(array):
    array_length = 0
    for _ in array:
        array_length += 1

## Initialize variables start and end to represent the start and end indices of the array.
    start = 0
    end = array_length - 1

## Use a while loop to iterate until start is less than end.
    while start < end:
        array[start], array[end] = array[end], array[start] # swap the elements at indices start and end.
## Move start index towards the end of the array and end index towards the start of the array.        
        start += 1
        end -= 1

## Return the reversed array.
    return array

# Example usage:
exp_array = [10, 20, 30, 40, 50]
reverseArr(exp_array)
print("Reversed Array:", exp_array)