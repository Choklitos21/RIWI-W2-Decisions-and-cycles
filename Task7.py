totalValue = 0
membershipKind = ["active", "temporal", "None"]
membership = ""

while True:
    print(
        "|- Big amount: more than $100.000\n|- Average amount: $50.000 up to 100.000\n|- Regular amount: Less than $50.000")

    totalValue = input("Enter the purchase value: ")
    if totalValue.isalpha():
        print("Must use numbers only")
        continue
    elif int(totalValue) < 0:
        print("Cannot be less than 0, try again")
        continue
    break

while True:
    print("\nMemberships options:\n- Active\n- Temporal\n- None\n")

    membership = input("Enter your kind of membership: ").strip().lower()
    if not membership.isalpha():
        print("Must be letters only")
        continue
    if membership != membershipKind[0] and membership != membershipKind[1] and membership != membershipKind[2]:
        print("Please use only one of the options above")
        continue
    break