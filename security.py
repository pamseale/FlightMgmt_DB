valid_password = "1234!"

def login():
        print("Please log in to access the Flight Manager:\n")
        print("Username: user1")
        supplied_password = input("Password: ")
        if supplied_password == valid_password:
            print("login details accepted.")
            return True
        else:
            response = input("login failed. Press any key to try again or 'E' to exit.")
            if response == "E":
                exit()
            else:
                return False

