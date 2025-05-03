from util.prompt import prompt_string, prompt_int, prompt_table_row, prompt_enter
from util.validators import recordExists, isValidPhone

def update_member(conn):
    """
    Updates an existing member in the database. It prompts the user for the
    member's new details, including name, email, phone, address, age, and
    membership plan. It then updates the member's information in the database
    and renews their membership if a new plan is selected. Finally, it commits
    the changes to the database and prints a confirmation message.

    :param conn: The database connection object.
    :return: None
    """

    cursor = conn.cursor()

    members = cursor.execute("SELECT * FROM Member").fetchall()
    selected_member = prompt_table_row("member", rows=members)

    heading = f"UPDATE MEMBER {selected_member[0]}"
    print(heading)
    print("_" * len(heading))
    print(
        "Enter the new details for the member. Leave blank to keep the current value."
    )
    name = prompt_string("Name", max_length=50, default=selected_member[1])
    email = prompt_string("Email", max_length=50, default=selected_member[2])
    if email != selected_member[2] and recordExists(conn, "Member", "email", email):
        print("That email already exists. Please use another email.")
        return        
    phone = prompt_string("Phone", max_length=15, default=selected_member[3])
    while not isValidPhone(phone):
        print("Invalid format. Phone number must be 10-15 digits.")
        phone = prompt_string("Phone", max_length=15, default=phone)  
          
    address = prompt_string("Address", max_length=100, default=selected_member[4])
    age = prompt_int("Age", min_value=15, default=selected_member[5])

    print()
    print(
        "SELECT A MEMBERSHIP PLAN TO RENEW THE MEMBERSHIP, OR LEAVE BLANK TO KEEP THE CURRENT PLAN"
    )

    membership_plans = cursor.execute("SELECT * FROM MembershipPlan").fetchall()
    selected_plan = prompt_table_row(
        "membership plan", rows=membership_plans, default=-1
    )

    cursor.execute(
        """
		UPDATE Member
		SET name = ?, email = ?, phone = ?, address = ?, age = ?
		WHERE memberId = ?
		""",
        (name, email, phone, address, age, selected_member[0]),
    )

    if selected_plan is not None:
        membership_end_date_function = (
            f"DATE('now', '+1 {'month' if selected_plan[1] == 'Monthly' else 'year'}')"
        )
        cursor.execute(
            f"""
			UPDATE Member
			SET membershipStartDate = DATE('now'),
			    membershipEndDate = {membership_end_date_function}
			WHERE memberId = ?
			""",
            (selected_member[0],),
        )

        cursor.execute(
            """
			INSERT INTO Payment (memberId, planId, amountPaid, paymentDate)
			VALUES (?, ?, ?, DATE('now'))
			""",
            (selected_member[0], selected_plan[0], selected_plan[2]),
        )
        print(f"Renewed membership.")

    conn.commit()
    print(f"Updated member.")
    cursor.close()

    prompt_enter(to="go back")
