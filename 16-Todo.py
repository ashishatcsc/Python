
def getToDos(filepath="todos.txt"):
     with open(filepath,"r") as file: 
        lst = file.readlines()
        return lst


def WriteToDos(lst_arg,filepath="todos.txt"): 
    with open(filepath,"w") as file: 
        file.writelines(lst_arg)


while True:
    #Get user input and strip the extra spaces from it. 
    choice = input("Please select ToDo List operation to be performed - 'show','add','edit,'remove','complete','exit'\n").strip()

    if choice.startswith('show'):       
           
           # Below 3 lines of code is improved using the "with" context shown in following line.
           # The With contxt will not require the explicit closing of the file. 
           # file = open("todos.txt","r")
           # lst = file.readlines()
           # file.close()   

           lst = getToDos()

           # new_list = [item.strip("\n") for item in lst] # This is example of list comphrehension when you need to change the values of the list. 

           for index,item in enumerate(lst):
                    item = item.strip("\n") # Logic for removing the new line character at the end of list values.
                    row=f'{index+1}-{item}'
                    print(row)
    elif choice.startswith('add'):
        #lstitem = input("Enter Todo Item:")
        lstitem = choice[4:] +"\n"
       
        # Below 3 lines of code is improved using the "with" context shown in following line.
        # The With contxt will not require the explicit closing of the file. 
        # file = open("todos.txt","r")
        # lst = file.readlines()
        # file.close()

        lst = getToDos()

        lst.append(lstitem)
        
        # Below 3 lines of code is improved using the "with" context shown in following line.
        # The With contxt will not require the explicit closing of the file. 
        # file = open("todos.txt","w")
        # file.writelines(lst)
        # file.close()

        WriteToDos(lst)

    elif choice.startswith('remove'):
        
        lst = getToDos()   

        if not list:
            print("There is no To-Do item to remove")
        else:
            itemtoremove=int(input("Enter Item to remove"))
            listvalue = lst[itemtoremove-1]
            print(listvalue)
            lst.remove(listvalue)
            print("To-do Item Removed")
            
            WriteToDos(lst)


    elif choice.startswith('edit'):
        try: 
            lst = getToDos()

            currentitems = enumerate(lst) 

            for index,val in currentitems:
                    val = val.strip("\n") 
                    print(str(index+1) + "." + val)

            itemtoedit = int(choice[5:].strip())
            newitem = input(f"Enter updated to-do item to edit item {itemtoedit}:")
    
            lst[itemtoedit-1] = newitem+"\n"

            WriteToDos(lst)

        except ValueError:
                print("Your command is not valid!")
                continue        

    elif choice.startswith('complete'):
        try:    
            lst = getToDos()

            number = int(choice[9:])

            to_do_to_be_removed =  lst.pop(number-1) 

            itemcompleted = lst.pop(number-1)
            print("Completed item is:",itemcompleted)

            WriteToDos(lst)

            message = f"Todo item {to_do_to_be_removed} was marked as completed and remvoed form the list."      

            print(message)
        except IndexError:
             print("The mentioned Item number is not in the list.")  
             continue  

    elif 'exit' in choice:
            break
    else:
        print("Command is incorrect")        



    




