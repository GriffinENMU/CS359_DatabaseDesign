from members.display import display_members
from members.add import add_member
from members.update import update_member
from util.prompt import prompt_option


def members_page(conn):
    """
    The members page of the CLI. It has five options:

    1. Display all members
    2. Add a new member
    3. Update a member
    4. Delete a member
    5. Go back to the main menu (0)
    """

    while True:
        option = _members_menu()

        match option:
            case 1:
                display_members(conn)
            case 2:
                add_member(conn)
            case 3:
                update_member(conn)
            case _:
                break


def _members_menu():
    """
    Prints out the members menu and prompts the user to select an option.
    """

    print("MEMBERS MENU")
    print("____________")
    print("1) Display all members")
    print("2) Add a new member")
    print("3) Update a member")
    print("4) Delete a member")
    print("0) Go back to main menu")

    return prompt_option(4)
