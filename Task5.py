data ={
    "username": "Choklitos",
    "password": "123456789"
}
count = 2

while True:
    text = ""
    username = str(input("Enter your username (Caps sensitive): "))
    password = str(input("\nEnter your password (Caps sensitive): "))

    if username != data["username"]:
        text += "Username"

    if password != data["password"]:
        if text != "":
            text += " & "
        text += "Password"

    if text == "":
        print("\n*************ACCESS GRANTED*************")
        break
    else:
        if count == 0:
            print("\n*************ACCESS DENIED*************")
            print("Too many attempts")
            break
        else:
            print("\n*************ACCESS DENIED*************")
            print(f"{text} incorrect")

        count -= 1
        print(f"Attempts left {count + 1}\n")