from pizza import PizzaFactory, Cheese, Olives

def test_pizza_creation():
    pizza = PizzaFactory.create_pizza("Margherita")
    assert pizza.get_description() == "Margherita Pizza"
    assert pizza.cost() == 5.0

def test_toppings():
    pizza = PizzaFactory.create_pizza("Pepperoni")
    pizza = Cheese(pizza)
    pizza = Olives(pizza)
    assert pizza.get_description() == "Pepperoni Pizza, Cheese, Olives"
    assert pizza.cost() == 7.5
