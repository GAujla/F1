import pprint

item_total = 0
def displayInventroy(inventory):
    item_total = 0 
    for k,v in inventory.items():
        print(v,k)
        item_total += v
    print("Total number of items: "  + str(item_total))
        
def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory 


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventroy(stuff)
print('//////////')
inv = addToInventory(stuff, dragonLoot)
print(inv)
print('//////////')
displayInventroy(inv)