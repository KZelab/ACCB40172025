# Exercise 5b (For Advanced Students)
#  bit trickier Display a solid rectangle of X characters where the user
# is allowed to enter the length of both sides of the rectangle.
# Constraint:
# To move to the next line you should use print("") It should look like this

WidthLength = int(input("Enter a width length"))
HeightLength = int(input("Enter a height length"))

while WidthLength <= 0 or HeightLength <= 0:
    if WidthLength <= 0:
        WidthLength = int(input("Try again dumbass, Enter a width length greater than zero"))

    if HeightLength <= 0:
        HeightLength = int(input("Try again dumbass, Enter a height length greater than zero"))


# for _ in range(HeightLength):
#     print("x" * WidthLength)


i = HeightLength
j = WidthLength
runningCount = 0
print(i, j)
while i > 0:
    while j > 0:
        runningCount += 1
        print("x", end="")
        j = j - 1

    j = WidthLength
    i = i - 1
    print("",end="\n")

print(f"The nested loop ran {runningCount} times")




