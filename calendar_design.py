# 1. Name:
#      Braden Hilton
# 2. Assignment Name:
#      Lab 03: Calendar
# 3. Assignment Description:
#      When given a month and year starting with the year 1753, it will display the month as if on a calendar.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was I initially created a code that also asked me to input a value for what day of the month as well, and it took me a while to realize why that was wrong even though I do need functions to change the day as well.
# 5. How long did it take for you to complete the assignment?
#     7 hours

def next_day(day, max_day):
    day += 1
    if day > max_day:
        day = 1
    return day

def next_month(day, month):
    if day == 1:
        month += 1
    return month

def next_year(year, month):
    if month >= 13:
        year += 1
        month = 1
    return year, month

def day_of_week(i):
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_week = week[i]
    i += 1
    if i > 6:
        i = 0
    return day_week, i

def goal_date():
    month = 0
    year = 0
    while month < 1 or month > 12:
        try:
            month = int(input("What month of the year is it? "))
            if month < 1 or month > 12:
                print("Choose a month between 1 and 12.")
        except ValueError:
            print("Choose a month between 1 and 12.")
    while year < 1753:
        try:
            year = int(input("What year is it? "))
            if year < 1753:
                print("Must be a whole intiger above 1752.")
        except ValueError:
            print("Must be a whole intiger above 1752.")
    return month, year

def days_in_month(month, year):
    month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if year%4 == 0:
        month_dict[2] = 29
    if year%100 == 0 and year%400 != 0:
        month_dict[2] = 28
    max_days = month_dict[month]
    return max_days

def display_full_month(max_days, month, year, day_week):
    week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print(f"{month} month of the year: {year}\n")
    print(" ".join(week))
    match day_week:
        case "Monday":
            space = 0
        case "Tuesday":
            space = 1
        case "Wednesday":
            space = 2
        case "Thursday":
            space = 3
        case "Friday":
            space = 4
        case "Saturday":
            space = 5
        case "Sunday":
            space = 6
    end_month = max_days + 1
    print()
    print("    " * space, end="")
    for day in range(1, end_month):
        print(f"{day:<4}", end="")
        if (day + space) % 7 == 0:
            print("\n")
    if day == max_days and (day + space) % 7 != 0:
        print("\n")

def test(goal_month, goal_year):
    day = 1
    month = 1
    year = 1753
    max_days = 31
    i = 0
    done = False
    while not done:
        day = next_day(day, max_days)
        month = next_month(day, month)
        year, month = next_year(year, month)    
        max_days = days_in_month(month, year)
        if day == 1 and month == 2 and year == 1753:
            i += 1
        weekday, i = day_of_week(i)
        if month == goal_month and year == goal_year:
            done = True
    display_full_month(max_days, month, year, weekday)          

def main():
    test_case = input("Would you like to run the test cases? (y/n)")
    if test_case == "y":
        test(1, 1753)
        test(2, 1753)
        test(1, 1754)
        test(2, 1756)
        test(2, 1800)
        test(2, 2000)   
    day = 1
    month = 1
    year = 1753
    max_days = 31
    i = 0
    done = False
    goal_month, goal_year = goal_date()
    while not done:
        day = next_day(day, max_days)
        month = next_month(day, month)
        year, month = next_year(year, month)    
        max_days = days_in_month(month, year)
        if day == 1 and month == 2 and year == 1753:
            i += 1
        weekday, i = day_of_week(i)
        if month == goal_month and year == goal_year:
            done = True
    display_full_month(max_days, month, year, weekday)  

main()