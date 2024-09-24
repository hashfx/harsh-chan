from constraints import DIFFICULTY
import hashlib
import datetime as date
import random, string

class Block:
    """
    Represents a single block in blockchain
    contains { index, timestamp, data, hash of previous block, nonce, current block hash }
    """
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    # generates final hash of current block
    def calculate_hash(self):
        hash_string = (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce))
        return hashlib.sha256(hash_string.encode()).hexdigest()

    # Prefix blocks with 'difficulty' number of zeros
    def mine_block(self):
        target = '0' * DIFFICULTY
        while self.hash[:DIFFICULTY] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")


if __name__ == "__main__":
    new_block = Block(1, date.datetime.now(), "transactions", "previous_block.hash")
    print(f"Block #{new_block.index} has been added to the blockchain with hash: {new_block.hash}")

