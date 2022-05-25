'''
import time
print(time.time())
print(time.localtime())
print(time.localtime(time.time()))
print(time.asctime())
print(time.perf_counter())
import sys
print(sys.version)
print(time.localtime(time.perf_counter()))

import calendar

print('-----------------------------')
print(calendar.month(2021,11,w=5,l=2))
print('-----------------------------')
print(calendar.month(2021,11))
print('-----------------------------')
print(calendar.weekday(2021,11,2))
print('-----------------------------')
print(calendar.isleap(2020))
print(calendar.calendar(2021))

'''
import time
print(time.time())
print(time.localtime(time.time()))
import calendar
print(calendar.month(1978,7))
calendar.setfirstweekday(6)
print(calendar.month(1978,7))
print(calendar.isleap(2020))
print('---------------------')
print(calendar.calendar(2019))
