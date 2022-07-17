import calendar
print (calendar.weekheader(5))
print ()
print (calendar.firstweekday())
print ()
print (calendar.month(2021,5))

print (calendar.monthcalendar(2021,5))
with open ("calendar 2021.txt","w") as f :
    f.write(calendar.calendar(2021))
day_of_the_week=calendar.weekday(2021,5,7)
print (day_of_the_week)
is_leap=calendar.isleap(2021)
print (is_leap)
how_many_leap_days=calendar.leapdays(2000,3000)
print (how_many_leap_days)