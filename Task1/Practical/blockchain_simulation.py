import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + self.timestamp + self.data + self.previous_hash + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

block1 = Block(1, str(time.time()), "Block 1 Data", "0")
block2 = Block(2, str(time.time()), "Block 2 Data", block1.hash)
block3 = Block(3, str(time.time()), "Block 3 Data", block2.hash)
block4 = Block(4,str(time.time()),"Block 4 Data",block3.hash)

for block in [block1, block2, block3,block4]:
    print(f"Index: {block.index}, Hash: {block.hash}, Previous: {block.previous_hash}")
