import sys

class Miner:

    def __init__(self, host, port, miners, genesis):
        pass # TODO

    def broadcast(self, block):
        pass # TODO

    def run(self):
        pass # TODO


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
    # TODO
