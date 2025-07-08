age = int(input("Enter age: "))
# You cant compare string with int, so we typecaste

if age >= 18:
    print("You can drink!")
else:
    print("Fuck off!")
# Else is optional, if you want you can use

gender = input("Enter your gender: ")
if gender == "male":
    print("Welcome!")
else:
    print("Kitchen is your gaming setup!")

# Using logical operators

if (gender == "female") and (age == 16): # Logical operator and
    print("Gora badan teri patli kamar, 16-17 saal ki ummer!")
elif (gender == "male") or (gender == "female") and (age >= 16) and (age <=19):
    # elif me bhi condition hota hai!
    print("You are in VIT!")
elif gender == "trans":
    print("Train business, clapping business, #ashirvaad!")
# last wala else choice hai tumhari dalna hai dalo warna rehne do
# par agar else hai, upper koi bhi condition match na hone par else execute ho jayega
else:
    print("SEEE and SMEC ki boli lag rhi block-1 me!")

