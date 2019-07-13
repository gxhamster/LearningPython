inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'dagger', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inv, addedItems):
    itemDict = {}
    for items in addedItems:
        itemDict.setdefault(items, addedItems.count(items))
        
    for keys, values in itemDict.items():
        if inv.get(keys) == None:
            inv.setdefault(keys, values)
        else:
            inv[keys] =  inv[keys] + itemDict[keys]
        
    return inv

def displayInventory(inv):
    print('Inventory: ')
    totalItems = 0

    for key, value in inv.items():
        print(value, key)
        totalItems = totalItems + value
    print('Total Number of Items: ', totalItems)

    return totalItems


inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
