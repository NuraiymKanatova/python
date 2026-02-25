# calculating time differences
# in datetime we calculate it through substituting 

from datetime import datetime

date1 = datetime(2025, 5, 1)
date2 = datetime(2025, 5, 10)

difference = date2 - date1
print(difference)
# output: 9 days, 0:00:00

# when substituting datetime of two objects, we got timedelta
# timedelta keeps the time difference 


print(difference.days)              # 9
print(difference.seconds)           # seconds in days
print(difference.total_seconds())   # all difference in seconds



from datetime import datetime

d1 = datetime(2025, 5, 1, 12, 0, 0)
d2 = datetime(2025, 5, 1, 15, 30, 0)

diff = d2 - d1
print(diff)                         # 3:30:00