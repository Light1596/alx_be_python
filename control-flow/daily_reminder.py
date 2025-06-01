task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
response = input("Is it time-bound? (yes/no): ")

match (priority, response):
    case ("high", "yes"):
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")

    case ("low", "no"):
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

    case _:
        print(f"{task} is a medium priority task")