import sys
import multiprocessing
import socket
import time
from blockchain import BlockChain
from block import Block

class Miner:

    def __init__(self, host, port, miners, genesis):
        self.host = host
        self.port = port
        self.miners = miners
        self.queue = multiprocessing.Queue()
        self.genesis = genesis
        self.blockchain = None

    def broadcast(self, block):
        for miner in miners:
            [host, port] = miner.split(":")
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(block.encode(), (host, int(port)))
    
    def create_blocks(self):
        while True:
            time.sleep(1)
            if self.blockchain != None:
                block = Block("random", self.blockchain.chain[-1].hash())
                self.queue.put(block)
                self.broadcast(block)
    
    def add_blocks(self):
        while True:
            block = self.queue.get()
            print(block.hash())
            if self.blockchain == None:
                self.blockchain = BlockChain(block)
            else:
                self.blockchain.append(block)
            print(self.blockchain.chain[-1].hash())

    def run(self):
        # Create the genesis block if you are the genesis miner
        if self.genesis:
            self.blockchain = BlockChain(Block("GENESIS", bytes()))

        # Create a thead for block creating
        block_creator = multiprocessing.Process(target=self.create_blocks)
        block_creator.start()

        # Create a thead for block adding
        block_adder = multiprocessing.Process(target=self.add_blocks)
        block_adder.start()

        # Listen for blocks
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.host, int(self.port)))
        while True:
            data, addr = sock.recvfrom(5120)
            block = Block.decode(data)
            self.queue.put(block)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 miner.py [addr] [others] [genesis|]")
        print("\taddr:\t\taddress of the miner in the format" \
             "host:port")
        print("\tothers:\t\tcomma-separated list of the other" \
              "miners' addresses \n\t\t\tin the format host:port," \
              "host:port,...")
        print("\tgenesis:\toptional, \"genesis\" if the miner must" \
                "generate\n\t\t\tthe genesis block") 
        sys.exit(0)
    addr = sys.argv[1]
    others = sys.argv[2]
    genesis = False
    if len(sys.argv) > 3:
        if sys.argv[3] == "genesis":
            genesis = True
    [host, port] = addr.split(":")
    miners = others.split(",")
    miner = Miner(host, port, miners, genesis)
    miner.run()
