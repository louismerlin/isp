import random
import requests
import phe as paillier

# Exercise 1

print("Exercise 1")

# Generate a public/private key pair
pubkey, privkey = paillier.generate_paillier_keypair(n_length=2048)

def encrypt_vector(x):
    return [pubkey.encrypt(i, precision=2**-16).ciphertext() for i in x]

def decrypt_value(x):
    return privkey.decrypt(x)

def query_pred(feature_vector):
    encrypted_vector = encrypt_vector(feature_vector)
    response = requests.post('http://hw7prediction:8000/prediction', json={'pub_key_n': pubkey.n, 'enc_feature_vector': encrypted_vector})
    prediction = paillier.EncryptedNumber(pubkey, response.json()['enc_prediction'], exponent=-8)
    decrypted_prediction = decrypt_value(prediction)
    return decrypted_prediction

assert 2**(-16) > abs(query_pred([0.48555949, 0.29289251, 0.63463107, 
                                  0.41933057, 0.78672205, 0.58910837,
                                  0.00739207, 0.31390802, 0.37037496,
                                  0.3375726 ]) - 0.44812144746653826)

print("SUCCESS")

# Exercise 2

print("Exercise 2")

empty_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# The constant b can be deduced with the empty list as argument
b = query_pred(empty_list)

# And w can be deduced value by value by putting a "1" in each slot
w = []
for i in range(10):
    l = list(empty_list)
    l[i] = 1
    w.append(query_pred(l) - b)

print("w:")
print(w)
print("b:")
print(b)

# Let's try this out with a random array :

random_array = [random.random() for _ in range(10)]

random_multiplied_array = []
for i in range(10):
    random_multiplied_array.append(random_array[i] * w[i])

a_priori_value = sum(random_multiplied_array) + b

assert 2 ** (-16) > abs(query_pred(random_array) - a_priori_value)

print("SUCCESS")
