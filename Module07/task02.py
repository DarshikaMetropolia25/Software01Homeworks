names = set()
enter_name = "empty"
new = "New Name !"
while enter_name != "":
    enter_name = input("Enter a name or press enter to print : ")
    for n in names:
        if n == enter_name:
            new = "Existing Name !"
            break
        else:
            new = "New Name !"

    print(new)
    names.add(enter_name)
for p in names:
    print(p)