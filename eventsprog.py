""" Event Scheduler
__author__ : Prakhar Srivastav
A small program to add, remove, edit and print events sorted datewise.
Uses mongodb for persistence.
Dependancies: Mongodb, pymongo
Usage: python eventsprog.py
"""

import sys
import pymongo
import datetime
import re

connection = pymongo.Connection("localhost", 27017)
db = connection.test
sch = db.schedule

def get_date(date):
    """ Returns a date instance for an input string of the format
    today, tomorrow, n days later or YYYY-MM-DD """
    if date == "today":
        d = datetime.date.today()
    elif date == "tomorrow":
        d = datetime.date.today() + datetime.timedelta(days=1)
    elif re.match(r'(\d+) days later', date):
        day_count = re.match(r'(\d+) days later', date).group(1)
        d = datetime.date.today() + datetime.timedelta(days=int(day_count))
    elif re.match(r'(\d+)-(\d+)-(\d+)', date):
        date_group = re.match(r'(\d+)-(\d+)-(\d+)', date).groups()
        d = datetime.date(int(date_group[ 0 ]), int(date_group[ 1 ]), int(date_group[ 2 ]))
    else: 
        return None
    return d

def get_time(time):
    """ Returns a time instance for an input string of the format 
    12:21 (24 hrs format)"""
    regtime = re.compile(r'^([0-1][0-9]|[2][0-3]):([0-5][0-9])$')
    if not regtime.match(time):
        return None
    time_group = regtime.match(time).groups()
    time_final = datetime.time(int(time_group[0]), int(time_group[1]))
    return time_final

def add_event(old_title = None, update=False):
    if update:
        title = raw_input("Enter new title: " )
        date = raw_input("Enter new date: (like today, tomorrow, 2 days later, 2012-04-21)\n")
    else:
        title = raw_input("Enter title: ")
        date = raw_input("Enter date: (like today, tomorrow, 2 days later, 2012-04-21)\n")

    date_final = get_date(date)
    if not date_final:
        while not date_final:
            print "Error: Invalid time format"
            date = raw_input("Enter date: (like today, tomorrow, 2 days later, 2012-04-21)\n")
            date_final = get_date(date)

    time = raw_input("Enter time: (like 21:30): ")
    time_final = get_time(time)
    if not time_final:
        while not time_final:
            print "Error: Invalid time format"
            time = raw_input("Enter time: (like 21:30): ")
            time_final = get_time(time)

    date_time = datetime.datetime.combine(date_final, time_final)
    if update:
        sch.update({"title": old_title}, {"title": title, "date" : date_time})
        print "Event Updated! \n"
    else:
        sch.insert({"title" : title, "date" : date_time })
        print "Event Added! \n"

def edit_event():
    title = raw_input("Enter title of the event to edited: ")
    add_event(update=True, old_title = title)

def print_event():
    events = list(sch.find().sort("date"))
    print "\n"
    print "Date: ", datetime.datetime.utcnow().strftime("%A - %d %b %Y")
    print "\n"
    print "TITLE".ljust(40), "DUE ON"
    print "-"*70
    for e in events:
        print e["title"].ljust(40), \
              e["date"].strftime("%A - %d %b at %H:%M")
    print "\n"

def delete_event():
    title = raw_input("Enter title of the event to deleted: ")
    sch.remove({"title" : title})
    print "Event Deleted! \n"

if __name__ == "__main__":
    while True:
        ri = raw_input("(a)dd, (d)elete, (e)dit, (p)rint, (q)uit: ")
        choice = ri[0].lower()
        if choice == "a": add_event()
        elif choice == "d": delete_event()
        elif choice == "e": edit_event()
        elif choice == "p": print_event()
        elif choice == "q": sys.exit()
        else: print "Incorrect char"
