
def check_in_range(value, low, high):
    result = False
    if low <= value <= high:
        result = True
    return result

def request_and_validate(low, high):
    while True:
        choice = input("Select a menu choice or 'E' to exit.")
        if choice == "E":
            exit()
        else:
            try:
                int(choice)
            except ValueError:
                print("invalid choice, please enter an integer")
            else:
                if low <= int(choice) <= high:
                    break
                else:
                    print("selection out of range, please choose a number between", low, " and", high)
    return choice

def user_validation():
    pin = 1234
    while True:
        response = input("Please enter the PIN or 'E' to exit program.")
        if response == 1234:
            print("\nPIN accepted.\n") #menu_1
            break
        elif response == "E":
            print(
                "\nExiting program.\n")
        else:
            print("\nPIN not accepted, please try again.\n")