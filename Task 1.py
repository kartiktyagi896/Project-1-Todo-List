from asyncio import tasks


mytasks = []
while True:
    print("/n TO DO LIST")
    print("1. Add a task");
    print("2. View tasks");
    print("3. Exit");
    
    choice = input("Enter your choice:(1-3) ")
    
    if choice == "1":
        task = input("Enter a task: ");
        mytasks.append(task);
    elif choice == "2":
        if len(mytasks) == 0:
            print("No tasks found.");
        else:
            print("\n Your tasks:");
            for index, task in enumerate(mytasks, start=1):
                print(f"{index}. {task}");
                
    elif choice == "3":
        print("Exiting the program. Goodbye!");
        break;      
    else:
        print("Invalid choice. Please enter a number between 1 and 3.");    
