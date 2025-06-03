
mark = int(input("Please enter a mark for a student"))

if mark >= 0 and mark <= 100:
    print("VALID")

if mark < 0 or mark > 100:
    print("INVALID")

if mark > 40 :
    print("Pass")
else :
    if mark > 20 :
        print("Fail")
    else :
        print("OMG")


