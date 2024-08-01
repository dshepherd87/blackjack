def input_integer(prompt_string):
    while True:
        user_input = input(prompt_string)
        try:
            user_int = int(user_input)
            break
        except ValueError:
            print(f"Invalid input. {user_input} is not an integer.")
    return user_int

def input_float(prompt_string):
    while True:
        try:
            user_input = float(input(prompt_string))
            break
        except ValueError:
            print("Invalid input. Please enter a valid floating-point number")
    return user_input 

def input_string(prompt_string):
    while True:
        user_input = input(prompt_string).strip()
        if len(user_input) > 0:
            break
        else:
            print("Invalid input. Please enter a valid string")
    return user_input

def input_yes_no(prompt_string):
    while True:
        user_input = input(prompt_string).strip()
        if user_input in ['y', 'Y', 'n', 'N']:
            break
        else:
            print("Invalid input. Response must be y (yes) or n (no)")
    return user_input