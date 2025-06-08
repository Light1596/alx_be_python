import datetime

def display_current_datetime():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_time}")
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    days = datetime.timedelta(days=number_of_days)
    future_date = now + days
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")



display_current_datetime()
