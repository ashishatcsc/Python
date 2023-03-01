lst = []
while True:
    choice = input("Please select ToDo List operation to be performed - 'show','add','edit,'remove','exit'\n")
    match choice:
        case 'show':
            if not lst:
                print("No Todo item")
            else:
                n = 1
                for i in lst:
                    print(str(n) +". " + i)
                    n += 1
        case 'add':
            lst.append(input("Enter Todo Item:"))
        case 'remove':
            if not list:
                print("There is no To-Do item to remove")
            else:
                itemtoremove=int(input("Enter Item to remove"))
                listvalue = lst[itemtoremove-1]
                print(listvalue)
                lst.remove(listvalue)
                print("To-do Item Removed")
        case 'edit':
                itemtoedit = int(input("Please enter item to edit"))
                newitem = input()
                lst[itemtoedit-1] = newitem
        case 'exit':
                break




