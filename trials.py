import matrix

def start():
    choice = input("Would you like to sign up or login: ")
    if choice.upper() == "REGISTER":
        signup()
    elif choice.upper() == "LOGIN":
        login()

def signup():
    username = input("Choose your username: ")
    password = input("Choose your password: ")
    password2 = input("Confirm password: ")
    if password != password2:
        print("Passwords do not match")
        start()
    else:
        secureFile = open('secureFile.txt','a')
        secureFile.write(username + ":" + password +"\n")
        secureFile.close()
        print("User " + username + " has been added to database")
        start()
        
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    details = username + ":" + password
    secureFile = open('secureFile.txt','r')
    #for user in secureFile.read().split('\n'):
    if details in secureFile.read().split('\n'):#user: 
            print(username + " has successfully logged in")
            matrix.main()
    else:
            print("Login details have not been found")
            start()
            


start()