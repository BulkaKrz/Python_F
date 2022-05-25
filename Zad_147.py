def DaysToEndOfYear():
    #funkcja oblicza ilośc dni do  sylwestra
    from datetime import date
    date_today = date.today()
    curent_year = date_today.year
    date_end_year = date(curent_year,12,31)
    delta = (date_end_year - date_today).days
    print('do sylwestra pozostało %s dni' % (delta))
    return
DaysToEndOfYear()
