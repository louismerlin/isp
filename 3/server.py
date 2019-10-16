from flask import Flask, request
import bcrypt

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hash_password(): 
  data = request.get_json()
  hashed = bcrypt.hashpw(data.pass, bcrypt.gensalt())
  return hashed, 200

if __name__ == "__main__":
  app.run()
