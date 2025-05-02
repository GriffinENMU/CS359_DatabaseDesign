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

    # This line is unreachable, but we need to return something to get rid of
    # the IDE warning.
    return 0


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
