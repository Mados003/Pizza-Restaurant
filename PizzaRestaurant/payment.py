class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError


class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using PayPal.")


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using Credit Card.")
