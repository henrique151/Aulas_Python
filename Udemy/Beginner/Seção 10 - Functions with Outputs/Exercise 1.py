def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Leap year
            else:
                return False  # Not a leap year
        else:
            return True  # Leap year
    else:
        return False  # Not a leap year


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29  # Leap year, February has 29 days
    else:
        return month_days[month - 1]  # Get the number of days from the month_days list


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)