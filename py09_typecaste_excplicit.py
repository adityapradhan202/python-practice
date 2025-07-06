# Type casting - Means converting one type into another type
# Type casting are of two types:
# 1. Implicit typecasting - On its own, automatic
# 2. Explicit typecasting - This done by us, manually

# 1. Converting integer into float
a = 9
print(f"Type of a: {type(a)}")
# Type casting a into float
a_float = float(a)
print(f"Type of a_float: {type(a_float)}")
print(f"Value of a_float: {a_float}")

# 2. Converting float into integer
b = 9.999456
b_int = int(b) # Fractional part will be removed
# b_round = round(b, 2)
print(f"Type of b_int: {type(b_int)}")
print(f"Value of b_int: {b_int}")

# 3. Converting a string into integer
str_int = "567"
integer = int(str_int)
print(f"integer = {integer}, type = {type(integer)}, type of str_int = {type(str_int)}")
# if str_int = 56.7, int(str_int) will throw error

# 4. Covnerting a string into float
float_str = "567.67"
float_var = float(float_str)
print(f"float_var = {float_var}, type = {type(float_var)}, type of float_str = {type(float_str)}")

print()
# 5. Type casting this float_str into integer, in one line
float_int = int(float(float_str))
print(f"float_int = {float_int}, type = {type(float_int)}")

# 6. Converting a integer or float into a string
v1, v2 = 5.6, 7
v1_str = str(v1) # v1_str becomes "5.6" (text/string)
v2_str = str(v2)
print(f"Type of v1_str, and v2_str, {type(v1_str)}, {type(v2_str)}")

# In python we dont have character
# But a string with length - 1 can be considered as character
c1 = "A"
# ord method converts a character into ascii code
ascii_val = ord(c1)
print(f"ascii_val = {ascii_val}")
# chr method converts ascii integer values into corresponding character or alphabet
print(f"chr(ascii_val+1) = {chr(ascii_val + 1)}, ascii of this = {ord("B")}")