# SOLID Principles and Design Patterns

## Single Responsibility Principle (SRP)
**Principle**: Each class should have one and only one reason to change.

### Application in Code
- The **PizzaFactory** class is responsible for creating pizza objects, separating the instantiation logic from the main program.
- The **ToppingDecorator** handles the logic for adding toppings, while the base pizza classes manage their respective properties.
- The **InventoryManager** focuses solely on managing inventory, adhering to SRP.

---

## Open/Closed Principle (OCP)
**Principle**: Software entities should be open for extension but closed for modification.

### Application in Code
- **PizzaFactory** can be extended to support new pizza types without modifying the existing factory code.
- **Decorator Pattern** allows new toppings to be added without changing the base pizza implementation.
- **Strategy Pattern** makes it easy to add new payment methods without altering the existing code.

---

## Liskov Substitution Principle (LSP)
**Principle**: Objects of a superclass should be replaceable with objects of a subclass without altering the correctness of the program.

### Application in Code
- Any `Pizza` instance can be replaced with a decorated `Pizza` (e.g., adding `Cheese`, `Olives`), ensuring the program behaves correctly.
- Payment methods (`PayPal`, `CreditCard`) adhere to the `PaymentMethod` interface, allowing seamless substitution.

---

## Interface Segregation Principle (ISP)
**Principle**: No client should be forced to depend on methods it does not use.

### Application in Code
- The **PaymentMethod** interface defines a single `pay` method, ensuring each payment class (e.g., `PayPal`, `CreditCard`) implements only the required behavior.

---

## Dependency Inversion Principle (DIP)
**Principle**: High-level modules should depend on abstractions, not concrete implementations.

### Application in Code
- The **Strategy Pattern** ensures that the `main.py` script depends on the `PaymentMethod` abstraction rather than concrete classes like `PayPal` or `CreditCard`.

---

### Summary
By applying these principles and patterns, the project achieves a modular, extensible, and maintainable design.
