age = 0
positive = 0
negativo = 0

flag = True
while flag:
    ageFlag = True
    answerFlag = True
    while ageFlag:
        print("\nQuestion")
        age = input("How old are you?: ")
        if age.isalpha() or age == "":
            print("Entry invalid, please use only numbers")
            continue
        elif age.isdigit() or (age.startswith('-') and age[1:].isdigit()):
            if int(age) > 0:
                ageFlag = False
            elif int(age) <= 0:
                if positive == 0 and negativo == 0:
                    print("No entries, program finished")
                    flag = False
                    answerFlag = False
                else:
                    print(f"{positive} like programming and {negativo} dont like programming")
                    flag = False
                    answerFlag = False
            else:
                print("Entry invalid, please use only numbers")
                continue
        else:
            print("Entry invalid, please use only numbers")
            continue
        ageFlag = False

    while answerFlag:
        answer = input("Do you like programming? y/n: ")
        if not answer.isalpha():
            print("Entry invalid, please use y/yes or n/no only")
        elif answer == "y" or answer == "yes":
            positive += 1
        elif answer == "n" or answer == "no":
            negativo += 1
        else:
            print("Entry invalid, please use y/yes or n/no only")
        answerFlag = False
