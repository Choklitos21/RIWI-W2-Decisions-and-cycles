name = ""
code = 0
user = {}
allowedAccounts = [
    {
        "name": "Choklitos",
    },
    {
        "name": "Zelda",
    }
]

flag = True
while flag:
    name = input("Enter your username (Caps will be taken) : ")
    for i in allowedAccounts:
        if i["name"] == name:
            user = i
            break
    if not user:
        print("*************ACCESS DENIED*************\nYou're not registered")
        continue
    flag = False

flag = True
while flag:
    code = input("Enter your code\nIt must be a multiple of 2 or end in 7\nEnter here: ").strip()
    if code.isalpha():
        print("Use only numbers")
        continue
    elif int(code) < 0:
        print("Cannot use negative numbers")
        continue
    elif (int(code) % 2) == 0:
        print("*************ACCESS GRANTED*************")
        break
    elif list(str(int(code)))[-1] == "7":
        print("*************ACCESS GRANTED*************")
        break
    else:
        print("*************ACCESS DENIED*************\nCode incorrect")
        continue