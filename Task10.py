lights = False
heater = False
daySet = False
temperature = 17

flag = True
while flag:
    print("""
    ****************OPTIONS MENU****************
    |1. Turn lights ON
    |2. Turn heater ON
    |3. Check status
    |4. EXIT
    """)

    option = str(input("Choose one option from 1 to 4: "))
    match option:
        case "1":
            if lights:
                print("Lights already ON")
            elif not daySet and not lights:
                lights = True
                print("Light turned ON")
            else:
                print("Cannot turn lights ON during day time")
        case "2":
            if heater:
                print("Heater already ON")
            elif temperature < 18 and lights:
                heater = True
                print("Heater turned ON")
            else:
                print("Cannot turn heater ON with lights OFF or Temperature below 18")
        case "3":
            print(f"""
            ****************STATUS****************
            |- Day time: {"Day" if daySet else "Night"}
            |- Temperature {temperature}°
            |- Lights are {"ON" if lights else "OFF"}
            |- Heater is {"ON" if heater else "OFF"}
            """)
        case "4":
            print("Program finished")
            flag = False
        case _:
            print("Entry not valid, use only numbers from 1 to 4")
            continue
