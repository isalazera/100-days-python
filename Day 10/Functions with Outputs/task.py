def format_name(f_name, l_name):
    # title() capitalizes the first letter and makes the rest of the string lowercase
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

f_name = input('Enter first name: ')
l_name = input('Enter last name: ')

output = format_name(f_name, l_name)
print(output)

