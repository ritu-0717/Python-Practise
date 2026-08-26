
#  LIST, TUPLE AND SET
# ==========================================



# 1. LIST
# ==========================================

# Definition:
# A list is an ordered and mutable collection of elements.
# It allows duplicate values and can store different data types.

fruits = ["apple", "banana", "mango", "apple"]

print("List:", fruits)

# List allows duplicate values
print("Duplicate value:", fruits)

# Accessing list elements
print("First element:", fruits[0])

# Adding an element
fruits.append("orange")
print("After append:", fruits)

# Changing an element
fruits[1] = "grapes"
print("After changing:", fruits)

# Removing an element
fruits.remove("apple")
print("After remove:", fruits)



# 2. TUPLE
# ==========================================

# Definition:
# A tuple is an ordered and immutable collection of elements.
# It allows duplicate values and can store different data types.

colors = ("red", "blue", "green", "red")

print("\nTuple:", colors)

# Tuple allows duplicate values
print("Duplicate value:", colors)

# Accessing tuple elements
print("First element:", colors[0])

# Tuple cannot be changed
# colors[1] = "yellow"   # This will give an error



# 3. SET
# ==========================================

# Definition:
# A set is an unordered and mutable collection of unique elements.
# It does not allow duplicate values.

numbers = {10, 20, 30, 40, 20}

print("\nSet:", numbers)

# Duplicate value is automatically removed
print("Set with unique values:", numbers)

# Adding an element
numbers.add(50)
print("After add:", numbers)

# Removing an element
numbers.remove(20)
print("After remove:", numbers)


