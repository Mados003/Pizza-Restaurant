from pizza import PizzaFactory, Cheese, Olives, Mushrooms
from inventory import InventoryManager
from payment import PayPal


def main():
    inventory = InventoryManager()

    print("Welcome to the Pizza Restaurant!")

    while True:
        print("\nChoose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0. Exit")
        pizza_choice = input("Enter the number of your choice: ")

        if pizza_choice == "0":
            break

        try:
            pizza_type = "Margherita" if pizza_choice == "1" else "Pepperoni"
            pizza = PizzaFactory.create_pizza(pizza_type)

            if not inventory.check_availability(pizza.get_description()):
                print("Sorry, that pizza is out of stock!")
                continue
        except ValueError as e:
            print(e)
            continue

        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            if topping_choice == "1":
                if inventory.check_availability("Cheese"):
                    pizza = Cheese(pizza)
                    inventory.use_ingredient("Cheese")
                else:
                    print("Cheese is out of stock!")
            elif topping_choice == "2":
                if inventory.check_availability("Olives"):
                    pizza = Olives(pizza)
                    inventory.use_ingredient("Olives")
                else:
                    print("Olives are out of stock!")
            elif topping_choice == "3":
                if inventory.check_availability("Mushrooms"):
                    pizza = Mushrooms(pizza)
                    inventory.use_ingredient("Mushrooms")
                else:
                    print("Mushrooms are out of stock!")
            elif topping_choice == "4":
                break
            else:
                print("Invalid choice. Try again.")

        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.cost():.2f}")

        payment = PayPal()
        payment.pay(pizza.cost())

        print("\nRemaining Inventory:")
        print(inventory.get_inventory())

    print("\nThank you for visiting the Pizza Restaurant!")


if __name__ == "__main__":
    main()
