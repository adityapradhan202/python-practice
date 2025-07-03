# Variables are nothing but containers
# Python variables are not static
# It means you dont have to mention the type of variable initially
# Type is automatically decided by it's value
# That is variables are dynamically defined here

# Naming conventions of variables
# 1. Variable name can't be a keyword - keyword means defined terms in python
# For example if, else, in, is, not
# 2. Never name the variable starting wihth number
# For example 1a, 23b, 45age, 2name
# 3. By default, it is recommended by official python docs that snake case should be used for variable names
# For example: CamelCase: AnimalType, pascalCase: animalType, snake_case: animal_type\

# Note: Type function is used to get the type of variable

a = 5
print(f"Value of a is {a}, and its type is {type(a)}")

a = 6.7
name = "Nitin"
bool_variable = True

print(f"a = {a}, name = {name}, bool_variable = {bool_variable}")
print(f"Type of a = {type(a)}, type of name = {type(name)}, type of bool_variable = {type(bool_variable)}")

# Homework (google it)
# .format method on python strings while printing