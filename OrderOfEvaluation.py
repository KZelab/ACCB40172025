
def StartMenu():
    menuValue = int(input("Enter 1 for option A, 2 for option B or 3 to exit"))

    if menuValue == 1:
        print("Option A")
    elif menuValue == 2:
        print("Option B")
    elif menuValue == 3:
        return True
    else:
        print("Unkown option")

    return False





stopLooping = False

while stopLooping == False:
    stopLooping = StartMenu()


