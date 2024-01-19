#FRB - January 29, 2023 - Create a file with Nested If-Else statements

points = 0

red = 5
blue = 10
green = 25

key = input("What color key did you find? ")

if key == red:
    points =+ 5
    print("You have earned", red, "points for finding a red key.")
    
elif key == blue:
    points =+ 10
    print("You have earned", blue, "points for finding a red key.")    

elif key == green:
    points =+ 25
    print("You have earned", green, "points for finding a red key.")

else:
    points +=0
    print("You did not find a valid key.")

print("You have", points, "total points.")
print("Keep looking for more keys!")


