
import sys

location = sys.path

for x in location:
    print(x)

import calendar

leapdays = calendar.leapdays(2000,2024) # returns number of leapyears btw y1 and y2

print(leapdays)

isitLeap = calendar.isleap(2024)
print(isitLeap)