
def convert_100_to_celsius():
    # converting between fahrenheit and celsius is to: first subtract 32, then multiply by 5/9. 
    # Convert a temperature of 100 degrees fahrenheit to celsius
    (100-32) * (5/9)
    # Save this to a variable called celsius_100, and use print() to print out the value
    celsius_100 = 37.777
    print(celsius_100)

    # Is the resulting temperature you get an integer or float?
    # Print 'float' if it is a float or 'int' if it is an int
    print("float")

    # How do you know? Write a comment below your code explaining how you know which it is
    # the result has a decimal

# convert_100_to_celsius()

def convert_0_to_celsius():
    # Convert a temperature of 0 degrees fahrenheit to celsius
    (0-32) * 5/9
    # Save this to a variable called celsius_0, and use print() to print out the value
    celsius_0 = (0-32) * 5/9
    print(celsius_0)

# convert_0_to_celsius()

def convert_34_2_to_celsius():
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # (34.2-100) * (5/9)
    # Do this one all in one print statement without saving any variables
    # print(34.2 - 100 * 5/9)
    print((34.2-32) * 5/9)
# convert_34_2_to_celsius()

# Now, can you convert back?


def convert_5_to_fahrenheit():
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    # print((5 * 9/5 + 32))
    print(5 * 1.8 + 32)
# convert_5_to_fahrenheit()

def hotter_temp():
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively
    print("30.2 degrees celsius")
# hotter_temp()
