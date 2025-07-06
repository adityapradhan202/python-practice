a = 201
a_str = str(a)

# "201"
# 0 index = 2, 1 = 0, at 2 we have 1

index = 0
sum = 0
while index < len(a_str):
    digit = a_str[index]
    digit = int(digit)
    sum += digit # sum = sum + digit
    index += 1
# Loop ended here

print(f"Sum = {sum}")
