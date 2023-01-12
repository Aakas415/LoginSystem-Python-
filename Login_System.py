username = "admin"
password = "admin"

for i in range(0,3):
    uname = input("Enter User Name: ")
    pasw = input("Enter Password: ")
    if uname != username and pasw == password:
        print("UserName is invalid :( ")
    elif uname == username and pasw != password:
        print("Password is invalid :( ")
    elif uname != username and pasw != password:
        print("Invalid username and password :(")
    elif uname== username and pasw==password:
        print("You are logged in successfully :)")
        exit()
print("You system is locked plese try after 15min later.. :(")