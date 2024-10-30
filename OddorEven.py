# Odd or Even Checker as Function
def OddorEven(num):
    if int(num % 2 == 0):
        print("The number", num, "is Even!")
        # added math check for odd
    elif int(num % 2 == 1):
        print("The number", num, "is Odd!")


print("Enter a number:")
# added check for string
try:
    OddorEven(int(input()))
except ValueError:
    print("Enter a number only!")
