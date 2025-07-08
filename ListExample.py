def AddItemToList(myList):
    print("We are inside the function before addition: ", listExample)
    myList.append(10)
    print("We are inside the function after addition: ", listExample)

listExample = []

listExample.append(5)
listExample.append(4)
listExample.append(3)

print("List before function call, ", listExample)
AddItemToList(listExample)
print("List after function call, ", listExample)