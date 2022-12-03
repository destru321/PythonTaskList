from pymongo import MongoClient


def get_database():
    connection_string = "mongodb+srv://destru:Was1ant201@pyproject.f8a312k.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(connection_string)
    return client["taskList"]


dbname = get_database()
collection_name = dbname["tasks"]


def get_tasks():
    tasks = collection_name.find()
    return tasks


def add_task(task):
    collection_name.insert_one(task)


def delete_task(task):
    collection_name.delete_one({"name": task})


def update_task(task, new_task):
    collection_name.update_one({"name": task}, {"$set": {"name": new_task}})


def program():
    print("1. Show tasks")
    print("2. Add new task")
    print("3. Delete task")
    print("4. Update task")
    print("5. End program")

    correct_option = False
    option = ""

    while not correct_option:
        option = int(input("Choose an option: "))
        if option == 1 or option == 2 or option == 3 or option == 4 or option == 5:
            correct_option = True
        else:
            print("Choose correct option!!!")

    print("\n")

    match option:
        case 1:
            for i in get_tasks():
                print("Name: " + i["name"])
                print("Date: " + i["date"])
                print("____________________")

            print("\n")
            program()
        case 2:
            task_name = input("type the name of new task: ")

            for i in get_tasks():
                while i["name"] == task_name:
                    print("You already have task with this name!!!")
                    task_name = input("type the name of new task: ")

            date = input("type today's date: ")

            new_task = {
                "name": task_name,
                "date": date
            }

            add_task(new_task)

            print("\n")
            program()
        case 3:
            for i in get_tasks():
                print("Name: " + i["name"])
                print("Date: " + i["date"])
                print("____________________")

            task_name = input("Type name of the task u would like to delete: ")

            delete_task(task_name)

            print("\n")
            program()
        case 4:
            for i in get_tasks():
                print("Name: " + i["name"])
                print("Date: " + i["date"])
                print("____________________")

            task_name = input("Type name of the task u would like to update: ")
            new_task = input("Type new name of the task: ")

            update_task(task_name, new_task)

            print("\n")
            program()
        case 5:
            print("Bye!!!")


print("WELCOME TO TASK LIST APP!!!")
program()
