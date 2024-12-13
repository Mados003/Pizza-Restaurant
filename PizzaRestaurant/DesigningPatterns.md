# Design Patterns and Their Applications

## Factory Pattern
**Purpose**: To centralize the creation of pizza objects, making the system modular and easy to extend.

### Application in Code
- The `PizzaFactory` class is used to create different types of pizzas (`Margherita`, `Pepperoni`).
- Adding a new pizza type is as simple as extending the `Pizza` class and updating the factory.

### Example
```python
class PizzaFactory:
    @staticmethod
    def create_pizza(type):
        if type == "Margherita":
            return MargheritaPizza()
        elif type == "Pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError("Invalid pizza type.")
```

---

## Decorator Pattern
**Purpose**: To add toppings to pizzas dynamically without modifying the base pizza classes.

### Application in Code
- Toppings such as `Cheese`, `Olives`, and `Mushrooms` are implemented as decorators that wrap around a `Pizza` object.
- Each topping appends its cost and description to the base pizza.

### Example
```python
class Cheese(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Cheese"

    def cost(self):
        return self.pizza.cost() + 1.0
```

### Benefits
- New toppings can be added without modifying existing pizza classes or decorators.

---

## Singleton Pattern
**Purpose**: To ensure only one instance of the inventory manager exists across the system.

### Application in Code
- The `InventoryManager` class is implemented as a singleton to maintain a single source of truth for ingredient availability.

### Example
```python
class InventoryManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.inventory = {"Cheese": 10, "Olives": 10, "Mushrooms": 10}
        return cls._instance
```

### Benefits
- Prevents multiple instances that could lead to inconsistent inventory management.

---

## Strategy Pattern
**Purpose**: To provide multiple payment methods that follow a common interface, allowing the system to choose the appropriate method dynamically.

### Application in Code
- Payment methods such as `PayPal` and `CreditCard` implement the `PaymentMethod` interface.

### Example
```python
class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using PayPal.")
```

### Benefits
- New payment methods can be added without modifying the existing ones.

---

## Summary
By using the **Factory**, **Decorator**, **Singleton**, and **Strategy** patterns, the system achieves:
- **Modularity**: Each component has a specific responsibility.
- **Extensibility**: New pizzas, toppings, and payment methods can be added easily.
- **Maintainability**: The code is clean and easy to understand.
