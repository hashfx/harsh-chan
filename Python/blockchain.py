from block import Block
import datetime as date
from constraints import DIFFICULTY

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), date.datetime.now(), transactions, previous_block.hash)
        new_block.mine_block()  # Mine the new block with set difficulty
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

if __name__ == "__main__":
    blockchain = Blockchain()

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

