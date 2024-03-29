import time
import datetime
import hashlib

DIGESTS_1a = [
  "7c58133ee543d78a9fce240ba7a273f37511bfe6835c04e3edf66f308e9bc6e5",
  "37a2b469df9fc4d31f35f26ddc1168fe03f2361e329d92f4f2ef04af09741fb9",
  "19dbaf86488ec08ba7a824b33571ce427e318d14fc84d3d764bd21ecb29c34ca",
  "06240d77c297bb8bd727d5538a9121039911467c8bb871a935c84a5cfe8291e4",
  "f5cd3218d18978d6e5ef95dd8c2088b7cde533c217cfef4850dd4b6fa0deef72",
  "dd9ad1f17965325e4e5de2656152e8a5fce92b1c175947b485833cde0c824d64",
  "845e7c74bc1b5532fe05a1e682b9781e273498af73f401a099d324fa99121c99",
  "a6fb7de5b5e11b29bc232c5b5cd3044ca4b70f2cf421dc02b5798a7f68fc0523",
  "1035f3e1491315d6eaf53f7e9fecf3b81e00139df2720ae361868c609815039c",
  "10dccbaff60f7c6c0217692ad978b52bf036caf81bfcd90bfc9c0552181da85a",
]

print("\033[1mPart 1a: Brute force attack\033[0m")

possible_characters = "0123456789abcdefghijklmnopqrstuvwxyz"

def brute_crack():
  for a in possible_characters:
    p1 = a
    for b in possible_characters:
      p2 = p1 + b
      for c in possible_characters:
        p3 = p2 + c
        for d in possible_characters:
          p4 = p3 + d
          if try_password(p4):
            return
          for e in possible_characters:
            p5 = p4 + e
            if try_password(p5):
              return
            for f in possible_characters:
              p6 = p5 + f
              if try_password(p6):
                return

def try_password(password):
  global solved
  hashed = hashlib.sha256(password.encode()).hexdigest()

  for idx, h in enumerate(DIGESTS_1a):
    if hashed == h:
      print(h, "=>", password)
      del DIGESTS_1a[idx]
      if len(DIGESTS_1a) <= 0:
        return True
  return False

start = time.process_time()

brute_crack()

end = time.process_time()

print("1a took", str(datetime.timedelta(seconds=round(end - start))))
