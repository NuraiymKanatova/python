# by default datetime creates naive object - without information about timezone

from datetime import datetime

now = datetime.now()
print(now)

# to work with timezones, used timezone

from datetime import datetime, timezone

now_utc = datetime.now(timezone.utc)
print(now_utc)

# now this is aware object - it knows UTC


# creating offset - смещение
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=3))                # UTC+3
dt = datetime(2025, 5, 1, 12, 0, 0, tzinfo=tz)

print(dt)


# converting between timezones
dt_utc = dt.astimezone(timezone.utc)
print(dt_utc)

# we can compare different timezone only if objects are aware
# UTC - standard starting point