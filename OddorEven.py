# Odd or Even Checker as Function
def OddorEven(num):
    if int(num % 2 == 0):
        print("The number", num, "is Even!")
        # math check for odd
    elif int(num % 2 == 1):
        print("The number", num, "is Odd!")


# added greeting to app
print("Welcome to the ODD or EVEN app")
print("Please Enter a Number:")

# added a while loop to run the program until user ended
i = 1
while i == 1:
    # check for string
    try:
        OddorEven(int(input()))

        # user input to end program
        user_input = input("Would you like to exit the program? (y/n): ")
        if user_input.lower() == "y":
            i = i - 1

    except ValueError:
        print("Enter a number only!")
