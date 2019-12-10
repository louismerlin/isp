class BlockChain:

    def __init__(self, genesis_block):
        self.root = genesis_block
        self.chain = [genesis_block]

    def append(self, new_block):
        if new_block.previous_hash == self.chain[-1].hash():
            self.chain.append(new_block)
