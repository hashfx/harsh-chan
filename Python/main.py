"""
BlockChain:
    System of recording information, impossible to change or hack, distributed across entire network, hashed blocks

BlockChain Coin:
    transaction1(t1): A sends 2 coins to B
    transaction2(t2): C sends 4 coins to D
    transaction3(t3): E sends 8 coins to E

    block_syntax (for current program):
        [hash_of_previous_block, transaction1, transaction2, transaction3..., current_block]
    block1(b1): ("String", t1, t2, t3) -> hash(b1),
        b2: ("hash(b1)", t4, t5, t6) -> hash(b2),
        b3: ("hash(b2)", t7, t8) -> hash(b3)

    Change in one block would change its hash, which would change hash of the other blocks too,
    therefore changing is not possible in the blockchain.

"""
import hashlib
import datetime as date
import random, string

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_string = (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce))
        return hashlib.sha256(hash_string.encode()).hexdigest()

    # Prefix blocks with 'difficulty' number of zeros
    def mine_block(self, difficulty=2):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __repr__(self):
        return f"{self.sender} sends {self.amount} coins to {self.receiver}"

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), date.datetime.now(), transactions, previous_block.hash)
        new_block.mine_block(self.difficulty)  # Mine the new block with set difficulty
        self.chain.append(new_block)
        print(f"Block #{new_block.index} has been added to the blockchain with hash: {new_block.hash}")

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

class Wallet:
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

def get_user_transaction(wallet):
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


# Create the blockchain
blockchain = Blockchain()
wallet = Wallet()

# Add blocks to the blockchain
blockchain.add_block("Transaction Data 1")
blockchain.add_block("Transaction Data 2")
blockchain.add_block("Transaction Data 3")

# Print the contents of the blockchain
for block in blockchain.chain:
    print("Block #" + str(block.index))
    print("Nonce: " + str(block.nonce))
    print("Timestamp: " + str(block.timestamp))
    print("Data: " + str(block.data))
    print("Hash: " + block.hash)
    print("Previous Hash: " + block.previous_hash)
    print("\n")