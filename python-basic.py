def someFunction(some_name):
    lists = [1, 4.6, 9, "Champ", 3, 7]
    lists.append(some_name)
    lists[0] = "First"

    print("first : {}".format(lists[0]))
    print("last : {}".format(lists[-1]))
    print("name : {}".format(lists[3]))
    print("middle 2 : {}\n".format(lists[2:4]))

    for i in lists:
        if isinstance(i,str):
            print("Hello {}".format(i))
        else:
            print(i)

someFunction("Nat")
