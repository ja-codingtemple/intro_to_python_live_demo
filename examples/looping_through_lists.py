#            0                1           2
tasks = ["Do homework", "Go the gym", "Get groceries"]

# Method 1:
print("\nMETHOD 1:")
for task in tasks:
    print(task)

# Method 2:
print("\nMETHOD 2:")
for i in range(len(tasks)):
    print(tasks[i])

# Method 3:
print("\nMETHOD 3:")
for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}")
    
# Method 4:
print("\nMETHOD 4:")
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")