# Display "Goodbye" and ask the user if they wish to quit.
# Repeatedly do this until user decides type "yes"


print("goodbye")

exitcriteria = "yes"


response = input("Enter yes to quit").lower()


while response != exitcriteria:
    print("goodbye")
    response = input("Enter yes to quit").lower()


    if(response == exitcriteria):
        break

