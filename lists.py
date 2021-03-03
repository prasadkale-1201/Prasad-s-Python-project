myUniqueList = []
myLeftOvers = []

def shoppinglist():
    myUniqueList1 = [input('1 : '),input('2 : '),input('3 : '),input('4 : '),input('5 : '),input('6 : '),input('7 : ')]
    for items in myUniqueList1:
        if items not in myUniqueList:
            output = True
            myUniqueList.append(items)
            print(output)
            print(myUniqueList)
        else:
            myLeftOvers.append(items)
            output = False
            print(output)
            print(myLeftOvers)
    return

ShoppingList = shoppinglist()

