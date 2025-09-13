air_port = { "CMB" : "Colombo" ,
            "HEL" : "Helsinki" ,
            "DEL" : "New_Delhi" ,
            "BKN" : "Bangkok" ,
             "DUB" : "Dubai" ,
             "SGP": "Singapore" }

user_input = input("What do you want to do? \n Press 1 to add a new air port \n press 2 to fetch a existing air port \n press 3 to quit: ")

while user_input != "3":
    if user_input == "1":
        name = input("Enter the air port name: ")
        code = input("Enter the air port code: ")
        air_port[code]= name
        user_input = input("What do you want to do? \n Press 1 to add a new air port \n press 2 to fetch a existing air port \n press 3 to quit: ")

    elif user_input == "2":
        code = input("Enter the air port code: ")
        if code in air_port:
            print(f"{code} belongs to {air_port[code]}.")
        user_input = input("What do you want to do? \n Press 1 to add a new air port \n press 2 to fetch a existing air port \n press 3 to quit: ")













