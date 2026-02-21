# a date in python is not a data type of its own, 
# but we can import a module named datetime to work with dates as date objects


# import the datetime module and display the current date
import datetime

x = datetime.datetime.now()
print(x)
# output is current time with year, month, day, hour, minute, second and microsecond
# (2026-02-21 19:58:26.464420)

# when we execute the code from the example above the result will be current time
# the datetime module has many methods to return information about the date object

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
# output: 2026 and current day (Saturday)