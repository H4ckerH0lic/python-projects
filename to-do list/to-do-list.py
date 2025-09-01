# we gonna build a to-do list and will use file handeling
# and datetime module

import os
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

FILE_NAME = "tasks.txt"

def add_task():
    task = input(Fore.CYAN + " Enter new task : " + Style.RESET_ALL)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_NAME, "a") as f:
        f.write(f"{task} | {timestamp}\n")

    print(Fore.GREEN + "✔ Task added successfully! ")

def view_task():
    if not os.path.exists(FILE_NAME):
        print(Fore.RED+" No Task Found! ")
        return
    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()
    if not tasks:
        print("No Tasks Added! ")
        return
    print(Fore.YELLOW+"\n Your To-Do List: ")
    for idx, tasks in enumerate(tasks, start=1):
        print(f"{idx}. {tasks.strip()}")

def delete_task():
    if not os.path.exists(FILE_NAME):
        print(Fore.RED + "No Task Found ")
        return
    with open(FILE_NAME,"r") as f:
        tasks = f.readlines()
        if not tasks:
            print(Fore.RED + "no tasks to delete")
            return
    view_task()
    try:
        task_num = int(input(Fore.CYAN + "Enter task number to delete"+ Style.RESET_ALL))
        if 1<= task_num <= len(tasks):
            del tasks[task_num-1]
            with open(FILE_NAME, "w") as f:
                f.writelines(tasks)
            print(Fore.GREEN + "Task deleted successfully! ")
        else:
            print(Fore.RED + " Invalid file number !! ")
    except ValueError:
        print(Fore.RED + "Invalid input")

def main():
    while True:
        print(Fore.MAGENTA + "\n-------TO-DO LIST MENU-------")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3.delete tasks")
        print("4. Exit")

        choice = input(Fore.CYAN + "Enter Choice (1-4)" + Style.RESET_ALL)
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print(Fore.LIGHTGREEN_EX + "GOODBYE")
            break
        else:
            print(Fore.RED + "Invalid choice, try again ")

if __name__ == "__main__":
    main()