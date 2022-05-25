from datetime import date
def DaysToEndOfYear(year=date.today().year, month=date.today().month, day=date.today().day):
    from datetime import date
    date_choosen = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_choosen
    
    return delta.days

print('Date: 2020-12-20 days to end of year: %d' %( DaysToEndOfYear(2020,12,20)))
 
print('Date: 2020-12-21 days to end of year: %d' %( DaysToEndOfYear(2020,12,21)))
 
print('Date: TODAY days to end of year: %d' %( DaysToEndOfYear()))
