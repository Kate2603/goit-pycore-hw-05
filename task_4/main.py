def input_error(func):
    """
    Decorator to handle input errors and return appropriate messages to the user.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input format."
        except IndexError:
            return "Missing arguments."

    return inner

def parse_input(user_input):
    """
    Parse the user input into a command and its arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """
    Change the phone number of an existing contact.
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    """
    Show the phone number of a contact.
    """
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

@input_error
def show_all(contacts):
    """
    Show all contacts and their phone numbers.
    """
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        return "Contact list is empty."

def main():
    """
    Main function to control the command processing loop.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
