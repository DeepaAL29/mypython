from emp import *
def time(hours):
    if hours<40:
        raise TimeSheet("less than 40 hours")
    else:
        print("submit the timesheet")
try:
    time(20)
except(TimeSheet):
    print("message")
time(40)