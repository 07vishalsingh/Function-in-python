'''
problem: Imagine you're developing a task management application where users can create, update, and delete tasks. You can create a function called add_task to handle the addition of new tasks to the task list. This function might take parameters such as the task title, description, priority level, and due date. Here's how you could implement this function:
'''
class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date

def add_task(task_list, title, description, priority, due_date):
    new_task = Task(title, description, priority, due_date)
    task_list.append(new_task)
    print(f"Task '{title}' added successfully.")

# Example usage
task_list = []

# Add tasks
add_task(task_list, "Complete project proposal", "Write a proposal for the new project.", "High", "2024-02-20")
add_task(task_list, "Prepare presentation", "Prepare slides for the upcoming presentation.", "Medium", "2024-02-25")
add_task(task_list, "Review documentation", "Review and update project documentation.", "Low", "2024-03-01")

# Print task list
print("\nTask List:")
for idx, task in enumerate(task_list, start=1):
    print(f"{idx}. {task.title} - Priority: {task.priority}, Due Date: {task.due_date}")
