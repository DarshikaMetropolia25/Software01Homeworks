password=("rules")
user_name = ("python")
user_name1= input("Enter username : ")
password1=input("Enter password : ")
attempts=1
while attempts !=5:
    if password == password1 and user_name == user_name1:
        print("Welcome ")
        break
    else:
        print("Wrong password or username")
        user_name1 = input("Enter username : ")
        password1 = input("Enter password : ")
        attempts=attempts+1

if attempts==5:
    print("Access denied")


