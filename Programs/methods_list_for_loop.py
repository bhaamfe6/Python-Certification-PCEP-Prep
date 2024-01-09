"""
This program is more practice using lists and dictionaries with for loops.
I attempt to create functions, then turn those functions into variables that
will be passed into a list.  Then I will attempt to create a for loop that loops
through each function.
"""

# This function will receive input of a user's first name
def user_first_name():
    user_fname = input("Enter your first name: ")
    # The return outputs the information received in the input variable
    return user_fname

# This function will receive input of a user's last name
def user_last_name():
    user_lname = input("Enter your last name: ")
    return user_lname

# This function will receive input of a user's age
def user_age():
    user_age = input("Enter your age: ")
    return user_age

def main():
# Create an empty user list
    user_fn_list = []
    user_age_list = []
    fname_age_dict = {}
    fname_lname_dict = {}

    while True:
        # Create variables that executes the functions in the functions
        fname = user_first_name()
        lname = user_last_name()
        age = user_age()

        

        # Add the input from the variables fname, lname, and age to the user_list
        user_fn_list.append(fname)
        user_age_list.append(age)

        # Adds fname input as keys in fname_age dictionary and fname_lname dictionaries
        # with age and lname  inputs as values in the dictionaries
        fname_age_dict[fname] = age
        fname_lname_dict[fname] = lname
            
        
        if fname == "":
            break

    #Loop though the user_list which is a list of three functions that returns output
    # of first name, last name, and age
    
    for user in user_fn_list:
        print(user)

    #print the list contents    
    print("This is the first name list: ", user_fn_list)
    print("This is the age list: ", user_age_list)
    print("This is the first name and age dictionary: ", fname_age_dict)
    print("This is the first name and last name dictionary: ", fname_lname_dict)
    
if __name__ == '__main__':
    main()
