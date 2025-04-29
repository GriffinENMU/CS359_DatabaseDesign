from greet_user import greet_user
from util.prompt import prompt_option


def subpage():
    """
    The submenu of the CLI. It has two options:

    1. Greet the user whose name is given
    2. Go back to the main menu by entering 0.

    It works by running an infinite loop, which runs the corresponding function
    based on the option entered by the user, and brings us back to this menu
    once that task is completed (once the function returns). If the user enters
    0, we break out of the loop, effectively exiting this page and giving
    control back to the main menu.
    """
    while True:
        option = _submenu()

        match option:
            case 1:
                greet_user()
            case _:
                break


def _submenu():
    """
    Prints out the submenu and prompts the user to select an option.
    """

    print("SUBMENU")
    print("_____________")
    print("1) Greet user")
    print("0) Go back")

    return prompt_option(1)
