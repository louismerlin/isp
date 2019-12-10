import base64
import json
import hashlib

class Block:
    def __init__(self, data, previous):
        self.data = data
        self.previous_hash = previous

    def hash(self):
        h = hashlib.sha256()
        h.update(self.data.encode())
        h.update(self.previous_hash)
        return h.digest()

    def encode(self):
        data = base64.b64encode(self.data.encode("utf-8")).decode("utf-8")
        previous = ''.join(format(x, '02x') for x in self.previous_hash) 
        return json.dumps({"data": data, "previous": previous}).encode("utf-8")

    @staticmethod
    def decode(b):
        block = json.loads(b.decode("utf-8"))
        data = block["data"].encode("utf-8")
        return Block(base64.b64decode(data), bytes.fromhex(block["previous"]))
