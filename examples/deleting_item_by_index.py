#            0                1           2
tasks = ["Do homework", "Go the gym", "Get groceries"]
    
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")
    
choice = int(input("Which task do you want to delete? "))
choice = choice - 1

tasks.pop(choice)
print(tasks)