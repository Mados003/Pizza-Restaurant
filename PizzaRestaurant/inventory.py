class InventoryManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.inventory = {"Cheese": 10, "Olives": 10, "Mushrooms": 10}
        return cls._instance

    def check_availability(self, topping):
        return self.inventory.get(topping, 0) > 0

    def use_ingredient(self, topping):
        if self.check_availability(topping):
            self.inventory[topping] -= 1
        else:
            raise Exception(f"{topping} is out of stock.")
