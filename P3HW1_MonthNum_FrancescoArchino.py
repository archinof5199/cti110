# CTI-110
# P3HW1 - Month number
# Francesco Archino
# 9/29/2019
#

# This program asks he user to enter a month from 1-12 and provides the name
#of the monthcorrelating with the number given.

#ask user to enter a month using the number that corresponds with that month
#i.e febuary =2, july = 7 and so on



month_num = float(input(" Please enter a month's calender number from 1 to 12 ."))

if month_num == 1:
    print("January")
elif month_num == 2:
    print("Febuary.")
elif month_num == 3:
    print("March.")
elif month_num == 4:
    print("April.")
elif month_num == 5:
    print("May.")
elif month_num == 6:
    print("June.")
elif month_num == 7:
    print("July.")
elif month_num == 8:
    print("August.")
elif month_num == 9:
    print("September.")
elif month_num == 10:
    print("October.")
elif month_num == 11:
    print("November.")
elif month_num == 12:
    print("December.")

else:
    print("error there are only 12 monthes in a year try again.") 
