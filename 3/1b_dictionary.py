import time
import datetime
import random
import hashlib

print("\033[1mPart 1b: Dictionary attack with rules\033[0m")

DIGESTS_1b = [
  "2e41f7133fd134335f566736c03cc02621a03a4d21954c3bec6a1f2807e87b8a",
  "7987d2f5f930524a31e0716314c2710c89ae849b4e51a563be67c82344bcc8da",
  "076f8c265a856303ac6ae57539140e88a3cbce2a2197b872ba6894132ccf92fb",
  "b1ea522fd21e8fe242136488428b8604b83acea430d6fcd36159973f48b1102e",
  "fa5700d75974a94dd73f7c5d48e85afa87beba19b873d4eb8d411dd251560321",
  "326e90c0d2e7073d578976d120a4071f83ce6b7bc89c16ecb215d99b3d51a29b",
  "269398301262810bdf542150a2c1b81ffe0e1282856058a0e26bda91512cfdc4",
  "4fbee71939b9a46db36a3b0feb3d04668692fa020d30909c12b6e00c2d902c31",
  "55c5a78379afce32da9d633ffe6a7a58fa06f9bbe66ba82af61838be400d624e",
  "5106610b8ac6bc9da787a89bf577e888bce9c07e09e6caaf780d2288c3ec1f0c"
]

solved = 0

file = open("rockyou.txt", encoding ='ISO-8859-1').read().splitlines()

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def coin_toss(n):
  return random.randint(0, n) == 0

start = time.process_time()

while len(DIGESTS_1b) > 0:
  random_password = random.choice(file).strip()
  occurencesOfE = findOccurrences(random_password, 'e')
  occurencesOfO = findOccurrences(random_password, 'o')
  occurencesOfI = findOccurrences(random_password, 'i')
  if coin_toss(1):
    random_password = random_password.title()
  for index in occurencesOfE:
    if coin_toss(len(occurencesOfE)):
      p = list(random_password)
      p[index] = '3'
      random_password = "".join(p)
  for index in occurencesOfO:
    if coin_toss(len(occurencesOfO)):
      p = list(random_password)
      p[index] = '0'
      random_password = "".join(p)
  for index in occurencesOfI:
    if coin_toss(len(occurencesOfI)):
      p = list(random_password)
      p[index] = '1'
      random_password = "".join(p)
  hashed = hashlib.sha256(random_password.encode()).hexdigest()
  for idx, h in enumerate(DIGESTS_1b):
    if hashed == h:
      print(h, "=>", random_password)
      del DIGESTS_1b[idx]

end = time.process_time()

print("1b took", str(datetime.timedelta(seconds=round(end - start))))
