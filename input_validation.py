
def check_in_range(value, low, high):
    result = False
    if low <= value <= high:
        result = True
    return result

def request_and_validate(low, high):
    while True:
        choice = input("\nEnter a number or 'E' to exit:  ")
        if choice == "E":
            exit()
        else:
            try:
                int(choice)
            except ValueError:
                print("\nInvalid choice, please enter an integer:  ")
            else:
                if low <= int(choice) <= high:
                    break
                else:
                    print("\nSelection out of range, please choose a number between", low, " and", high)
    return choice

