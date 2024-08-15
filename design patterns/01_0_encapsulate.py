class PaymentBase:
    def __init__(self, amount:int):
        self.amount:int = amount

    def process_payment(self):
        pass

class CreditCard(PaymentBase):
    def process_payment(self):
        msg = f"Credit Card Payment: {self.amount}"
        print(msg)
        
class Paypal(PaymentBase):
    def process_payment(self):
        msg = f"Paypal Payment: {self.amount}"
        print(msg)

if __name__ == "__main__":
    payments = [CreditCard(200), Paypal(300)]
    for payment in payments:
        payment.process_payment()