# Exercise 4 Display a solid rectangle of X characters
# where the user is allowed to enter the height of the rectangle.
# The width should be always be taken as 5.
# Once the rectangle is drawn display the message "A 5 x ? rectangle has been drawn“


height = int(input("Enter a height for the renderer"))
copyHeight = height

while height > 0:
    print("xxxxx")
    height = height - 1

print(f"a 5 x {copyHeight} rectangle has been drawn")

