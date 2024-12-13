from inventory import InventoryManager

def test_inventory():
    inventory = InventoryManager()
    assert inventory.check_availability("Cheese") is True
    inventory.use_ingredient("Cheese")
    assert inventory.inventory["Cheese"] == 9
