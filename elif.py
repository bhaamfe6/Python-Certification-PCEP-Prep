grade = int(input("Enter the grade earned: "))

if grade >= 70:
    print("You passed the exam.")
    if grade <=79:
        print("Your grade is", grade,".You earned a C.")
    elif grade <= 89:
        print("Your grade is", grade,". You earned an B.")
    elif grade > 89:
        print("Your grade is", grade,". You earned an A.")

else:
    print("You need to retake the test. You have not passed.")
print()
print("Thank you for completing the exam.")
