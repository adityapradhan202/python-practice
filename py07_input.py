# input is an built in function to take user input from the terminal or console or cmd

user_input = input("Enter an integer: ")
print(f"Given input = {user_input}")

# By default input function retruns strings
print(f"Type of user_input = {type(user_input)}")

# Type casting can be used
user_input2 = input("Give me an integer: ")
user_input2 = int(user_input2)
print(f"Type of user_input2 = {type(user_input2)}")

