tasks = []

def add_task():
  """Adds a new task to the to-do list."""
  new_task = input("Enter a new task: ")
  tasks.append(new_task)
  print("Task added!")

def list_tasks():
  """Prints all tasks in the to-do list."""
  if tasks:
    for index, task in enumerate(tasks):
      print(f"{index + 1}. {task}")
  else:
    print("There are no tasks in the list.")

def delete_task():
  """Deletes a task from the to-do list."""
  if tasks:
    list_tasks()
    task_index = int(input("Enter the number of the task to delete: ")) - 1
    if 0 <= task_index < len(tasks):
      deleted_task = tasks.pop(task_index)
      print(f"Task '{deleted_task}' deleted.")
    else:
      print("Invalid task number.")
  else:
    print("There are no tasks to delete.")

def main():
  """Main loop for the to-do list application."""
  while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      add_task()
    elif choice == '2':
      list_tasks()
    elif choice == '3':
      delete_task()
    elif choice == '4':
      print("Exiting To-Do List.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
