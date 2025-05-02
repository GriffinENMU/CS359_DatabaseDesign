def prompt_option(max_n):
    """
    Prompts the user to select an option (an integer) from 0 to max_n. It keeps
    prompting until a valid option is entered. It then returns the selected
    option.

    :param max_n: The maximum option number.
    :return: The selected option.
    """

    option = _prompt_option(max_n)

    print()  # Empty line for better readability
    return option


def _prompt_option(max_n):
    while True:
        option_str = input("Choose an option: ").strip()

        try:
            # int() will throw an exception if the input is not a number, in
            # which case we restart the loop
            option = int(option_str)

            if option in range(0, max_n + 1):
                return option

        except:
            continue


def prompt_int(prompt, min_value=0, max_value=None):
    """
    Prompts the user for an integer input. It keeps prompting until a valid
    integer is entered. It then returns the input.

    :param prompt: The prompt message to display to the user.
    :param min_value: The minimum value of the input integer.
    :param max_value: The maximum value of the input integer.
    :return: The integer input from the user.
    """

    while True:
        value_str = input(f"{prompt}: ").strip()

        try:
            # int() will throw an exception if the input is not a number, in
            # which case we restart the loop
            value = int(value_str)

            if min_value is not None and value < min_value:
                print(f"Input cannot be less than {min_value}. Please try again.")
                continue

            if max_value is not None and value > max_value:
                print(f"Input cannot be greater than {max_value}. Please try again.")
                continue

            return value

        except:
            print("Invalid input. Please enter a valid integer.")


def prompt_string(prompt, max_length):
    """
    Prompts the user for a non-empty string input. It keeps prompting until a
    valid input is entered. It then returns the input.

    :param prompt: The prompt message to display to the user.
    :param max_length: The maximum length of the input string.
    :return: The non-empty string input from the user.
    """

    while True:
        value = input(f"{prompt}: ").strip()

        if len(value) == 0:
            print("Input cannot be empty. Please try again.")
            continue

        if len(value) > max_length:
            print(
                f"Input cannot be longer than {max_length} characters. Please try again."
            )
            continue

        return value


def prompt_table_row(table_name, rows):
    """
    Prompts the user to select a row from a table in the database. It keeps
    prompting until a valid row is selected. It then returns the selected row.

    :param table_name: The name of the table to display.
    :param rows: The rows to display from the table.
    :return: The selected row from the table.
    """

    option = _prompt_table_row(table_name, rows)

    print()  # Empty line for better readability
    return option


def _prompt_table_row(table_name, rows):
    if not rows:
        print(f"No {table_name} found.")
        return None

    print(f"{table_name.upper()}")
    print("_" * len(table_name))
    for i, row in enumerate(rows):
        print(f"{i + 1}) {row}")

    while True:
        value_str = input(f"Select a {table_name} by number (1-{len(rows)}): ").strip()

        try:
            choice = int(value_str)

            if 1 <= choice <= len(rows):
                return rows[choice - 1]

            print(f"Please enter a number between 1 and {len(rows)}.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def prompt_enter(to="continue"):
    """
    Prompts the user to press ENTER to continue. This is not strictly necessary
    for the purposes of flow control, but it is a good practice to give the user
    time to read the output before moving on.

    :param to: Describes the action that will be taken after pressing ENTER.
    """

    print()
    input(f"Press ENTER to {to}.")
    print()
