'''Task 6: Leap Year Check
Take a year as input.
Check if it is a leap year or not using nested if.'''
year=int(input("please enter year:"))
if year%400==0:
    print("given year is leap year:",year)
elif year%100==0:
     print("given year is not leap year:",year)
elif year%4==0:
        print("given year is leap year:",year)
else:
   print("this year is not leap year:",year)
    