numberOfLoops = int(input("Enter anumber less than 10 or 0 to exit"))


while False:
    if numberOfLoops == 0:
        break
    print(f"You entered {numberOfLoops}")
    if numberOfLoops < 10:
        print("Less than 10")
    else:
        print("more than 10")
    numberOfLoops = (numberOfLoops - 1)




