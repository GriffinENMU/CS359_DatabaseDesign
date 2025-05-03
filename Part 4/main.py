import sys

from classes import classes
from equipmentmenu import equipment
from members import members_page
from signin import init_db
from util.prompt import prompt_option


def main_page(conn):
    """
    The main page of the CLI. It has options to navigate to the members page,
    classes page, and equipment page. It also has an option to exit the app.

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
                members_page(conn)
            case 2:
                classes(conn)
            case 3:
                equipment(conn)
            case _:
                break


def _main_menu():
    """
    Prints out the main menu and prompts the user to select an option.
    """

    print("MAIN MENU")
    print("_____________")
    print("Please make a selection to open the appropriate menu.")
    print("1) Members Menu")
    print("2) Classes Menu")
    print("3) Equipment Menu")
    print("0) Exit")

    return prompt_option(3)


if __name__ == "__main__":
    print("Initializing database")
    conn = init_db()
    try:
        main_page(conn)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Closing database")
        conn.close()
        sys.exit(0)
