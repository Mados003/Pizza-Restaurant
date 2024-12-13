# Design Patterns and Their Applications

## Factory Pattern
**Purpose**: Encapsulates the creation of objects, ensuring that the logic for object instantiation is centralized and reusable.

### Application in Code
- The **PizzaFactory** class is responsible for creating `Pizza` objects (`Margherita` or `Pepperoni`), removing the need for the main program to handle instantiation logic.
- New pizza types can be added without modifying the main program.

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
Decorator Pattern
Purpose: Dynamically adds behavior or responsibilities to objects without modifying their code.

Application in Code
Toppings such as Cheese, Olives, and Mushrooms are added to Pizza objects without altering the base pizza classes.
Each topping is represented as a decorator, which appends its description and cost to the pizza.
Example
python
Copy code
class Cheese(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Cheese"

    def cost(self):
        return self.pizza.cost() + 1.0
Benefits
Makes it easy to add new toppings.
Promotes code reusability and flexibility.
Singleton Pattern
Purpose: Ensures that a class has only one instance and provides a global point of access to that instance.

Application in Code
The InventoryManager class is implemented as a singleton to manage the availability of ingredients in a consistent manner.
Example
python
Copy code
class InventoryManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.inventory = {"Cheese": 10, "Olives": 10, "Mushrooms": 10}
        return cls._instance
Benefits
Prevents multiple instances of the inventory manager, ensuring accurate tracking of inventory.
Strategy Pattern
Purpose: Enables the selection of an algorithm (or behavior) at runtime by defining a family of algorithms and encapsulating them in separate classes.

Application in Code
Payment methods such as PayPal and CreditCard are implemented as strategies that share the same interface (PaymentMethod).
Example
python
Copy code
class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using PayPal.")
Benefits
New payment methods can be added easily.
Promotes separation of concerns and adheres to the Open/Closed Principle.
Overengineering in the System
Definition: Overengineering occurs when unnecessary complexity is introduced to a system, often by anticipating future requirements that may never arise.

Example of Overengineering
Implementing a database for inventory management in a small application is unnecessary. Using a simple dictionary suffices for the current requirements.

python
Copy code
# Overengineered Inventory Management
class DatabaseInventoryManager:
    def __init__(self):
        self.connection = DatabaseConnection()

    def check_availability(self, topping):
        # Query the database for topping availability
        pass
How to Avoid Overengineering
Focus on solving current problems rather than anticipating every possible future need.
Add complexity only when it is justified by real requirements.
Summary
By applying the appropriate design patterns—Factory, Decorator, Singleton, and Strategy—the project achieves:

Modularity
Extensibility
Maintainability