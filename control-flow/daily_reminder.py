task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
response = input("Is it time-bound? (yes/no): ")

match (priority, response):
    case ("high", "yes"):
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")

    case ("low", "no"):
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

    case ("high", _):  # High priority, regardless of time-bound status
        print(f"Reminder: {task} has **high priority**. Address it soon.")

    case (_, "yes"):  # Time-bound, regardless of priority
        print(f"Reminder: {task} is **time-bound**. Don't miss the deadline!")

    case ("medium", "no"):  # Specific combination
        print(f"Note: {task} is a medium-priority, non-time-bound task.")

    case _:  # Default case for anything else
        print(f"Task: {task}. Priority: {priority}. Time-bound: {response}.")