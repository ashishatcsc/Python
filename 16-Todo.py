
while True:
    choice = input("Please select ToDo List operation to be performed - 'show','add','edit,'remove','complete','exit'\n").strip()
    match choice:
        case 'show':
           file = open("todos.txt","r")
           lst = file.readlines()
           file.close()     
           for index,item in enumerate(lst):
                    row=f'{index+1}-{item}'
                    print(row)
        case 'add':
            lstitem = input("Enter Todo Item:")

            file = open("todos.txt","r")
            lst = file.readlines()
            file.close()

            lst.append(lstitem)

            file = open("todos.txt","w")
            file.writelines(lst)
            file.close()

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
                currentitem = enumerate(lst)
                for index,val in currentitem:
                     print(str(index+1) + "." + val)
                itemtoedit = int(input("Please enter item number to be edited"))
                newitem = input()
                lst[itemtoedit-1] = newitem
        case 'complete':
              number = int(input("Please enter the item number to be marked as complete"))
              itemcompleted = lst.pop(number-1)
              print("Completed item is:",itemcompleted)        
        case 'exit':
                break




