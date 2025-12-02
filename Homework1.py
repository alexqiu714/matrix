names = []

while True:
    x = input("Choose an action \n 1. Add a name \n 2. Edit a name \n 3. Remove a name \n 4. View all names \n 5. End program \n (1, 2, 3, 4, 5)")

    if x == "1":
        a = input("What name do you want to add?")
        names.append(a)

    if x == "2":
        e = input("Which name would you like to edit?")
        u = input("What would you like to change it to?")
        index = 0
        for i in names:
            if i == e:
                names[index] = u
            else:
                index += 1

    if x =="3":
        d = input("Which name would you like to remove?")
        names.remove(d)

    if x == "4":
        print(names)

    if x == "5":
        print("Ending program")
        break