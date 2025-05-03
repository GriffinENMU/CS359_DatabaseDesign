from util.prompt import prompt_string, prompt_table_row, prompt_yes_no, prompt_enter


def delete_member(conn):
    """
    Deletes a member from the database. It prompts the user to select a member
    from the list of all members. It then confirms the deletion twice, the
    second time by asking the user to type the member's name. If the name does
    not match, the deletion is aborted. If the deletion is confirmed, it
    deletes the member from the database, as well as their payments and
    attendance records. Finally, it commits the changes to the database and
    prints a confirmation message.

    :param conn: The database connection object.
    :return: None
    """

    cursor = conn.cursor()

    members = cursor.execute("SELECT * FROM Member").fetchall()
    selected_member = prompt_table_row("member", rows=members)

    confirmed = prompt_yes_no(
        f"Warning: This action will delete the member {selected_member[1]} and all their payments and attendance records. Do you want to proceed?",
        default_to_no=True,
    )
    print()
    if not confirmed:
        return

    print(
        "CAUTION: THIS ACTION CANNOT BE UNDONE. PLEASE TYPE THE MEMBER'S NAME TO CONFIRM PERMANENT DELETION."
    )
    name = prompt_string("Name", max_length=50, default="")
    print()

    if name != selected_member[1]:
        print("Deletion aborted. The name does not match.")
        print()
        return

    cursor.execute(
        """
        DELETE FROM Payment
        WHERE memberId = ?
        """,
        (selected_member[0],),
    )

    cursor.execute(
        """
        DELETE FROM Attends
        WHERE memberId = ?
        """,
        (selected_member[0],),
    )

    cursor.execute(
        """
        DELETE FROM Member
        WHERE memberId = ?
        """,
        (selected_member[0],),
    )

    conn.commit()
    print(f"Deleted member {selected_member[1]} with ID {selected_member[0]}.")
    cursor.close()

    prompt_enter(to="go back")
