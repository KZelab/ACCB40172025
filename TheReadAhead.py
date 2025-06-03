number1 = int(input("Please enter a number (999 to exit) : "))

while number1 != 999:
    sq = number1 * number1
    print(f"The square of {number1} is {sq}")
    number1 = int(input("Please enter a number (999 to exit) : "))

print("Finished looping")