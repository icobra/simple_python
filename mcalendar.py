#!/usr/bin/python3
# Displays the current or selected month on the command line.

import calendar
import datetime
import sys

def chek_year(year):
    if (year.isdigit()) and (int(year) > 0) and (int(year) < 10000):
        return True
    else:
        return False

def chek_month(month):
    if (month.isdigit()) and (int(month) > 0) and (int(month) < 13):
        return True
    else:
        return False

def current_month():
    current_date = str(datetime.date.today())
    current_date = current_date.split('-')
    return current_date

def main():
    #Creating a calendar
    calendar_pages = calendar.TextCalendar(0)

    if len (sys.argv) > 2:
        input_date = [chek_year(sys.argv[1]), chek_month(sys.argv[2])]
        if all(input_date):              
            print("You chose month... \n")
            print(calendar_pages.formatmonth(int(sys.argv[1]), int(sys.argv[2]), w=0, l=0))
        else:
            print(input_date)
            print("Incorect date type.")
    elif len(sys.argv) > 1:
        if sys.argv[1] ==  "--help":
            print ("Call the program without options to print the current month.")
            print("Use: mcaledar.py [year] [month].")
        else:
            print("Введите --help для помощи или без параметров по умолчанию")
    else:
        print("Current month... \n")
        current_date = current_month()
        print(calendar_pages.formatmonth(int(current_date[0]), int(current_date[1]), w=0, l=0))

if __name__ == "__main__":
    main()