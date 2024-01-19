import random

"""
This program will loads word from a file cswords.txt into an empty list. The list
will then print random words from the list.  This will repeat and wait until the
hits enter. When the user hits enter another word will show. 
"""

# Create a variable that with the value of the file name
FILE_NAME = 'cswords.txt'


def main():
    # craete a variable to open the file 
    open_file = open(FILE_NAME)
    
    
    # Create an empty list that appends all of the lines in the file into the empty
# list
    file_list = []
    # for loop to add each line of the file to the empty list
    for line in open_file:
        file_list.append(line)
    
    print(file_list)
    print()
    print("_______________")
    while True:
        #create a variable that chooses a random word from the list
        random_word = random.choice(file_list)
        #repeat every time the user hits enter
        user_enter = input()
        print(random_word)
    
if __name__ == '__main__':
    main()
