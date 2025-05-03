from util.prompt import prompt_string, prompt_int, prompt_table_row, prompt_enter


def add_member(conn):
    """
    Adds a new member to the database. It prompts the user for the member's
    details, including name, email, phone, address, age, and membership plan.
    It then inserts the new member into the database and associates them with
    the selected membership plan. Finally, it commits the changes to the
    database and prints the ID of the newly created member.

    :param conn: The database connection object.
    :return: None
    """

    cursor = conn.cursor()

    print("ADD MEMBER")
    print("__________")
    print("Enter the following details to add a new member:")

    name = prompt_string("Name", max_length=50)
    email = prompt_string("Email", max_length=50)
    phone = prompt_string("Phone", max_length=15)
    address = prompt_string("Address", max_length=100)
    age = prompt_int("Age", min_value=15)

    print()

    membership_plans = cursor.execute("SELECT * FROM MembershipPlan").fetchall()
    selected_plan = prompt_table_row("membership plan", rows=membership_plans)
    membership_end_date_function = (
        f"DATE('now', '+1 {'month' if selected_plan[1] == 'Monthly' else 'year'}')"
    )

    cursor.execute(
        f"""
		INSERT INTO Member (name, email, phone, address, age, membershipStartDate, membershipEndDate)
		VALUES (?, ?, ?, ?, ?, DATE('now'), {membership_end_date_function})
		""",
        (name, email, phone, address, age),
    )
    member_id = cursor.lastrowid

    cursor.execute(
        """
		INSERT INTO Payment (memberId, planId, amountPaid, paymentDate)
		VALUES (?, ?, ?, DATE('now'))
		""",
        (member_id, selected_plan[0], selected_plan[2]),
    )

    conn.commit()
    print(f"Created member with ID {member_id}.")
    cursor.close()

    prompt_enter(to="go back")
