
# VARIABLES AND DATA TYPES
# =========================

# Variable
x = 5
print(x)

# String
name = 'Ritu'
print(name)

# Float
y = 566.89
print(y)

# Addition
a = 9
b = 6
x = a + b
print(x)

# Tuple
fruits = ('orange', 'mango', 'apple')
print(fruits)

# List
fruit = ['orange', 'mango', 'apple']
fruit.append('grapes')
fruit.remove('orange')
print(fruit)

# Set - Mutable
unique_number = {1, 2, 3, 3, 5, 5, 6, 7, 7}
print(unique_number)

# Frozenset - Immutable
immutable_number = frozenset([12, 2, 12, 4, 6, 6])
print(immutable_number)


# =========================
# BASIC PRACTICE QUESTIONS
# =========================

# 1. Create an integer variable age and store your age. Print it.
age = 20
print(age)

# 2. Create a float variable height and store your height. Print it.
height = 5.8
print(height)

# 3. Create a string variable name and print:
# My name is <your_name>
name = 'RITU'
print("My name is", name)

# 4. Create a boolean variable is_student and print the variable and its data type.
is_student = True
print(is_student)
print(type(is_student))

# 5. Create variables and print their data types.
x = 10
y = 3.14
z = 'Python'

print(type(x))
print(type(y))
print(type(z))

# 6. Create a list of 5 fruits. Print the third fruit.
Fruits = ['apple', 'mango', 'banana', 'grapes', 'kiwi']
print(Fruits[2])

# 7. Create a tuple of 5 numbers. Print the first element.
Numbers = (1, 2, 3, 4, 5)
print(Numbers[0])

# 8. Create a set and observe duplicate values.
number_set = {10, 20, 30, 20, 10}
print(number_set)

# 9. Create a dictionary and print only the name.
student = {
    "name": "Rahul",
    "age": 20,
    "city": "Mumbai"
}

print(student["name"])
print(student.get("age"))

# 10. Print each variable and its data type.
name = "Rahul"
age = 20
salary = 50000.50
is_student = True

print(name, type(name))
print(age, type(age))
print(salary, type(salary))
print(is_student, type(is_student))

