from pizza import PizzaFactory, Cheese, Olives
from inventory import InventoryManager
from payment import PayPal

if __name__ == "__main__":
    pizza = PizzaFactory.create_pizza("Margherita")

    inventory = InventoryManager()
    if inventory.check_availability("Cheese"):
        pizza = Cheese(pizza)
        inventory.use_ingredient("Cheese")

    if inventory.check_availability("Olives"):
        pizza = Olives(pizza)
        inventory.use_ingredient("Olives")

    print("Order:", pizza.get_description())
    print("Total Cost: $", pizza.cost())

    payment = PayPal()
    payment.pay(pizza.cost())
