# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

while True:
    try:
        provided_input = int(input("Please provide a valid integer: "))
    except ValueError:
        print("Regretfully that's not a valid integer - please try again!")
    else:
        break
