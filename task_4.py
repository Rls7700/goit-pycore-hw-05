from typing import Dict, List, Tuple, Callable

def input_error(func: Callable):
    """
    деоратор для обробки помилок вводу від користувача
    обгортаємо" ф-ю (add_contact)
    якщо в середині помилка то програма не завершується
    а повертає такст повідомлення
    """
    def inner(*args, **kwargs):
        try:

            # пробуємо виконати загорнуту ф-ю
            return func(*args,**kwargs)
        
        except IndexError:
            # команда phone без імені ->викликає IndexError
            return "Enter the argument for the command"
        
        except ValueError:
            # імя без тел -> name,phone = args дасть ValueError
            return "Give me name and phone please"
        
        except KeyError:
            #наприклад запитали тел контакта якого немає
            return "Contact not found"
        
    return inner

def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Розбирає введення користувача на:
    команду
    список аргументів
    """
    parts = user_input.strip().split()

    # якщо натиснув просто Enter -> parts буде порожній
    if not parts:
        return "", []
    
    # перше слово -це команда
    command = parts[0].lower()

    # все інше аргументи
    args = parts[1:]

    return command, args

@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    додає новий контакт
    очікує args = [name, phone]
    """
    name, phone = args

    # зберігаємо в словник ключ = імя, значення = тел
    contacts[name] = phone
    return "Contact added"

@input_error
def change_contact(args: List[str], contacts: Dict[str,str]) -> str:
    """
    оновлює тел існуючого контакту
    """
    name, phone = args

    # якщо контакта немає -  KeyError
    # щоб декоратор повернув "Contact not found"
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated"

@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """
    показує тел контакта
    очікує args = [name]
    """
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"{name}: {contacts[name]}"

@input_error
def show_all(contacts: Dict[str, str]) -> str:
    """
    показує всі контакти
    """
    if not contacts:
        return "No contacts yet"
    
    # формує список рядків "імя: телефон"
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]

    # обєднуємо рядки через перенос строки
    return "\n" .join(lines)

def main() -> None:
    """
    готовий цикл бота
    програма чекає команди користувача
    """

    contacts: Dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        # просимо ввод команди
        user_input = input("Enter a command: ")

        # розбираємо команду та аргументи
        command, args = parse_input(user_input)

        # команди виходу
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