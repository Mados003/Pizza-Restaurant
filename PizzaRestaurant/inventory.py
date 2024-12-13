class InventoryManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.inventory = {
                "Margherita": 10,
                "Pepperoni": 10,
                "Cheese": 15,
                "Olives": 10,
                "Mushrooms": 12,
            }
        return cls._instance

    def check_availability(self, item):
        return self.inventory.get(item, 0) > 0

    def use_ingredient(self, item):
        if self.check_availability(item):
            self.inventory[item] -= 1
        else:
            raise Exception(f"{item} is out of stock.")

    def get_inventory(self):
        return self.inventory
