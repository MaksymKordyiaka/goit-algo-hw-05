def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as error:
            if isinstance(error, KeyError):
                return 'Key error'
            elif isinstance(error, ValueError):
                return 'Error! if you want to:\n' \
                       'add contact: you must input ("add" username phone).\n' \
                       'change phone: you must input ("change" username phone) or no contacts.\n' \
                       'get phone: you must input ("phone" username)\n'
            elif isinstance(error, IndexError):
                return 'Index error'
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for '{name}' changed."
    else:
        return f"Contact {name} not found."

def show_all(contacts):
    if not contacts:
        return 'No contacts available, you need to (add "username" "phone")'
    else:
        result = ''
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()

@input_error
def get_phone(args, contacts):
    name, = args
    phone = contacts.get(name)
    if phone:
        return f"Phone number for '{name}': {phone}"
    else:
        return f"Contact {name} not found."

def main():
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
            print(change_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()