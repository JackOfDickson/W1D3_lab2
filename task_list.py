tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
#task 1 function to display uncompleted tasks

def uncompleted_tasks(chores):
    to_do_list = []
    for chore in chores:
        if chore['completed'] == False:
            to_do_list.append(chore["description"])
    print(to_do_list)

uncompleted_tasks(tasks)

#task 2 function to display completed tasks

def completed_tasks(chores):
    completed_list = []
    for chore in chores:
        if chore['completed'] == True:
            completed_list.append(chore["description"])
    print(completed_list)

completed_tasks(tasks)

#task 3

def name_of_tasks(chores):
    task_list = []
    for chore in chores:
        task_list.append(chore["description"])
    print(task_list)

name_of_tasks(tasks)

#task 4

def timed_tasks(chores, time):
    task_list = []
    for chore in chores:
        if chore["time_taken"] >= time:
            task_list.append(chore["description"])
    print(task_list)

timed_tasks(tasks, 30)

#task 5

def task_lookup(chores, desired_task):
    for chore in chores:
        if chore["description"] == desired_task:
            print(chore)

task_lookup(tasks, "Feed Cat")

#task 6

def update_task_status(chores, finished_task):
    for chore in chores:
        if chore["description"] == finished_task:
            chore["completed"] = True

update_task_status(tasks, "Feed Cat")
print(tasks)

#task 7

tasks.append({ 
    "description": "Make Bed", 
    "completed": False, 
    "time_taken": 10
     }
    )

#TASK 8
user_input = 0
while user_input != "Q" or 'q':

    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")

    user_input = input()

    if user_input == "Q" or "q":
        pass

    if user_input == "1":
        uncompleted_tasks(tasks)