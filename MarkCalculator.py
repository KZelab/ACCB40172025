
count = 0
numberOfStudents = 10
total = 0

while count < numberOfStudents:
    mark = int(input("Please enter a mark "))
    print(f"You have entered {mark}.")
    total = total + mark
    count = count + 1


average = total / count

print(f"The average mark calculated as {average}")