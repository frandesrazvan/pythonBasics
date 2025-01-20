import datetime

mytime = datetime.time(2, 20)
print(mytime) # 02:20:00
mytime = datetime.time(13, 30, 1, 20)
print(mytime) # 13:30:01.000020

today = datetime.date.today()
print(today) # 2025-01-16
print(today.month) # 1
print(today.ctime()) # Thu Jan 16 00:00:00 2025

from datetime import datetime

mydatetime = datetime(2025, 1, 16, 11, 20, 15)
print(mydatetime) # 2025-01-16 11:20:15
mydatetime = mydatetime.replace(year = 2024)
print(mydatetime) # 2024-01-16 11:20:15

# DATE
from datetime import date

date1 = date(2025, 11, 3)
date2 = date(2024, 11, 9)
print(date1 - date2) # 359 days, 0:00:00

# DATETIME
datetime1 = datetime(2025, 11, 3, 22, 0)
datetime2 = datetime(2023, 5, 2, 12, 0)
mydiff = datetime1 - datetime2
print(mydiff) # 916 days, 10:00:00
print(mydiff.total_seconds()) # 79178400.0