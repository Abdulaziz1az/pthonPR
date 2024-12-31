# This program use dictinary to keep friends names and birthdays
# Global constant
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# main function
def main():
    # empty dictionary.
    birthdays = {}
#user menu
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)
