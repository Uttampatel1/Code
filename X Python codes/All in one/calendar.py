# import module
import calendar

# To ask month and year from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))
with open('calendar2021.txt','a') as f:
	f.write (calendar.calendar(yy, 2,1,6))
	
print(calendar.calendar(yy, 2,1,6))