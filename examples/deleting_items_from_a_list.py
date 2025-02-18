tasks = []

# This function initializes our empty 'tasks' list with three elements.
def initializeList():
    '''
    Using the keyword 'global' here ensures that any usage of the word 'tasks' references our global tasks variable, defined on line 1.
    Without this, any reference to 'tasks' would instead create a completely new variable with that is scoped locally to the function.
    Meaning, it would not actually target the global tasks variable defined on line 1, it would be working with a completely different variable of the same name.
    '''
    global tasks
    tasks = ["Do homework", "Go the gym", "Get groceries"] 
    print("INITIAL LIST: " + str(tasks))
    
    
# METHOD 1: remove()
print("\nMETHOD 1:")
initializeList() # Assign values to our list variable.
tasks.remove("Do homework") # Remove the element with a value of "Do homework"
print("CURRENT LIST: " + str(tasks))

# METHOD 2: pop()
print("\nMETHOD 2:")
initializeList() # Assign values to our list variable.
tasks.pop(0) # Remove the element at index 0 in the list.
print("CURRENT LIST: " + str(tasks))

# METHOD 3: del
print("\nMETHOD 3:")
initializeList()
del tasks[0] # Remove the element at index 0 in the list.
print("CURRENT LIST: " + str(tasks))

# BONUS METHOD (not recommended for the project): Loop through list, check if any element contains a particular substring, use remove() to remove the element if it does.
print("\nBONUS METHOD:")
initializeList() # Assign values to our list variable.
for task in tasks:
    if "homework" in task: # Check if 'task' contains the substring 'homework'
        tasks.remove(task)
print("CURRENT LIST: " + str(tasks))