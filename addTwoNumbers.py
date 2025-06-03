#Exercise 2 Allow the user to add two numbers together
# but allow them to do this repeatedly until they decide to stop.


while True:

    number1 = int(input("Enter the first number"))

    number2 = int(input("Enter the second number"))

    print(f"The result: = {number1 + number2}")

    exit = input("Press q to exit or any to continue")
    if exit == "q":
        break
