#Felicia Royal-Baham
#This exercise is from ThinkPython Exercise 2.10
#completed December 13, 2022

#Scenario: If I leave my house at 6:52 and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile)
#and 1 mile at easy pace again, what time do I get home for breakfast?

#Variables defining the pace at 1 mile, and tempo for 3 miles
pace = 8.15
tempo = 7.12
paceMile = 1
tempoMile = 3

#Variables that create a formula for calculating the easy pace per mile and the tempo per 3 miles.
easyPace = pace * paceMile
tempoPace = tempo * tempoMile
totalTime = easyPace + tempoPace + easyPace

#Print() function showing the total calculated time.
print("Your run total time is: ", totalTime)

#Print() function showing the time you left the house and the total running time.
print("You left the house at 6:52 am and returned home", totalTime, "minutes later for breakfast." )










