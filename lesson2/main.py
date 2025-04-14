import tkinter


tasks = ["go to gym"]

# ---------------------------------- add Tasks -----------------------------------

def addTask():
    task = input("Sisesta ülesanne: ")
    tasks.append(task)
    print("Ülesanne lisatud!")


# ---------------------------------- delete Tasks -----------------------------------
def deleteTask():
    if not tasks:
        print("Ülesannete nimekiri on tühi.")
        return
    print("-----------------------Ülesanded-------------------------")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("---------------------------------------------------------")

    try:
        index = int(input("Sisesta kustutatava ülesande number: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Ülesanne \"{removed}\" kustutatud.")
        else:
            print("Vigane number.")
    except ValueError:
        print("Palun sisesta number!")


# ---------------------------------- view Tasks -----------------------------------

def viewTasks():
    if not tasks:
        print("Ülesannete nimekiri on tühi.")
    else:
        print("-----------------------Ülesanded-------------------------")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        print("---------------------------------------------------------")


# ---------------------------------- update Tasks -----------------------------------

def updateTask():
    if not tasks:
        print("Ülesannete nimekiri on tühi.")
        return

    print("\n----------------------- Ülesanded -----------------------")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("---------------------------------------------------------")

    try:
        index = int(input("Sisesta uuendatava ülesande number: "))
        if 1 <= index <= len(tasks):
            new_task = input("Sisesta uus ülesanne: ")
            old_task = tasks[index - 1]
            tasks[index - 1] = new_task
            print(f"Ülesanne \"{old_task}\" uuendatud → \"{new_task}\".")
        else:
            print("Vigane number.")
    except ValueError:
        print("Palun sisesta korrektne number.")


def main():
    while True:
        print("\n1. Lisada ülesanne\n" \
              "2. Kustutada ülesanne\n" \
              "3. Ülevaadata ülesanded\n" \
              "4. Uuenda ülesanne\n"
              "5. Välju")
        userInput = input("Mida sa tahad?: ")

        match userInput:
            case "1":
                addTask()
            case "2":
                deleteTask()
            case "3":
                viewTasks()
            case "4":
                updateTask()
            case "5":
                print("Head aega!")
                break
            case _:
                print("Tundmatu valik. Proovi uuesti.")

main()
