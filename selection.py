
colour = "green"
age = 12

if colour == "green123":
    print("It is equal to green")
    # end of the scope of the if statement
    if colour == "green":
        print("This is nested even further, but it will never execute")
else:
    print("This is the alternative flow of code that executed because the first if was false")


print("This piece of code always executes")
