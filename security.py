valid_password = "1234!"

def login():
        print("\nPlease log in to access the Flight Manager:\n")
        print("Username: user1")
        supplied_password = input("Password: ")
        if supplied_password == valid_password:
            print("\nlogin details accepted.\n")
            return True
        else:
            response = input("\nLogin failed. Press any key to try again or 'E' to exit.\n")
            if response == "E":
                exit()
            else:
                return False

