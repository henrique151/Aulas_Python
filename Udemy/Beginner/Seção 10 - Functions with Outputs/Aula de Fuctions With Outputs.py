# Funcitons With Outputs
def formatted_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    new_f_name = f_name.title()
    new_l_name = l_name.title()
    return f"{new_f_name} {new_l_name}"


print(formatted_name(input("What your first name? "),input("What your last name? ")))

# Already used functions with outputs.
#lenght = len(formatted_name)

#Return as an early exit
def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the tutle case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name}{formated_l_name}"
