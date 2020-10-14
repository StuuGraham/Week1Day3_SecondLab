tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
# Function that prints a list of incomplete tasks.
def uncompleted_tasks(list):
    uncompleted = []
    for task in list:
            if task["completed"] == False:
                uncompleted.append(task)
    return uncompleted

#print(uncompleted_tasks(tasks))

# Function that returns a list of complete tasks.
def completed_tasks(list):
    completed = []
    for task in list:
            if task["completed"] == True:
                completed.append(task)
    return completed

#print(completed_tasks(tasks))

# Function that will print a list of all task descriptions.
def task_descriptions(list):
    descriptions = []
    for task in list:
        descriptions.append(task["description"])
    return descriptions

#print(task_descriptions(tasks))

# Function that will print a list of tasks that take at least a given time.
def tasks_longer_than(list, time):
    tasks = []
    for task in list:
        if task["time_taken"] > time:
            tasks.append(task)
    return tasks

#print(tasks_longer_than(tasks, 20))

# Function that will print a task based on it's description.
def task_by_description(list, description):
    for task in list:
        if task["description"] == description:
            return task
    return "Task not found"

#print(task_by_description(tasks, "Walk Dog"))

# Given a description update the task to mark it as complete.
def mark_task_complete(list, description):
    for task in list:
        if task["description"] == description:
            task["completed"] = True

mark_task_complete(tasks, "Feed Cat")
#print(tasks)

# Add a task to the list
def create_task(list, task_to_add):
    list.append(task_to_add)
print(tasks)
create_task(tasks, {"description": "Wash Car", "completed": True, "time_taken": 45})
#print(tasks)