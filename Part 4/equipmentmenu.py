from util.prompt import prompt_option


def equipment(conn):
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
                show_equipment_menu(conn)
            case 2:
                insert_equipment_menu(conn)
            case 3:
                update_equipment_menu(conn)
            case 4:
                delete_equipment_menu(conn)

            case _:
                break


def _submenu():
    """
    Prints out the submenu and prompts the user to select an option.
    """

    print("EQUIPMENT MENU")
    print("_____________")
    print("Please make a selection to perform the selected function.")
    print("1) Show all equipment entries.")
    print("2) Insert new equipment.")
    print("3) Update equipment.")
    print("4) Delete equipment")
    print("0) Go back")

    return prompt_option(4)


def show_equipment_menu(conn):
    """
    Query all rows in the Equipment table
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Equipment")

    rows = cur.fetchall()
    for row in rows:
        print(row)


def insert_equipment_menu(conn):
    """
    Insert new equipment: name, type, quantity, and gym ID.
    Only allows types already in Equipment.type.
    """
    cur = conn.cursor()

    
    while True:
        name = input("Equipment name: ").strip()
        if not name:
            print("Name cannot be empty.")
        elif len(name) > 50:
            print("The name is too long (50 char max).")
        else:
            break

    cur.execute("SELECT DISTINCT type FROM Equipment;")
    types = [r[0] for r in cur.fetchall()]
    print("Allowed types:", types)
    while True:
        type_ = input("Equipment type (must match one above): ").strip()
        if type_ in types:
            break
        print(f"'{type_}' is not a valid type. Choose from {types}.")

    while True:
        qty_str = input("Quantity (integer): ").strip()
        try:
            quantity = int(qty_str)
            if quantity < 0:
                print("Quantity must be positive.")
            else:
                break
        except ValueError:
            print("Please enter a valid whole number for quantity.")

    while True:
        gym_str = input("Gym ID (integer): ").strip()
        try:
            gymId = int(gym_str)
        except ValueError:
            print("Please enter a valid whole number for Gym ID.")
            continue

        cur.execute(
            "SELECT 1 FROM GymFacility WHERE gymId = ?;",
            (gymId,),
        )
        if not cur.fetchone():
            print(f"Gym ID {gymId} does not exist.")
            continue
        break

    sql = """
    INSERT INTO Equipment(name, type, quantity, gymId)
         VALUES (?, ?, ?, ?)
    """
    cur.execute(sql, (name, type_, quantity, gymId))
    conn.commit()

    new_id = cur.lastrowid
    print(f"\nInserted equipment with ID {new_id}.")

    cur.execute(
        "SELECT equipmentId, name, type, quantity, gymId FROM Equipment WHERE equipmentId = ?;",
        (new_id,),
    )
    inserted = cur.fetchone()
    print("\nInserted entry:")
    print(inserted)
    input("Press ENTER to return to the equipment menu.")


def update_equipment_menu(conn):
    """
    Update equipment details by equipment ID, then print the updated row.
    """
    cur = conn.cursor()


    while True:
        id_str = input("Enter equipment ID to update: ").strip()
        if not id_str.isdigit():
            print("Invalid ID. Please enter a positive integer.")
            continue
        equipmentId = int(id_str)
        break

    cur.execute(
        "SELECT equipmentId, name, type, quantity, gymId FROM Equipment WHERE equipmentId = ?;",
        (equipmentId,),
    )
    current = cur.fetchone()
    if not current:
        print(f"No equipment found with ID {equipmentId}.")
        input("Press ENTER to return to the equipment menu.")
        return

    print("\nCurrent entry:")
    print(current)
    print("\nPress ENTER at any prompt to keep its current value.\n")


    while True:
        new_name = input(f"New name [{current[1]}]: ").strip()
        if not new_name:
            name = current[1]
            break
        if len(new_name) > 50:
            print("Name is too long (Max 50 chars).")
            continue
        name = new_name
        break

    cur.execute("SELECT DISTINCT type FROM Equipment;")
    types = [r[0] for r in cur.fetchall()]
    print("Allowed types:", types)
    while True:
        new_type = input(f"New type [{current[2]}]: ").strip()
        if not new_type:
            type_ = current[2]
            break
        if new_type in types:
            type_ = new_type
            break
        print(f"'{new_type}' is not valid. Choose from {types}.")


    while True:
        q_in = input(f"New quantity [{current[3]}]: ").strip()
        if not q_in:
            quantity = current[3]
            break
        if not q_in.isdigit():
            print("Please enter a valid whole number for quantity.")
            continue
        quantity = int(q_in)
        if quantity < 0:
            print("Quantity must be zero or positive.")
            continue
        break


    while True:
        g_in = input(f"New Gym ID [{current[4]}]: ").strip()
        if not g_in:
            gymId = current[4]
            break
        if not g_in.isdigit():
            print("Please enter a valid whole number for Gym ID.")
            continue
        candidate = int(g_in)
        cur.execute(
            "SELECT 1 FROM GymFacility WHERE gymId = ?;",
            (candidate,),
        )
        if cur.fetchone() is None:
            print(f"Gym ID {candidate} does not exist.")
            continue
        gymId = candidate
        break

   
    sql = """
    UPDATE Equipment
       SET name     = ?,
           type     = ?,
           quantity = ?,
           gymId    = ?
     WHERE equipmentId = ?
    """
    cur.execute(sql, (name, type_, quantity, gymId, equipmentId))
    conn.commit()

   
    cur.execute(
        "SELECT equipmentId, name, type, quantity, gymId FROM Equipment WHERE equipmentId = ?;",
        (equipmentId,),
    )
    updated = cur.fetchone()
    print("\nUpdated entry:")
    print(updated)
    input("Press ENTER to return to the equipment menu.")

def delete_equipment_menu(conn):
    """
    Delete equipment by ID.
    Prompts the user to enter an equipmentId and confirms the deletion
    """
    cur = conn.cursor()

    try:
        equipment_id = int(input("Enter equipment ID to delete: ").strip())
    except ValueError:
        print("Invalid ID format. Must be an integer.")
        input("Press ENTER to return to the equipment menu.")
        return

    cur.execute(
        "SELECT equipmentId, name, type, quantity, gymId FROM Equipment WHERE equipmentId = ?;",
        (equipment_id,),
    )
    row = cur.fetchone()

    if not row:
        print(f"No equipment found with ID {equipment_id}.")
        input("Press ENTER to return to the equipment menu.")
        return

    print("\nSelected entry:")
    print(row)

    confirm = input(
        f"Are you sure you want to delete equipment #{equipment_id}? (Y/N): "
    ).lower()
    if confirm != "y":
        print("Delete canceled.")
    else:
        cur.execute("DELETE FROM Equipment WHERE equipmentId = ?;", (equipment_id,))
        conn.commit()
        print(f"Deleted {cur.rowcount} row(s).")

    input("Press ENTER to return to the equipment menu.")
