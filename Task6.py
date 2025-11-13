numbers = []
count = 1
text = ""

while True:
    data = input(f"Enter the {count} of 3 numbers: ")
    if data.isalpha():
        print("Must be numbers only")
        continue
    else:
        numbers.append(int(data))
        count += 1
        if len(numbers) == 3: break

if numbers[0] > 0 and numbers[1] > 0 and numbers[2] > 0:
    text += "All 3 numbers are positives"

if numbers[0] < 0 or numbers[1] < 0 or numbers[2] < 0:
    text += "Theres at least one negative number"

if numbers[0] == 0 and numbers[1] != 0 and numbers[2] != 0:
    text += "There's only one number which is 0, the first one"
elif numbers[0] != 0 and numbers[1] == 0 and numbers[2] != 0:
    text += "There's only one number which is 0, the second one"
elif numbers[0] != 0 and numbers[1] != 0 and numbers[2] == 0:
    text += "There's only one number which is 0, the third one"

if text: print(text)
print("Program ended")