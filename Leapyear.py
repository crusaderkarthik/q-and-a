##Question: Write a program to find given year is leap or not

##Model 1

year = int(input('Enter year: '))

if (year%400==0) or (year%4==0 and year%100!=0):
    print('LEAP YEAR')
else:
    print('NOT LEAP YEAR')



##Model 2

import calendar

year = int(input('Enter year: ')
is_leapyear = calendar.isleap(year)

if is_leapyear:
           print('Leap Year')
else:
    print('Not Leap Year')
