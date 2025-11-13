flag = True
while flag:
    age = input("Enter your age: ").strip()

    if age.isalpha():
        print("Entry not valid, please use numbers for age")
        continue
    elif int(age) <= 0 or int(age) > 110:
        print("Age cannot be 0, less than 0 or more than 110")
        continue
    else:
        flag = False

flag = True
while flag:
    if int(age) <= 6: break
    print("""
-----Select one option-----
| Are you currently:
|- Studying
|- Working
|- None
    """)
    educationalLevel = input("Your option: ").strip().lower()
    if not educationalLevel.isalpha():
        print("Option not valid, please use only letters")
        continue
    elif educationalLevel != "studying" and educationalLevel != "working" and educationalLevel != "none":
        print("Option not valid, please use only one of the above")
        continue
    else:
        flag = False

if 0 < int(age) < 6:
    print("\nYou're a kindergarten".center(20, "*"))
elif 6 <= int(age) <= 17 and educationalLevel == "studying":
    print("\nYou're at school".center(20, "*"))
elif 18 <= int(age) <= 25 and educationalLevel == "studying":
    print("\nYou're a university student".center(20, "*"))
elif 25 < int(age) <= 60 and educationalLevel == "working":
    print("\nYou're an Active adult".center(20, "*"))
elif 60 < int(age) <= 110 and educationalLevel == "none":
    print("\nYou're a retired older adult".center(20, "*"))
else:
    print("\n", "Not determined".center(20, "*"))