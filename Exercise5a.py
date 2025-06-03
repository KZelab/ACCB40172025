#Display a line of X characters where the user is allowed to enter the length of the line.
# Once the line is printed you should display the message
# "A line of length ? has been displayed“

lineLength = int(input("Enter a length"))

lineLengthcopy = lineLength

while lineLength > 0:
    print("x", end="")
    lineLength = lineLength - 1;


print(f"\na line of length {lineLengthcopy} has been displayed")