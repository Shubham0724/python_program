import time
print(time.time())

#time.sleep():
import time

time.sleep(10)
print(time.ctime())

#time.localtime():
import time

print(time.localtime(1658672956.8853111))

#time.gmtime():

import time

print(time.gmtime(1658672956.8853111))

#time.mktime():
import time

local_time = (2022, 7, 24, 20, 14, 39, 6, 205, 0)
print(time.mktime(local_time))

#time.asctime():
import time

local_time = (2022, 7, 24, 20, 14, 39, 6, 205, 0)
print(time.asctime(local_time))

#time.strptime():
import time

local_time = "24 July, 2022"
print(time.strptime(local_time, "%d %B, %Y"))

#Calendar:
import calendar

print(calendar.month(2022, 7))

