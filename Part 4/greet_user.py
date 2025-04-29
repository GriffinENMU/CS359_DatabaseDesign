from util.prompt import prompt_enter


def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

    prompt_enter(to="go back")
