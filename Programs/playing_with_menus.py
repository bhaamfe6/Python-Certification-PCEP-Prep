"""
This program will create a menu that displays an introduction that includes a graphic
click to start button that leads the user to a submenu.  The submenu will ask the
user to enter information about themselves which will be stored into lists and dictionaries.
"""






def main_menu():
    # This is a collection of print statements which will display a welcome message
    print("****_____________________________****")
    print("****_____________________________****")
    print("**                                 **")
    print("**             HELLO!              **")
    print("**                                 **")
    print("**              AND                **")
    print("**                                 **")
    print("**         WELCOME TO THE          **")
    print("**                                 **")
    print("**       EARLY LEARNERS CLUB       **")
    print("****_____________________________****")
    print("****_____________________________****")
    print()
    print()

    print("MAKE A SELECTION BELOW:")

    # This will require the user to choose which submenu to go to, either create a new account or
    # the log in menu.
    
    login_or_create_new =  int(input("To Log In Enter 1. To Create New Account Enter 2: "))

    if login_or_create_new != 1:
        sub_menu_create_new()
    else:
        log_in_menu()
        
def sub_menu_create_new():
# This function will require the user to enter all new information to create a new account
    create_unique_username = input("Create a unique user name: ")
    print()
    create_password = input("Create your password: ")
    print()
    user_first_name = input("Enter your first name: ")
    print()
    user_last_name = input("Enter your last name: ")
    print()
    user_date_of_birth = input("Enter your date of birth in mmddyyyy format: ")
    print()

def log_in_menu():
    #If the user has an account they will be able to log in.
    enter_username = input("Enter your username: ")
    print()
    enter_password = input("Enter your password: ")

def main():
    main_menu()

if __name__ == '__main__':
    main()
