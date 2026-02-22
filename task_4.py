from typing import Dict, List, Tuple, Callable

def input_error(func: Callable):
    """Декоратор для обробки помилок вводу від користувача"""

    def inner(*args, **kwargs):
        try:
            return func(*args,**kwargs)
        
        except IndexError:
            return "Enter the argument for the command"
        
        except ValueError:
            return "Give me name and phone please"
        
        except KeyError:
            return "Contact not found"
        
    return inner


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """Розбирає введення користувача"""
    parts = user_input.strip().split()
    if not parts:
        return "", []
    
    command = parts[0].lower()
    args = parts[1:]
    return command, args


@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Додає новий контакт очікує args = [name, phone]"""
    name, phone = args
    contacts[name] = phone
    return "Contact added"


@input_error
def change_contact(args: List[str], contacts: Dict[str,str]) -> str:
    """Оновлює тел. існуючого контакту"""
    name, phone = args
    if name not in contacts:
        raise KeyError
    
    contacts[name] = phone
    return "Contact updated"


@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """Показує тел контакта очікує args = [name]"""
    name = args[0]
    if name not in contacts:
        raise KeyError
    
    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts: Dict[str, str]) -> str:
    """Показує всі контакти"""
    if not contacts:
        return "No contacts yet"
    
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n" .join(lines)


def main() -> None:
    """Готовий цикл бота"""
    contacts: Dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            print("Good bye!")
            
        elif command == "Hello":
            print("How can i help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command =="phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        elif command == "":

            continue

        else:
            print("Invalid command")
            

if __name__ == "__main__":
    main() 