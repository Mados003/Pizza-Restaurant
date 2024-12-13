class Pizza:
    def __init__(self):
        self.description = "Unknown Pizza"

    def get_description(self):
        return self.description

    def cost(self):
        return 0.0

class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"

    def cost(self):
        return 5.0

class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Pepperoni Pizza"

    def cost(self):
        return 6.0

class PizzaFactory:
    @staticmethod
    def create_pizza(type):
        if type == "Margherita":
            return MargheritaPizza()
        elif type == "Pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError("Invalid pizza type.")

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
