# Loops
# 1. For loop
# 2. While loop

# range function with one parameter
# only end is mentioned, starts from 0
print("Output-1")
for i in range(5): # 0-4
    # range(5) returns kind of [0,1,2,3,4]
    print(i) 
    # i += 1 happens automatically
    # i++ doesn't exits in python

# range function with two parameter
# start to end
print("\nOutput-2")
for i in range(1, 7): # 1 to 6
    print(i)
# range function with three parameter
# start, end, step
print("\nOutput-3")
for i in range(0, 5, 2):
    print(i)

# decrement
print("\nOutput-4")
for i in range(6, 2, -1):
    print(i)

print("\nOutput-5")
# while loop
ind = 1
while ind <= 10:
    print(f"5 x {ind} = {5 * ind}")
    # Important part
    # Never forget to increment/decrement
    ind += 1



