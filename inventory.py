"""HW0: a game inventory. Practises Session 1: names and objects, defaults, *args, comprehensions."""


def add_item(inventory, item, count=1):
    """Return a new inventory with count more of item. Do not change inventory."""
    new_inventory = inventory.copy()
    new_inventory[item] = new_inventory.get(item, 0) + count
    return new_inventory
    



def total_items(*inventories):
    """Return how many items there are in all the inventories together."""
    total = 0
    for inventory in inventories:
        total += sum(inventory.values())
    return total
    


def running_low(inventory, limit=2):
    """Return the names of items with fewer than limit left, sorted A to Z."""
    low_items = []
    for item, count in inventory.items():
        if count < limit:
            low_items.append(item)
    return sorted(low_items)        
    
