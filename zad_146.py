from datetime import date
from datetime import timedelta

def GivWorkingDay(year=date.today().year, month=date.today().month, day=date.today().day):
    # printins the nearest working day date
    #from datetime import date
    #from datetime import timedelta

    day = date(year,month,day)
    #day = date.today()

    if day.weekday()==5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

   
    return workingday

nextWorkingDay = GivWorkingDay(2017,9,2)
print('Next working day after',2017,9,2,'is',nextWorkingDay)

nextWorkingDay = GivWorkingDay()
print('Next working day after today is',nextWorkingDay)

print('Next working day after today is',GivWorkingDay())

