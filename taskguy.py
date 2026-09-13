import os

FILENAME = "my_tasks.txt"

# Your terminal mascot!
PIGEON = r"""
     _.---._
   .' `.
  / _ _ \
  | (o) (o) | Coo! Time to get to work.
  | /
  \ \ / /
   `. ` .'
     `-----'
"""

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

while True:
    print(PIGEON) # Prints your mascot every time the menu loads
    print("--- Task Guy ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        if len(tasks) == 0:
            print("\nYour task list is empty!")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
                
    elif choice == "2":
        new_task = input("Enter the task you want to add: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"'{new_task}' added and saved!")
        
    elif choice == "3":
        print("Coo! Goodbye!")
        break
        
    else:
        print("Invalid choice, please pick 1, 2, or 3.")

