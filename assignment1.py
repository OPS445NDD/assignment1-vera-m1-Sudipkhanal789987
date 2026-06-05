#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
Author: "Sudip Khanal"
Semester: "Summer 2026"

The python code in this file (assignment1.py) is original work written by
"Sudip Khanal". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    if leap_year(year): #Check if the given year is a leap year
        feb_max = 29 #February has 29 days in a leap year
    else:
        feb_max = 28  # February has28 days in normal year

    month_days = {  #Dictionary storing days in each month
        1: 31,
        2: feb_max,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return month_days[month]  #Return the number of days for the requested month

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format
    Return the date for the next day of the given date in YYYY-MM-DD format.
    '''
    str_year, str_month, str_day = date.split('-') #Split yyyy-mm-dd into the year and month

    year = int(str_year)  #Convert  year form string to integer
    month = int(str_month) # Convert month form string to integer
    day = int(str_day) #Convert day from string to integer

    month_max = mon_max(month, year) #get the maximum number of days for this month and year
    tmp_day = day + 1 # move to the next month

    if tmp_day > month_max:  #To check if next day goes past the end of the  month
        to_day = 1  #Reset day to 1 for the new month
        tmp_month = month + 1 #move to the next month
    else:
        to_day = tmp_day #keep the calculated next day
        tmp_month = month #Month stays the same

    if tmp_month > 12: #Check if month goes past December
        to_month = 1 #Reset month to january
        year = year + 1 #Move to the next year
    else:
        to_month = tmp_month #keep the calculated month

    next_date = f"{year}-{to_month:02}-{to_day:02}" #Format date as yyyy-mm-dd
    return next_date  #Return the next date
def usage():
    "Print a usage message to the user"
    ...


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    if year % 400 == 0: # years divisible by 400 are leap years
        return True
    if year % 100 == 0: # years divisible by 100 are not leap years
        return False
    if year % 4 == 0:  # years divisible by 4 are leap years
        return True
    return False   #all other years are not leap years 

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    ...

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    ...

if __name__ == "__main__":
    ...
