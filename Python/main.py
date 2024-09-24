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

# importing blockchains-components modules
from block import Block
from blockchain import Blockchain
from wallet import Wallet

if __name__ == "__main__":
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