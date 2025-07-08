import random

myList = []

myList2 = [2,3,4, "fart", len("Fart")]

print(myList2)

myList.append(7)

myList.append(10)

myList.append(4)

# [ 7, 10, 4 ]


print(f"my list values {myList} and the length of the list is {len(myList)}")

print(len("the wet farts came with lumps"))


print(f"the popped off value {myList.pop()}" )

print("the altered list", myList)

total = myList[0] + myList[1]
print(total)


myList[0] = 10 # the item must already exist

total = myList[0] + myList[1]
print(total)

count = 0
while count < 50000:
    myList.append(random.randint(0, 50))
    count += 1

print(myList)
count = 0
while count < 50000:
    print(myList.pop())
    count += 1




print(myList)