from datetime import date
from datetime import time
from datetime import datetime

def main():
    # Date Objects
    # Get today's date from today() method in date class
    # today = date.today()
    # print("Today's date is", today)
    
    # print out date's individual components
    # print("Date components: ", today.day, today.month, today.year)

    # # retrieve today's weekday 0=Monday 6=Sunday
    # print("Today's weekday # is: ", today.weekday())
    # days = ["mon", "tue", "wed", "thr", "fri", "sat", "sun"]
    # print("Which is a:", days[today.weekday()])

    today = datetime.now()
    print("The current date and time is", today)

    # get the current time
    t = datetime.time(datetime.now())
    print(t)


if __name__ == "__main__":
    main()