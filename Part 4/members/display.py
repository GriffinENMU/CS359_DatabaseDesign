from util.prompt import prompt_enter


def display_members(conn):
    """
    Displays all members in the database.
    """

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Member")
    members = cursor.fetchall()

    if not members:
        print("No members found.")
        return

    print("MEMBERS")
    print("_______")
    for member in members:
        print(member)

    prompt_enter(to="go back")
