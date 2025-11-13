namesList = []

while True:
    name = input("Enter a name (Or end to finish): ")

    if not name.isalpha():
        name = input("Invalid input. Please enter a valid name (letters only): ")
        continue
    elif name == "End" or name == "end":
        print("Program ended")
        break

    namesList.append(name)

text = f"There are {len(namesList)} names"

flag = False
for i in range(len(namesList)):
    for j in range(i + 1, len(namesList)):
        if namesList[i] == namesList[j]: flag = True

if flag: text += " and there are repeated names."

print(text)
