import array

# Importing the array module

# Creating an array
arr = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements
print("First element:", arr[0])
print("Second element:", arr[1])

# Adding elements
arr.append(6)
print("Array after appending 6:", arr)

# Inserting elements
arr.insert(2, 9)
print("Array after inserting 9 at index 2:", arr)

# Removing elements
arr.remove(3)
print("Array after removing 3:", arr)

# Popping elements
popped_element = arr.pop()
print("Popped element:", popped_element)
print("Array after popping an element:", arr)

# Finding the index of an element
index = arr.index(4)
print("Index of element 4:", index)

# Reversing the array
arr.reverse()
print("Array after reversing:", arr)

# Getting the length of the array
length = len(arr)
print("Length of the array:", length)
# List operations

# Creating a list
lst = [1, 2, 3, 4, 5]

# Accessing elements
print("First element of list:", lst[0])
print("Second element of list:", lst[1])

# Adding elements
lst.append(6)
print("List after appending 6:", lst)

# Inserting elements
lst.insert(2, 9)
print("List after inserting 9 at index 2:", lst)

# Removing elements
lst.remove(3)
print("List after removing 3:", lst)

# Popping elements
popped_element_list = lst.pop()
print("Popped element from list:", popped_element_list)
print("List after popping an element:", lst)

# Finding the index of an element
index_list = lst.index(4)
print("Index of element 4 in list:", index_list)

# Reversing the list
lst.reverse()
print("List after reversing:", lst)

# Getting the length of the list
length_list = len(lst)
print("Length of the list:", length_list)

# Difference between array and list:
# 1. Arrays are more efficient for numerical operations and require all elements to be of the same type.
# 2. Lists are more flexible and can contain elements of different types.
# 3. Arrays are part of the array module, while lists are built-in data structures in Python.