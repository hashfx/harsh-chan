import random, string

class Wallet:
    """
    Generates unique wallet address of 8 characters for users
    """
    def __init__(self):
        self.addresses = {}

    def create_wallet(self, user_name):
        # Generate a short and unique wallet address (e.g., 8 characters long)
        address = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        # Ensure uniqueness by checking existing addresses
        while address in self.addresses.values():
            address = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.addresses[user_name] = address
        print(f"Wallet created for {user_name}: Address = {address}")
        return address

    def get_address(self, user_name):
        return self.addresses.get(user_name, None)


if __name__ == "__main__":
    wallet = Wallet()
    wallet.create_wallet("user_name")