"""
Implement a program that helps other people learn addition. Write a program that randomly
generates a simple addition problem for the user, reads in the answer from the user, and then
checks to see if they got it right or wrong.
"""

import random

# This function will add two random two-digit integers together
# and ask the user to enter the answer
# then check if the user entered the correct answer


def add_nums():
    correct_answer_streak = 0

    while True:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        add_nums = num1 + num2
        print("What is", num1, "+", num2, "?" )
        your_answer = int(input("Your answer: "))

    
        
    #test if the user entered the correct answer
    
        if your_answer == add_nums:
            # Increase the correct answer counter.
            correct_answer_streak += 1
            print("Correct!")
            #print how many questions answered correctly in a row.
            print("You've gotten", correct_answer_streak, "in a row.")

            if correct_answer_streak == 3:
                break
            
        else:
            correct_answer_streak = 0
            print("Incorrect.")
            print("The expected answer is ", add_nums)
            
# This function will add the number of correct answers the user enters

def main():
    print("Khansole Academy")
    print("")
    add_nums()
    print("")
    print("You have completed the test.")
    print()
    print("Congratulations! You answer 3 in a row.")
       
    
    
    

    
    
if __name__ == '__main__':
    main()


    

