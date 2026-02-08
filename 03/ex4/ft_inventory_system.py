import sys


def current_inventory(inventory: dict[str, int], total_items: int) -> None:
    print("\n=== Current Inventory ===")
    for item in inventory:
        percent_of_inventory = inventory[item] / total_items * 100
        if inventory[item] > 1:
            print(f"{item}: {inventory[item]} units\
 ({percent_of_inventory:.1f}%)")
        else:
            print(f"{item}: {inventory[item]} unit\
 ({percent_of_inventory:.1f}%)")


def inventory_statistics(inventory: dict[str, int]) -> None:
    most_abundant: tuple[str, int] = ("", 0)
    less_abundant: tuple[str, int] = ("", 0)
    for item in inventory:
        if most_abundant[1] < inventory[item] or most_abundant[1] == 0:
            most_abundant = (item, inventory[item])
        if less_abundant[1] > inventory[item] or less_abundant[1] == 0:
            less_abundant = (item, inventory[item])
    print("\n=== Inventory Statistics ===")
    if most_abundant[1] > 1:
        print(f"Most abundant: {most_abundant[0]} ({most_abundant[1]} units)")
    else:
        print(f"Most abundant: {most_abundant[0]} ({most_abundant[1]} unit)")
    if less_abundant[1] > 1:
        print(f"Most abundant: {less_abundant[0]} ({less_abundant[1]} units)")
    else:
        print(f"Most abundant: {less_abundant[0]} ({less_abundant[1]} unit)")


def item_categories(inventory: dict[str, int]) -> None:
    inv_cat: dict[str, dict[str, int]] = {
        "abundant": {},
        "moderate": {},
        "scarce": {},
    }
    for item in inventory:
        if inventory[item] > 9:
            inv_cat["abundant"][item] = inventory[item]
        elif inventory[item] > 4:
            inv_cat["moderate"][item] = inventory[item]
        else:
            inv_cat["scarce"][item] = inventory[item]
    print("\n=== Item Categories ===")
    for cat in inv_cat:
        if inv_cat[cat]:
            print(f"{cat}: {inv_cat[cat]}")


def management_suggestions(inventory: dict[str, int]) -> None:
    item_to_restock: dict[str, int] = {}
    for item in inventory:
        if inventory[item] < 2:
            item_to_restock[item] = inventory[item]
    print("\n=== Management Suggestions ===")
    if item_to_restock:
        print(f"Restock needed: {list(item_to_restock.keys())}")


def dictionnary_properties_demo(inventory: dict[str, int]) -> None:
    print("\n=== Dictionnary Properties Demo ===")
    print(f"Dictionnary keys: {list(inventory.keys())}")
    print(f"Dictionnary values: {list(inventory.values())}")
    x = "sword" in inventory
    print(f"Sample lookup - 'sword' in inventory: {x}")


def inventory_report(inventory: dict[str, int]) -> None:
    nb_unique_items = len(inventory)
    nb_item_in_inventory = 0
    for n in inventory:
        nb_item_in_inventory += inventory[n]
    if nb_item_in_inventory == 0:
        print("Inventory is empty")
    else:
        print("=== Inventory System Analysis ===")
        print(f"Total items in inventory: {nb_item_in_inventory}")
        print(f"Unique item types: {nb_unique_items}")
        current_inventory(inventory, nb_item_in_inventory)
        inventory_statistics(inventory)
        item_categories(inventory)
        management_suggestions(inventory)
        dictionnary_properties_demo(inventory)


def main(argv: list[str]) -> None:
    inventory: dict[str, int] = {}
    try:
        if len(argv) <= 1:
            raise Exception
        i = 1
        while i < len(argv):
            key_value = argv[i].split(":")
            if len(key_value) != 2:
                raise Exception("Invalid input")
            if int(key_value[1]) > 0:
                inventory[key_value[0]] = int(key_value[1])
            if int(key_value[1]) < 0:
                raise Exception("Nb of item in inventory cannot be negative")
            i += 1
    except Exception as err:
        print(err)
        return
    inventory_report(inventory)


if __name__ == "__main__":
    main(sys.argv)
