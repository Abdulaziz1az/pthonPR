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

# get menu choice from the user
def get_menu_choice():
    print()
    print("Friends and Their Birthdays")
    print("---------------------------")
    print("1. Look up a birthday")
    print("2. Adda new birthday")
    print("3. Change a birthday")
    print("4. Delete a birthday")
    print("5. Quite the program")
    print()

    # get the user choice
    choice = int(input("Enter your choice : "))

    # Validate the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int (input("Enter a valid choice: "))
    return choice

    # function looks up a name in the birthdays 
    def look_up(birthdays):
        name = input(" Enter a name: ")
        # Look it iup in the dictinary
        print(birthdays.get(name, 'Not found.'))

    # The add function adds a new entry into the birthdays dictionary
    def add(birthdays):
        # Get a name and birthday
        name = input("Enter a name: ")
        bday = input("Enter a birthday: ")

        # if the name does not exist, add it.
        if name not in birthdays:
            brithdays[name] = bday
        else:
            print("That enntry alread exists.")
        
