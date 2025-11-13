age = 0
car_licence: ""
car_status: ""

flag = True
while flag:
    age = input("What's your age?: ")
    if age.isalpha():
        print("Entry not valid, use only numbers")
        continue
    elif int(age) <= 0 or int(age) >= 110:
        print("Age cannot be less than 0 or more than 110")
        continue
    else:
        flag = False

flag = True
while flag:
    car_licence = input("Do you have a driver's licence? y/n : ").strip().lower()
    if not car_licence.isalpha():
        print("Entry not valid, use only letters")
        continue
    elif car_licence != "y" and car_licence != "yes" and car_licence != "n" and car_licence != "no":
        print("Please select only between yes/y or no/n")
        continue
    else:
        flag = False

flag = True
while flag:
    car_status = str(
        input("Do you own a car, or have a borrowed one?\nOptions:\n- Own\n- Borrowed\n Enter here: ")).lower()
    if not car_status.isalpha():
        print("Entry not valid, use only letters")
        continue
    elif car_status != "own" and car_status != "borrowed":
        print("Please select only between 'Own' or 'Borrowed'")
        continue
    else:
        flag = False

if int(age) < 18:
    print("You're not elegible for this race, you must be 18 or higher")
elif car_licence == "n" or car_licence == "no":
    print("You're not elegible for this race, you must have a driver's licence to participate")

print(f"""\n
************CONGRATULATIONS************
¡You are elegible for the race!

|Your info:
|+ {age} years old
|+ Driver's licence: {car_licence}
|+ Racing car: {car_status.capitalize()}
""")