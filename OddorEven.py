# Odd or Even Checker as Function
def odd_even_checker(num):
    if (num % 2 == 0):
        print("The number", num, "is Even!")
        # math check for odd
    elif (num % 2 == 1):
        print("The number", num, "is Odd!")

# added exit function
def exit_program():
    print("Farewell...")
    exit()

# greeting to app
# added additional greeting for program exit
print("Welcome to the ODD or EVEN app")
print('If you would like to exit at anytime, type "Stop".\n')
print("Please Enter a Number:")

# added a while "true" loop to run the program until ended
while True:
    # check for string
    try:
        # added exit call key and moved input to its own variable
        num = input()
        if num.lower() == "stop":
            exit_program()
        else:
            num = int(num)
            odd_even_checker(num)

    except ValueError:
        print("Enter a Number only!")
