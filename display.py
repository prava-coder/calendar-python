#import the module "calendar"
import calendar
#taking the input from the user
#to display the year
yy=int(input("enter a year:"))
#to display the month
mm=int(input("enter a month:"))
#to print the calendar of user entered month,year
print(calendar.month(yy,mm))