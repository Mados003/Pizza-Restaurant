from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass


class MargheritaPizza(Pizza):
    def __init__(self):
        self.description = "Margherita"

    def get_description(self):
        return self.description

    def cost(self):
        return 5.0


class PepperoniPizza(Pizza):
    def __init__(self):
        self.description = "Pepperoni"

    def get_description(self):
        return self.description

    def cost(self):
        return 6.0


# Decorator for Toppings
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def cost(self):
        return self.pizza.cost()


class Cheese(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Cheese"

    def cost(self):
        return self.pizza.cost() + 1.0


class Olives(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Olives"

    def cost(self):
        return self.pizza.cost() + 0.5


class Mushrooms(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Mushrooms"

    def cost(self):
        return self.pizza.cost() + 0.7


class PizzaFactory:
    @staticmethod
    def create_pizza(type):
        if type == "Margherita":
            return MargheritaPizza()
        elif type == "Pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError("Invalid pizza type.")
