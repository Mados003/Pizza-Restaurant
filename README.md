# Pizza-Restaurant

## Overview
The **Pizza-Restaurant** is a Python-based console application that allows users to order pizzas, customize them with various toppings, and make payments. The application uses several design patterns, including Factory, Decorator, Singleton, and Strategy, to ensure modularity, maintainability, and extensibility.

---

## Features
- **Pizza Types**: Choose between Margherita and Pepperoni pizzas.
- **Custom Toppings**: Add toppings like Cheese, Olives, and Mushrooms dynamically.
- **Inventory Management**: Tracks ingredient availability using a Singleton pattern.
- **Multiple Payment Methods**: Supports PayPal and Credit Card payments.
- **Real-Time Order Summary**: Displays the final cost and description of the pizza after customization.

---

## Installation and Setup

### Prerequisites
- Python 3.9 or later

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Mados003/Pizza-Restaurant.git
   cd PizzaRestaurant
   ```

2. Install dependencies (if required):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## Usage
1. **Start the Application**: Follow the on-screen prompts to choose your pizza and customize it.
2. **Select Pizza Base**:
   - Margherita ($5.0)
   - Pepperoni ($6.0)
3. **Add Toppings**:
   - Cheese ($1.0)
   - Olives ($0.5)
   - Mushrooms ($0.7)
4. **Finalize and Pay**:
   - Review the order details.
   - Choose a payment method (PayPal or Credit Card).

---

## Directory Structure
```
PizzaRestaurant/
├── main.py             # Main application logic
├── pizza.py            # Pizza classes, Topping decorators, and Factory
├── inventory.py        # Singleton inventory manager
├── payment.py          # Payment strategy classes
├── tests/              # Unit tests for the application
│   ├── test_inventory.py
│   ├── test_pizza.py
│   └── test_payment.py
```

---

## Example Workflow
1. **Choose a Base Pizza**:
   ```
   Choose your base pizza:
   1. Margherita ($5.0)
   2. Pepperoni ($6.0)
   0. Exit
   Enter the number of your choice: 1
   ```

2. **Add Toppings**:
   ```
   Available toppings:
   1. Cheese ($1.0)
   2. Olives ($0.5)
   3. Mushrooms ($0.7)
   4. Finish order
   Enter the number of your choice: 1
   ```

3. **Review the Order**:
   ```
   Your order:
   Description: Margherita, Cheese
   Total cost: $6.00
   ```

4. **Make Payment**:
   ```
   Paid $6.00 using PayPal.
   ```

---

## Testing
Run the unit tests to verify the functionality of the application:
```bash
pytest tests/
```

---

## Design Patterns Used
1. **Factory Pattern**: Simplifies the creation of pizza objects.
2. **Decorator Pattern**: Dynamically adds toppings to pizzas without modifying base classes.
3. **Singleton Pattern**: Ensures a single instance of `InventoryManager`.
4. **Strategy Pattern**: Abstracts payment methods for extensibility.

---

## Contribution
Feel free to fork the repository and submit pull requests for enhancements or bug fixes.

---

## Contact
For any questions or issues, please contact the project maintainer.

