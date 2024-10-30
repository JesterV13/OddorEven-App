# Turned Odd or Even Checker into a Function
def OddorEven(num):
    if int(num % 2 == 0):
        print("The number", num, "is Even!")
    else:
        print("The number", num, "is Odd!")


print("Enter a number:")
OddorEven(int(input()))
