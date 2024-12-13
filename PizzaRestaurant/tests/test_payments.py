from payment import PayPal, CreditCard

def test_paypal_payment(capsys):
    paypal = PayPal()
    paypal.pay(10.0)
    captured = capsys.readouterr()
    assert "Paid $10.00 using PayPal." in captured.out

def test_creditcard_payment(capsys):
    credit_card = CreditCard()
    credit_card.pay(15.0)
    captured = capsys.readouterr()
    assert "Paid $15.00 using Credit Card." in captured.out
