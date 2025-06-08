from datetime import *

def display_current_datetime():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_time}")

    def calculate_future_date():
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        days = timedelta(days=number_of_days)
        future_date = now + days
        print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

    calculate_future_date()

display_current_datetime()
