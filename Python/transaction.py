from wallet import Wallet

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __repr__(self):
        return f"{self.sender} sends {self.amount} coins to {self.receiver}"

    @staticmethod
    def add_user_transaction(wallet):
        sender_name = input("Enter the sender's name: ").strip()
        receiver_name = input("Enter the receiver's name: ").strip()
        
        
        sender = wallet.get_address(sender_name) or wallet.create_wallet(sender_name)
        receiver = wallet.get_address(receiver_name) or wallet.create_wallet(receiver_name)
        
        try:
            amount = float(input("Enter the amount to transfer: ").strip())
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
        except ValueError as e:
            print(f"Invalid amount: {e}")
            return None

        return Transaction(sender, receiver, amount)

if __name__ == "__main__":
    wallet = Wallet()
    transaction = Transaction("a", "b", 25)
    print(transaction)
    newTransaction = Transaction.add_user_transaction(wallet)
    print("New Transaction: ", newTransaction)