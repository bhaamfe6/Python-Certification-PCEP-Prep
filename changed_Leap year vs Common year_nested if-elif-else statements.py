#FRB 04/11/2023
#Python Institute Module 3.1.12 Lab: Essentials of the if-elif-else statement
#Objectives
#using the if-elif-else statement

#create code that calculates the year to determine if the year is a Leap year or a common year
year = int(input("Enter a year: "))

#code to determine if the year entered falls within the Gregorian calendar period
if year < 1582:
    print("Not within the Gregorian calendar period")

#code to determine if year is Leap or Common
if year%4 == 0:
    print("Common year")
elif year%100 == 0:
    print("Common year")
elif year%400 == 0:
    print("Leap year")
else:
    print("Leap year")

