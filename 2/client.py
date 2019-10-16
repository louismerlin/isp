import asyncio
import websockets
import hashlib
import binascii
import random

# h = hashlib.sha256()
# h.update(some_bigendian_bytes)
# h.update(some_utf8_string)
# bigendian_bytes_result = h.digest()

EMAIL = "your.email@epfl.ch"
PASSWORD = "correct horse battery staple"
# H = sha256
N = int("EEAF0AB9ADB38DD69C33F80AFA8FC5E86072618775FF3C0B9EA2314C9C256576D674DF7496EA81D3383B4813D692C6E0E0D5D8E250B98BE48E495C1D6089DAD15DC7D7B46154D6B6CE8EF4AD69B15D4982559B297BCF1885C529F566660E57EC68EDBC3C05726CC02FD4CBF4976EAA9AFD5138FE8376435B9FC61D2FC0EB06E3", 16)
g = 2

# Encoding
# number = 123456789
# bigendian_array = number.to_bytes((number.bit_length() + 7) // 8, 'big')
# utf8_hexadecimalstring = binascii.hexlify(bigendian_array).decode()
# await websocket.send(utf8_hexadecimalstring) 

# Decoding
# utf8_message = await websocket.recv()
# bigendian_bytes = binascii.unhexlify(utf8_message)
# number = int.from_bytes(bigendian_bytes, 'big')

# randomInt(32)

async def hello():
  uri = "ws://127.0.0.1:5000/"
  async with websockets.connect(uri) as websocket:
    # Send encoded email
    await websocket.send(EMAIL.encode())
    # Receive the encoded salt
    salt_encoded = await websocket.recv()
    # Decode the salt
    salt_bigendian = binascii.unhexlify(salt_encoded)
    salt = int.from_bytes(salt_bigendian, 'big')
    # Create a random a
    a = random.randint(1, 10**96)
    # Compute g ^ a mod N
    A = g^a % N
    # Encode A
    A_bigendian = A.to_bytes((A.bit_length() + 7) // 8, 'big')
    A_hexadecimal = binascii.hexlify(A_bigendian)
    # Send encoded A
    await websocket.send(A_hexadecimal) 
    # Receive encoded B
    B_encoded = await websocket.recv()
    # Decode B
    B_bigendian = binascii.unhexlify(B_encoded)
    B = int.from_bytes(B_bigendian, 'big')
    # u = H(A || B)
    h = hashlib.sha256()
    h.update(A_bigendian)
    h.update(B_bigendian)
    u = h.digest()
    # x = H(salt || H(U || ":" || PASSWORD))
    h1 = hashlib.sha256()
    h1.update(salt_bigendian)
    h2 = hashlib.sha256()
    h2.update(EMAIL.encode())
    h2.update(":".encode())
    h2.update(PASSWORD.encode())
    x2 = h2.digest()
    h1.update(x2)
    x = h1.digest()
    # S = (B - g^x) ^ (a + u * x) % N
    x_int = int.from_bytes(x, 'big')
    u_int = int.from_bytes(u, 'big')
    # S = (B - g ** x_int) ** (a + u_int * x_int) % N
    S = pow(B - pow(g, x_int, N), (a + u_int * x_int), N)
    print("S:", S)
    S_bigendian = S.to_bytes((S.bit_length() + 7) // 8, 'big')
    h = hashlib.sha256()
    h.update(A_bigendian)
    h.update(B_bigendian)
    h.update(S_bigendian)
    final = h.digest()
    final_hexadecimal = binascii.hexlify(final)
    await websocket.send(final_hexadecimal)
    print(await websocket.recv())

asyncio.get_event_loop().run_until_complete(hello())
