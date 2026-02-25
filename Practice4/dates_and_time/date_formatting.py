# the datetime object has a method for formatting date objects into readable strings
# this method is called strftime(), and takes one parameter, format, 
# to specify the format of the returned string:

# display the name of the month
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

# %a - weekday short version
# %A - weekday full version
# %w - weekday as a number 0-6, 0 is Sunday
# %d - day of month 01-31
# %b - month name short version
# %B - month name full version
# %m - month as a number 01-12
# %y - year short version
# %Y - year full version
# %H - hour 00-23
# %I - hour 00-12
# %p - AM/PM
# %M - minute 00-59
# %S - second 00-59
# %f - microsecond
# %j - day number of year 001-366
# %C - century