# write a Python program to subtract five days from current date
from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)
# timedelta(days=5) represents a 5-day time difference
# we subtract it from the current date
print("Current date:", current_date)
print("Five days ago:", new_date)



# write a Python program to print yesterday, today, tomorrow
from datetime import datetime, timedelta

today = datetime.now().date()         # .date() removes the time part, leaving only the date
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)



# write a Python program to drop microseconds from datetime
from datetime import datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)
# replace(microseconds=0) removes the microseconds portion
print("Original:", now)
print("WIthout microseconds:", no_microseconds)



# write a Python program to calculate two date difference in seconds
from datetime import datetime

date1 = datetime(2025, 5, 1, 12, 0, 0)
date2 = datetime(2025, 5, 3, 12, 0, 0)

difference = date2 - date1            # subtracting two datetime objects gives a timedelta
seconds = difference.total_seconds()  # total_seconds() converts the full difference into seconds

print("Difference in seconds:", seconds)