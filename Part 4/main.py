from greet_user import greet_user
from submenu import subpage
from util.prompt import prompt_option


def main_page():
    """
    The main page of the CLI. It has three options:

    1. Greet the user whose name is given
    2. Enter a submenu
    3. Exit the app by entering 0.

    It works by running an infinite loop, which runs the corresponding function
    based on the option entered by the user, and brings us back to this menu
    once that task is completed (once the function returns). If the user enters
    0, we break out of the loop, effectively exiting this page and, thus, the
    entire app.
    """

    while True:
        option = _main_menu()

        match option:
            case 1:
                greet_user()
            case 2:
                subpage()
            case _:
                break


def _main_menu():
    """
    Prints out the main menu and prompts the user to select an option.
    """

    print("MAIN MENU")
    print("_____________")
    print("1) Greet user")
    print("2) Submenu")
    print("0) Exit")

    return prompt_option(2)


if __name__ == "__main__":
    main_page()
